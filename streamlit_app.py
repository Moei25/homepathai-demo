import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# -----------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------
st.set_page_config(page_title="HomePathAI", layout="wide")

# -----------------------------------------------------------
# GLOBAL CSS  (colors & layout close to your screenshot)
# -----------------------------------------------------------
st.markdown(
    """
    <style>
    :root {
        --hp-bg: #F2F6F7;
        --hp-teal: #0C7682;
        --hp-teal-dark: #0A5D66;
        --hp-tag: #0A9456;
        --hp-gray: #8890A4;
        --hp-card-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }

    body {
        background-color: var(--hp-bg);
    }
    .stApp {
        background-color: var(--hp-bg);
    }

    /* TOP NAV BUTTONS (all st.button at top) */
    .top-nav .stButton>button {
        background: var(--hp-teal);
        color: white;
        padding: 12px 22px;
        border-radius: 10px;
        border: none;
        font-weight: 600;
        margin-right: 8px;
        cursor: pointer;
    }
    .top-nav .stButton>button:hover {
        background: var(--hp-teal-dark);
    }

    /* HERO BAR */
    .hp-hero {
        background: var(--hp-teal);
        color: white;
        padding: 32px;
        border-radius: 14px;
        margin-top: 10px;
        box-shadow: var(--hp-card-shadow);
    }
    .hp-hero h2 {
        margin: 0 0 6px 0;
    }
    .hp-hero p {
        margin: 0;
        opacity: 0.95;
    }

    .hp-hero-input {
        width: 70%;
        padding: 14px;
        border-radius: 10px;
        border: none;
        font-size: 16px;
    }
    .hp-hero-btn {
        padding: 14px 26px;
        background: #07525A;
        border-radius: 10px;
        border: none;
        color: white;
        font-weight: 700;
        cursor: pointer;
    }

    /* GENERIC CARD */
    .hp-card {
        background: white;
        border-radius: 16px;
        padding: 20px;
        box-shadow: var(--hp-card-shadow);
        margin-bottom: 20px;
    }

    .hp-label {
        color: var(--hp-gray);
        font-size: 14px;
    }
    .hp-value {
        font-weight: 700;
        font-size: 16px;
    }
    .hp-green {
        color: #0B9D4A;
    }

    .hp-tag {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 999px;
        background: rgba(10,148,86,0.1);
        color: var(--hp-tag);
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }

    .hp-section-title {
        margin-top: 24px;
        margin-bottom: 4px;
        font-size: 20px;
        font-weight: 700;
    }
    .hp-section-sub {
        margin: 0 0 12px 0;
        color: var(--hp-gray);
        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------
# NAV BAR
# -----------------------------------------------------------
pages = [
    "Home dashboard",
    "First-time buyer friendly",
    "Investor deal analysis",
    "Neighbor insights",
    "Repair estimator",
    "Rent & moving tools",
]

if "active" not in st.session_state:
    st.session_state["active"] = "Home dashboard"


def render_nav():
    st.markdown("### HomePathAI")
    st.caption("Neighborhood & home insight assistant")

    st.markdown('<div class="top-nav">', unsafe_allow_html=True)
    cols = st.columns(len(pages))
    for i, p in enumerate(pages):
        if cols[i].button(p, key=f"nav-{p}"):
            st.session_state["active"] = p
    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------------------------------
# HOME DASHBOARD (matches screenshot layout)
# -----------------------------------------------------------
def page_home():
    # HERO SECTION
    st.markdown(
        """
        <div class="hp-hero">

            <h2>Smart search for your next home — powered by AI.</h2>
            <p>
                Neighborhood insights, investor-grade numbers, repair tools,
                and first-time buyer help — all in one place.
            </p>

            <div style="display:flex; gap:12px; margin-top:18px;">
                <input class="hp-hero-input" type="text"
                    placeholder="Search city, neighborhood, or ZIP" />
                <button class="hp-hero-btn">Search</button>
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # SECTION TITLE
    st.markdown('<p class="hp-section-title">🔥 Trending homes near you</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="hp-section-sub">Sample homes across Detroit — demo data only.</p>',
        unsafe_allow_html=True,
    )

    # MAP + LISTING
    left, right = st.columns([1.3, 1])

    # ------ LEFT: HEATMAP ------
    with left:
        st.markdown('<p class="hp-section-title">Neighborhood snapshot</p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="hp-section-sub">Safety, price, and walkability at a glance — demo map.</p>',
            unsafe_allow_html=True,
        )

        df = pd.DataFrame(
            {
                "lat": np.random.uniform(42.28, 42.42, 220),
                "lon": np.random.uniform(-83.5, -83.0, 220),
                "value": np.random.uniform(0, 1, 220),
            }
        )

        layer = pdk.Layer(
            "HeatmapLayer",
            df,
            get_position="[lon, lat]",
            threshold=0.2,
            opacity=0.8,
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

    # ------ RIGHT: LISTING CARD ------
    with right:
        st.markdown(
            """
            <div class="hp-card">

                <img src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg"
                     style="width:100%; border-radius:12px; margin-bottom:14px;" />

                <div style="display:flex; justify-content:space-between; margin-bottom:10px; align-items:flex-start;">
                    <div>
                        <div style="font-size:22px; font-weight:700;">$579,900</div>
                        <div class="hp-label">4 bd | 3 ba | 2,580 sq ft</div>
                        <div class="hp-label">Downtown, Detroit, MI</div>
                    </div>
                    <button class="hp-hero-btn" style="padding:10px 18px; font-size:14px;">
                        Constrain this deal
                    </button>
                </div>

                <div style="display:flex; justify-content:space-between; margin-top:12px;">
                    <div>
                        <div class="hp-label">HomePath score</div>
                        <div class="hp-value">88</div>
                    </div>
                    <div>
                        <div class="hp-label">Est. value</div>
                        <div class="hp-value">$340,000</div>
                    </div>
                    <div>
                        <div class="hp-label">5-yr growth</div>
                        <div class="hp-value hp-green">+5.2%</div>
                    </div>
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# -----------------------------------------------------------
# FIRST-TIME BUYER PAGE
# -----------------------------------------------------------
def page_first_time():
    st.markdown('<p class="hp-section-title">🧭 First-time buyer friendly</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="hp-section-sub">AI-powered guidance so new buyers do not feel lost.</p>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="hp-card">
                <span class="hp-tag">Buyer journey</span>
                <h3>Step-by-step path to your first home</h3>
                <p class="hp-section-sub">
                    Clear stages from saving for a down payment to closing day.
                    Each step can be turned into tasks with reminders.
                </p>
                <ul>
                    <li>🧾 Affordability check and budget setup</li>
                    <li>🏦 Lender pre-approval and rate shopping</li>
                    <li>🏡 Touring homes with AI deal summaries</li>
                    <li>🖊️ Offer, inspection, and closing checklist</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="hp-card">
                <span class="hp-tag">AI tools</span>
                <h3>What HomePathAI will do for first-time buyers</h3>
                <ul>
                    <li>
                        <b>Payment coach:</b> translate listing price into
                        monthly payment with taxes and insurance.
                    </li>
                    <li>
                        <b>Risk radar:</b> flags high taxes, weak schools, or
                        unusual crime trends in the area.
                    </li>
                    <li>
                        <b>Comparison view:</b> line up up to three homes
                        side by side with scores for safety, schools,
                        commute, and long term value.
                    </li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )


# -----------------------------------------------------------
# INVESTOR DEAL ANALYSIS PAGE
# -----------------------------------------------------------
def page_investor():
    st.markdown('<p class="hp-section-title">💼 Investor deal analysis</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="hp-section-sub">Cap rates, cash-on-cash, and BRRRR-style metrics at a glance.</p>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown(
            """
            <div class="hp-card">
                <span class="hp-tag">Sample deal</span>
                <h3>Detroit duplex — demo numbers</h3>
                <table>
                    <tr><td class="hp-label">Purchase price</td><td class="hp-value">$210,000</td></tr>
                    <tr><td class="hp-label">Renovation budget</td><td class="hp-value">$40,000</td></tr>
                    <tr><td class="hp-label">Total all-in</td><td class="hp-value">$250,000</td></tr>
                    <tr><td class="hp-label">Projected rent</td><td class="hp-value">$2,800 / month</td></tr>
                    <tr><td class="hp-label">Cap rate (stabilized)</td><td class="hp-value hp-green">8.7%</td></tr>
                </table>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="hp-card">
                <span class="hp-tag">Planned features</span>
                <h3>How investors will use HomePathAI</h3>
                <ul>
                    <li>Run instant cap rate and cash-on-cash from a listing link.</li>
                    <li>Upload rehab numbers and let AI stress test the deal.</li>
                    <li>Compare multiple zip codes by rent growth and vacancy.</li>
                    <li>Export clean deal summaries to share with partners or lenders.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )


# -----------------------------------------------------------
# NEIGHBOR INSIGHTS PAGE
# -----------------------------------------------------------
def page_neighbor():
    st.markdown('<p class="hp-section-title">🏘️ Neighbor insights</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="hp-section-sub">Understand the block, not just the house.</p>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="hp-card">
                <span class="hp-tag">Quality of life</span>
                <h3>AI neighborhood snapshot</h3>
                <ul>
                    <li>Safety, school rating, and walkability score.</li>
                    <li>Commute time to downtown or major job centers.</li>
                    <li>Nearby grocery, parks, and health care.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="hp-card">
                <span class="hp-tag">Trends</span>
                <h3>Watch how an area is changing</h3>
                <ul>
                    <li>Price growth and days-on-market trend.</li>
                    <li>Rent trend for similar properties.</li>
                    <li>Renovation activity and permit volume.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )


# -----------------------------------------------------------
# REPAIR ESTIMATOR PAGE
# -----------------------------------------------------------
def page_repair():
    st.markdown('<p class="hp-section-title">🔧 Repair estimator</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="hp-section-sub">Phase 2 idea — fast rehab ranges from photos and checklists.</p>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="hp-card">
                <span class="hp-tag">Scope of work</span>
                <h3>Room-by-room estimator</h3>
                <ul>
                    <li>Kitchen, baths, roof, HVAC, electrical, and more.</li>
                    <li>Choose light, medium, or heavy update level.</li>
                    <li>Costs auto-adjust to local labor and material ranges.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="hp-card">
                <span class="hp-tag">Planned AI</span>
                <h3>Upload photos → get budget bands</h3>
                <ul>
                    <li>Vision model flags dated finishes and big-ticket items.</li>
                    <li>Generates best-case, likely, and high-risk scenarios.</li>
                    <li>Exports into the investor deal analysis page.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )


# -----------------------------------------------------------
# RENT & MOVING TOOLS PAGE
# -----------------------------------------------------------
def page_rent():
    st.markdown('<p class="hp-section-title">🚚 Rent & moving tools</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="hp-section-sub">Help renters decide where to land next and what it will really cost.</p>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="hp-card">
                <span class="hp-tag">Rent map</span>
                <h3>Compare rent across neighborhoods</h3>
                <ul>
                    <li>Heatmap of typical rents by bedroom count.</li>
                    <li>Filter by commute, school rating, and lifestyle.</li>
                    <li>See how far your budget goes in each zip code.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="hp-card">
                <span class="hp-tag">Moving helper</span>
                <h3>From lease end to settled in</h3>
                <ul>
                    <li>Timeline for notice, packing, movers, and utilities.</li>
                    <li>Compare buying vs renting timeline side by side.</li>
                    <li>Estimated total move cost with deposits and fees.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )


# -----------------------------------------------------------
# ROUTER
# -----------------------------------------------------------
render_nav()
current = st.session_state["active"]

if current == "Home dashboard":
    page_home()
elif current == "First-time buyer friendly":
    page_first_time()
elif current == "Investor deal analysis":
    page_investor()
elif current == "Neighbor insights":
    page_neighbor()
elif current == "Repair estimator":
    page_repair()
elif current == "Rent & moving tools":
    page_rent()















