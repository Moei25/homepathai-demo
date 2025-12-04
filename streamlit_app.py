import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# -------------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------------
st.set_page_config(
    page_title="HomePathAI Demo",
    layout="wide"
)

# -------------------------------------------------------------
# GLOBAL STYLES (MATCH SCREENSHOT)
# -------------------------------------------------------------
st.markdown(
    """
    <style>
        /* PAGE BACKGROUND */
        body {
            background-color: #F4F7FB;
        }
        .main {
            background-color: #F4F7FB;
        }

        /* REMOVE DEFAULT PADDING TOP */
        .block-container {
            padding-top: 1.5rem;
        }

        /* HEADER */
        .hp-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 8px;
        }
        .hp-logo-circle {
            width: 42px;
            height: 42px;
            border-radius: 12px;
            background: #0A7C8B;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 700;
            font-size: 18px;
        }
        .hp-title-text {
            font-size: 24px;
            font-weight: 700;
            color: #004F6E;
        }
        .hp-subtitle {
            font-size: 12px;
            color: #5F6B7A;
            margin-top: -4px;
        }

        /* TOP NAV BAR */
        .hp-nav-row {
            display: flex;
            gap: 10px;
            margin-top: 18px;
            margin-bottom: 24px;
        }

        /* STYLE ALL STREAMLIT BUTTONS AS NAV PILLS */
        .stButton > button {
            background: #0A7C8B;
            color: #FFFFFF;
            padding: 12px 26px;
            border-radius: 10px;
            border: none;
            font-size: 13px;
            font-weight: 600;
            box-shadow: 0 3px 6px rgba(0,0,0,0.18);
            cursor: pointer;
        }
        .stButton > button:hover {
            background: #086874;
        }

        /* ACTIVE NAV PILL (we'll target via custom data attribute) */
        .hp-active-nav {
            background: #005E6D !important;
        }

        /* HERO SEARCH CARD */
        .hp-hero-card {
            background: linear-gradient(135deg, #0086B3, #00AECB, #0A9A5A);
            border-radius: 10px;
            padding: 24px 28px;
            color: white;
            margin-bottom: 26px;
        }
        .hp-hero-title {
            font-size: 24px;
            font-weight: 700;
            margin: 0 0 4px 0;
        }
        .hp-hero-subtitle {
            font-size: 13px;
            opacity: 0.95;
        }
        .hp-hero-row {
            margin-top: 14px;
            display: flex;
            gap: 10px;
        }
        .hp-hero-input {
            flex: 1;
            padding: 12px 14px;
            border-radius: 8px;
            border: none;
            font-size: 14px;
        }
        .hp-hero-btn {
            padding: 12px 26px;
            border-radius: 8px;
            border: none;
            background: #00837A;
            color: white;
            font-weight: 600;
            font-size: 14px;
            cursor: pointer;
        }
        .hp-hero-helper {
            margin-top: 10px;
            font-size: 12px;
            opacity: 0.9;
        }

        /* GENERIC CARD */
        .hp-card {
            background: white;
            border-radius: 16px;
            padding: 18px 18px 16px 18px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        }

        /* SECTION TITLE */
        .hp-section-title {
            font-size: 18px;
            font-weight: 700;
            color: #1F2D3D;
            display: flex;
            align-items: center;
            gap: 6px;
            margin-bottom: 2px;
        }
        .hp-section-sub {
            font-size: 12px;
            color: #67727E;
            margin-bottom: 14px;
        }

        /* NEIGHBORHOOD SNAPSHOT CARD */
        .hp-metric-label {
            font-size: 11px;
            color: #6C7A89;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .hp-metric-value-main {
            font-size: 26px;
            font-weight: 700;
            color: #004F6E;
        }
        .hp-metric-value-sub {
            font-size: 14px;
            color: #005E6D;
        }

        /* LISTING CARD */
        .hp-listing-img {
            width: 100%;
            border-radius: 14px;
            margin-bottom: 12px;
        }
        .hp-price {
            font-size: 22px;
            font-weight: 700;
            color: #004F6E;
        }
        .hp-line {
            font-size: 13px;
            color: #687280;
            margin-top: 1px;
        }
        .hp-city {
            font-size: 13px;
            color: #0A9A5A;
            margin-top: 8px;
        }
        .hp-pill-btn {
            padding: 8px 16px;
            background: #0A7C8B;
            color: white;
            border-radius: 999px;
            font-size: 12px;
            border: none;
            font-weight: 600;
            cursor: pointer;
        }
        .hp-listing-metrics-row {
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
        }
        .hp-listing-metric-label {
            font-size: 11px;
            text-transform: uppercase;
            color: #6C7A89;
        }
        .hp-listing-metric-value {
            font-size: 15px;
            font-weight: 600;
            color: #004F6E;
        }
        .hp-listing-metric-green {
            color: #0A9A5A;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------------
# SESSION STATE NAV
# -------------------------------------------------------------
if "active_page" not in st.session_state:
    st.session_state["active_page"] = "Home dashboard"


# -------------------------------------------------------------
# HEADER + NAV
# -------------------------------------------------------------
def render_header_and_nav():
    # header row
    st.markdown(
        """
        <div class="hp-header">
            <div class="hp-logo-circle">AI</div>
            <div>
                <div class="hp-title-text">HomePathAI</div>
                <div class="hp-subtitle">Neighborhood &amp; home insight assistant</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # nav row
    pages = [
        "Home dashboard",
        "First-time buyer friendly",
        "Investor deal analysis",
        "Neighbor insights",
        "Repair estimator",
        "Rent & moving tools",
    ]

    st.markdown('<div class="hp-nav-row">', unsafe_allow_html=True)
    cols = st.columns(len(pages))

    for i, p in enumerate(pages):
        is_active = (st.session_state["active_page"] == p)
        # we still use Streamlit buttons for routing
        with cols[i]:
            if st.button(p):
                st.session_state["active_page"] = p

    st.markdown("</div>", unsafe_allow_html=True)


# -------------------------------------------------------------
# HOME DASHBOARD - FULL SCREENSHOT STYLE
# -------------------------------------------------------------
def render_home_dashboard():
    # HERO BAR (search card)
    hero_html = """
    <div class="hp-hero-card">
        <div class="hp-hero-title">Smart search for your next home — powered by AI.</div>
        <div class="hp-hero-subtitle">
            Neighborhood insights, investor-grade numbers, repair tools, moving resources, and first-time buyer help —
            all in one experience built for real people.
        </div>

        <div class="hp-hero-row">
            <input class="hp-hero-input" placeholder="Search city, neighborhood, or ZIP" />
            <button class="hp-hero-btn">Search</button>
        </div>

        <div class="hp-hero-helper">
            Your AI-powered home search companion for smarter buying.
        </div>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)

    # SECTION TITLE (Trending homes)
    st.markdown(
        """
        <div class="hp-section-title">
            <span>🔥</span>
            <span>Trending homes near you</span>
        </div>
        <div class="hp-section-sub">
            Sample homes across Detroit and nearby areas — demo data only.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # HEATMAP + LISTING CARD LAYOUT
    left, right = st.columns([1.15, 1])

    # LEFT: Neighborhood snapshot card with heatmap
    with left:
        st.markdown(
            """
            <div class="hp-card">
                <div class="hp-section-title" style="margin-bottom:4px;">
                    <span>📍</span>
                    <span>Neighborhood snapshot</span>
                </div>
                <div class="hp-section-sub" style="margin-bottom:10px;">
                    Safety, price, and walkability at a glance — demo map.
                </div>
            """,
            unsafe_allow_html=True,
        )

        # build DataFrame for heatmap
        df = pd.DataFrame(
            {
                "lat": np.random.uniform(42.28, 42.42, 250),
                "lon": np.random.uniform(-83.5, -83.0, 250),
                "value": np.random.uniform(0, 1, 250),
            }
        )

        layer = pdk.Layer(
            "HeatmapLayer",
            df,
            get_position='[lon, lat]',
            opacity=0.9,
            threshold=0.2,
        )

        deck = pdk.Deck(
            layers=[layer],
            initial_view_state=pdk.ViewState(
                latitude=42.33,
                longitude=-83.1,
                zoom=9,
                pitch=40,
            ),
        )

        st.pydeck_chart(deck)

        # close card div
        st.markdown("</div>", unsafe_allow_html=True)

    # RIGHT: Listing card
    with right:
        listing_html = """
        <div class="hp-card">
            <img class="hp-listing-img" src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg"
                 alt="Home photo" />

            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
                <div>
                    <div class="hp-price">$579,900</div>
                    <div class="hp-line">4 bd | 3 ba | 2,580 sq ft</div>
                    <div class="hp-city">Downtown, Detroit, MI</div>
                </div>
                <div>
                    <button class="hp-pill-btn">Constrain</button>
                </div>
            </div>

            <div class="hp-listing-metrics-row">
                <div>
                    <div class="hp-listing-metric-label">HomePath score</div>
                    <div class="hp-listing-metric-value">88</div>
                </div>
                <div>
                    <div class="hp-listing-metric-label">Est. value</div>
                    <div class="hp-listing-metric-value">$340,000</div>
                </div>
                <div>
                    <div class="hp-listing-metric-label">5-yr growth</div>
                    <div class="hp-listing-metric-value hp-listing-metric-green">+5.2%</div>
                </div>
            </div>
        </div>
        """
        st.markdown(listing_html, unsafe_allow_html=True)


# -------------------------------------------------------------
# OTHER PAGES - SIMPLE PLACEHOLDERS
# -------------------------------------------------------------
def render_first_time_buyer():
    st.subheader("First-time buyer friendly 🧭")
    st.write("This page will show AI resources, beginner tips, and affordability tools.")


def render_investor_analysis():
    st.subheader("Investor deal analysis 💼")
    st.write("This page will show cap rates, cash-on-cash, and flip / BRRRR style analysis.")


def render_neighbor_insights():
    st.subheader("Neighbor insights 🏘️")
    st.write("This page will show crime, schools, walkability, and lifestyle scores.")


def render_repair_estimator():
    st.subheader("Repair estimator 🔧")
    st.write("Upload photos or enter repair items for AI-powered cost estimates.")


def render_rent_and_moving():
    st.subheader("Rent & moving tools 🚚")
    st.write("Compare rents vs buying, moving timelines, and relocation helpers.")


# -------------------------------------------------------------
# ROUTER
# -------------------------------------------------------------
render_header_and_nav()
page = st.session_state["active_page"]

if page == "Home dashboard":
    render_home_dashboard()
elif page == "First-time buyer friendly":
    render_first_time_buyer()
elif page == "Investor deal analysis":
    render_investor_analysis()
elif page == "Neighbor insights":
    render_neighbor_insights()
elif page == "Repair estimator":
    render_repair_estimator()
elif page == "Rent & moving tools":
    render_rent_and_moving()













