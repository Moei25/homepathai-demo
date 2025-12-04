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
# GLOBAL STYLES (match your screenshot)
# -------------------------------------------------------------
st.markdown(
    """
    <style>
        body {
            background-color: #f3f7fb;
        }

        .main > div {
            padding-top: 0rem;
        }

        /* App background */
        .stApp {
            background-color: #f3f7fb;
            font-family: -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
        }

        /* Header row */
        .hp-header-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 18px;
        }

        .hp-logo-wrap {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .hp-logo-icon {
            width: 40px;
            height: 40px;
            border-radius: 12px;
            background: #007c91;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 700;
            font-size: 20px;
        }

        .hp-logo-text-main {
            font-size: 24px;
            font-weight: 700;
            color: #024047;
        }

        .hp-logo-text-sub {
            font-size: 12px;
            color: #5f7b84;
        }

        /* Top nav pills */
        .hp-nav-row {
            display: flex;
            gap: 10px;
        }

        .hp-pill {
            background: #0a95a5;
            color: #ffffff;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 2px 4px rgba(0,0,0,0.16);
            white-space: nowrap;
        }

        .hp-pill-active {
            background: #046879;
        }

        /* Hero banner */
        .hp-hero {
            margin-top: 12px;
            background: #0086b3;
            color: white;
            border-radius: 16px;
            padding: 22px 26px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.18);
        }

        .hp-hero-title {
            font-size: 26px;
            font-weight: 700;
            margin: 0 0 4px 0;
        }

        .hp-hero-sub {
            font-size: 14px;
            opacity: 0.95;
            margin: 0 0 18px 0;
        }

        .hp-hero-row {
            display: flex;
            gap: 10px;
            margin-bottom: 10px;
        }

        .hp-hero-input {
            flex: 1;
            padding: 14px;
            border-radius: 10px;
            border: 1px solid #e5e7eb;
            font-size: 15px;
        }

        .hp-hero-btn {
            padding: 14px 26px;
            border-radius: 10px;
            border: none;
            background: #004f6e;
            color: white;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
        }

        .hp-hero-helper {
            font-size: 12px;
            opacity: 0.88;
        }

        /* Section title */
        .hp-section-title {
            font-size: 18px;
            font-weight: 700;
            margin-top: 22px;
            margin-bottom: 2px;
            color: #12333c;
        }

        .hp-section-sub {
            font-size: 12px;
            color: #8c8f97;
            margin-bottom: 10px;
        }

        /* Listing card */
        .hp-card {
            background: white;
            border-radius: 16px;
            padding: 18px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.10);
        }

        .hp-listing-image {
            width: 100%;
            border-radius: 14px;
            margin-bottom: 10px;
        }

        .hp-listing-top-row {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 6px;
        }

        .hp-price {
            font-size: 20px;
            font-weight: 700;
            color: #002f3e;
        }

        .hp-line {
            font-size: 13px;
            color: #687280;
        }

        .hp-city {
            font-size: 13px;
            color: #0a95a5;
            margin-top: 4px;
        }

        .hp-pill-btn {
            background: #0a95a5;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 999px;
            font-size: 13px;
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
            color: #84919b;
        }

        .hp-listing-metric-value {
            font-size: 14px;
            font-weight: 700;
            color: #002f3e;
        }

        .hp-listing-metric-green {
            color: #0a9a6a;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------------------
# NAV STATE
# -------------------------------------------------------------
if "active_page" not in st.session_state:
    st.session_state["active_page"] = "Home dashboard"


# -------------------------------------------------------------
# HEADER + NAV
# -------------------------------------------------------------
def render_header_and_nav():
    header_html = """
    <div class="hp-header-row">
        <div class="hp-logo-wrap">
            <div class="hp-logo-icon">AI</div>
            <div>
                <div class="hp-logo-text-main">HomePathAI</div>
                <div class="hp-logo-text-sub">
                    Neighborhood &amp; home insight assistant
                </div>
            </div>
        </div>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

    pages = [
        "Home dashboard",
        "First-time buyer friendly",
        "Investor deal analysis",
        "Neighbor insights",
        "Repair estimator",
        "Rent & moving tools",
    ]

    nav_cols = st.columns(len(pages))
    for i, label in enumerate(pages):
        is_active = (st.session_state["active_page"] == label)
        btn_class = "hp-pill hp-pill-active" if is_active else "hp-pill"

        html = f'<button class="{btn_class}">{label}</button>'

        # Transparent Streamlit button that we ignore visually
        if nav_cols[i].button(" ", key=f"nav_{label}"):
            st.session_state["active_page"] = label

        # Draw our styled pill under the invisible button
        nav_cols[i].markdown(html, unsafe_allow_html=True)


# -------------------------------------------------------------
# HOME DASHBOARD – MATCHES YOUR SCREENSHOT LAYOUT
# -------------------------------------------------------------
def render_home_dashboard():
    # HERO
    hero_html = """
    <div class="hp-hero">
        <div class="hp-hero-title">
            Smart search for your next home — powered by AI.
        </div>
        <div class="hp-hero-sub">
            Neighborhood insights, investor-grade numbers, repair tools, moving resources,
            and first-time buyer help — all in one experience built for real people.
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

    # SECTION TITLE
    st.markdown('<div class="hp-section-title">🔥 Trending homes near you</div>',
                unsafe_allow_html=True)
    st.markdown(
        '<div class="hp-section-sub">Sample homes across Detroit and nearby areas — demo data only.</div>',
        unsafe_allow_html=True,
    )

    # HEATMAP + LISTING CARD
    left, right = st.columns([1.2, 1])

    # --- LEFT: map ---
    with left:
        st.markdown(
            '<div class="hp-section-title" style="font-size:16px;">Neighborhood snapshot</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="hp-section-sub" style="margin-bottom:8px;">Safety, price, and walkability at a glance — demo map.</div>',
            unsafe_allow_html=True,
        )

        df = pd.DataFrame({
            "lat": np.random.uniform(42.28, 42.42, 250),
            "lon": np.random.uniform(-83.5, -83.0, 250),
            "value": np.random.uniform(0, 1, 250),
        })

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

    # --- RIGHT: listing card ---
    with right:
        st.markdown(
            '<div class="hp-section-title" style="font-size:16px;">Phase 1 - Listing Card (Placeholder)</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="hp-section-sub" style="margin-bottom:8px;">This area shows the AI-scored property card (demo values).</div>',
            unsafe_allow_html=True,
        )

        listing_html = """
        <div class="hp-card">
            <img class="hp-listing-image"
                 src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg"
                 alt="House" />

            <div class="hp-listing-top-row">
                <div>
                    <div class="hp-price">$579,900</div>
                    <div class="hp-line">4 bd | 3 ba | 2,580 sq ft</div>
                    <div class="hp-city">Downtown, Detroit, MI</div>
                </div>
                <button class="hp-pill-btn">Constrain</button>
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
# OTHER PAGES – SIMPLE PLACEHOLDERS FOR NOW
# -------------------------------------------------------------
def render_first_time_buyer():
    st.subheader("First-time buyer friendly 🧭")
    st.write("AI resources & beginner-friendly tips will live here.")

def render_investor_analysis():
    st.subheader("Investor deal analysis 💼")
    st.write("This page will show cap rates, cash-on-cash, and flip / BRRRR style analysis.")

def render_neighbor_insights():
    st.subheader("Neighbor insights 🏘️")
    st.write("Local area crime, schools, walkability, and lifestyle fit scoring coming soon.")

def render_repair_estimator():
    st.subheader("Repair estimator 🔧")
    st.write("Upload photos + AI-estimated repair costs will be here.")

def render_rent_and_moving():
    st.subheader("Rent & moving tools 🚚")
    st.write("Rent vs buy, moving calculators, and relocation helpers will be here.")


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












