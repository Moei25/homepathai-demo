import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# -----------------------------------------------------------
# BASIC CONFIG
# -----------------------------------------------------------
st.set_page_config(page_title="HomePathAI", layout="wide")

# -----------------------------------------------------------
# GLOBAL CSS – COLORS + STYLING TO MATCH YOUR SCREENSHOT
# -----------------------------------------------------------
st.markdown(
    """
<style>
:root {
    --hp-bg: #F2F6F7;
    --hp-teal: #0C7682;
    --hp-deep-teal: #07525A;
    --hp-pill: #0C7682;
    --hp-pill-text: #FFFFFF;
    --hp-gray-text: #687280;
}

/* Page background */
[data-testid="stAppViewContainer"] {
    background-color: var(--hp-bg);
}

/* Remove extra top padding */
.block-container {
    padding-top: 1.5rem;
}

/* Top nav buttons (the teal pills) */
.stButton > button {
    border-radius: 999px;
    border: none;
    padding: 8px 22px;
    background-color: var(--hp-pill);
    color: var(--hp-pill-text);
    font-weight: 600;
    font-size: 14px;
    cursor: pointer;
}

/* Slight hover brighten */
.stButton > button:hover {
    filter: brightness(1.05);
}

/* Hero bar */
.hp-hero {
    background: var(--hp-teal);
    color: white;
    padding: 32px;
    border-radius: 14px;
    margin-top: 18px;
}

/* Hero input row */
.hp-hero-row {
    display: flex;
    gap: 12px;
    margin-top: 16px;
}

/* Hero input */
.hp-hero-input {
    flex: 1;
    padding: 14px;
    border-radius: 10px;
    border: none;
    font-size: 15px;
}

/* Hero button */
.hp-hero-btn {
    padding: 14px 26px;
    background: var(--hp-deep-teal);
    border-radius: 10px;
    border: none;
    color: white;
    font-weight: 700;
    cursor: pointer;
}

/* Generic white card */
.hp-card {
    background: white;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

/* Listing card text helpers */
.hp-label {
    color: #8890A0;
    font-size: 14px;
}

.hp-value {
    font-weight: 700;
    font-size: 16px;
}

.hp-green {
    color: #0B9D4A;
}

/* Page section header subtitle */
.hp-section-subtitle {
    font-size: 13px;
    color: #8890A0;
    margin-top: -6px;
}

/* Simple tag label used on other pages */
.hp-tag {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 600;
    color: #0C7682;
    background: #D9F2F6;
    margin-bottom: 10px;
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------
# NAV BAR
# -----------------------------------------------------------
PAGES = [
    "Home dashboard",
    "First-time buyer friendly",
    "Investor deal analysis",
    "Neighbor insights",
    "Repair estimator",
    "Rent & moving tools",
]

if "active_page" not in st.session_state:
    st.session_state["active_page"] = "Home dashboard"

# Top title
st.title("HomePathAI")
st.caption("Neighborhood & home insight assistant")

# Nav pills
nav_cols = st.columns(len(PAGES))
for i, page_name in enumerate(PAGES):
    if nav_cols[i].button(page_name, use_container_width=True):
        st.session_state["active_page"] = page_name

st.write("")  # small spacer

# -----------------------------------------------------------
# HOME DASHBOARD PAGE
# -----------------------------------------------------------
def page_home_dashboard():
    # HERO SECTION
    hero_html = """
    <div class="hp-hero">
        <h2 style="margin:0;">Smart search for your next home — powered by AI.</h2>
        <p style="margin:6px 0 0 0; font-size:14px;">
            Neighborhood insights, investor-grade numbers, repair tools,
            moving resources, and first-time buyer help — all in one experience built for real people.
        </p>

        <div class="hp-hero-row">
            <input class="hp-hero-input" placeholder="Search city, neighborhood, or ZIP" type="text" />
            <button class="hp-hero-btn">Search</button>
        </div>

        <div style="margin-top:12px; font-size:12px; opacity:0.9;">
            Your AI-powered home search companion for smarter buying.
        </div>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)

    # SECTION TITLE
    st.markdown("### 🔥 Trending homes near you")
    st.markdown(
        '<div class="hp-section-subtitle">Sample homes across Detroit — demo data only.</div>',
        unsafe_allow_html=True,
    )

    # MAP + LISTING SIDE BY SIDE
    left, right = st.columns([1.3, 1])

    # ----- LEFT: HEATMAP -----
    with left:
        st.markdown("#### Neighborhood snapshot")
        st.markdown(
            '<div class="hp-section-subtitle">'
            "Safety, price, and walkability at a glance — demo map."
            "</div>",
            unsafe_allow_html=True,
        )

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
            get_position="[lon, lat]",
            threshold=0.2,
            opacity=0.9,
        )

        deck = pdk.Deck(
            layers=[layer],
            initial_view_state=pdk.ViewState(
                latitude=42.33, longitude=-83.1, zoom=9, pitch=40
            ),
        )

        st.pydeck_chart(deck)

    # ----- RIGHT: LISTING CARD -----
    with right:
        listing_html = """
        <div class="hp-card">
            <img src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg"
                 width="100%"
                 style="border-radius:12px; margin-bottom:12px;" />

            <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                <div>
                    <div style="font-size:22px; font-weight:700;">$579,900</div>
                    <div class="hp-label">4 bd | 3 ba | 2,580 sq ft</div>
                    <div class="hp-label">Downtown, Detroit, MI</div>
                </div>
                <button
                    style="
                        padding:10px 18px;
                        background:#0C7682;
                        color:white;
                        border:none;
                        border-radius:999px;
                        font-size:13px;
                        font-weight:600;
                        cursor:pointer;
                        margin-top:4px;
                    ">
                    Constrain this deal
                </button>
            </div>

            <div style="display:flex; justify-content:space-between; margin-top:16px;">
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
        """
        st.markdown(listing_html, unsafe_allow_html=True)


# -----------------------------------------------------------
# FIRST-TIME BUYER PAGE
# -----------------------------------------------------------
def page_first_time_buyer():
    st.markdown("### 🧭 First-time buyer friendly")
    st.markdown(
        '<div class="hp-section-subtitle">'
        "AI-powered guidance so new buyers do not feel lost."
        "</div>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        card = """
        <div class="hp-card">
            <div class="hp-tag">Buyer journey</div>
            <h4>Step-by-step path to your first home</h4>
            <p style="font-size:13px; color:var(--hp-gray-text);">
                Clear stages from saving for a down payment to closing day.
                Each step can be turned into tasks with reminders.
            </p>
            <ul style="font-size:13px; color:var(--hp-gray-text);">
                <li>Affordability check and budget setup</li>
                <li>Lender pre-approval and rate shopping</li>
                <li>Touring homes with AI deal summaries</li>
                <li>Offer, inspection, and closing checklist</li>
            </ul>
        </div>
        """
        st.markdown(card, unsafe_allow_html=True)

    with col2:
        card = """
        <div class="hp-card">
            <div class="hp-tag">AI tools</div>
            <h4>What HomePathAI will do for first-time buyers</h4>
            <ul style="font-size:13px; color:var(--hp-gray-text);">
                <li>Payment coach: translate listing price into monthly payment bands.</li>
                <li>Risk radar: flag high taxes, weak schools, or unusual crime trends.</li>
                <li>Comparison view: line up three homes side by side with scores.</li>
                <li>Co-buyer mode: share a link and vote on favorites together.</li>
            </ul>
        </div>
        """
        st.markdown(card, unsafe_allow_html=True)


# -----------------------------------------------------------
# INVESTOR DEAL ANALYSIS PAGE
# -----------------------------------------------------------
def page_investor_analysis():
    st.markdown("### 💼 Investor deal analysis")
    st.markdown(
        '<div class="hp-section-subtitle">'
        "Cap rates, cash-on-cash, and BRRRR-style analysis for small investors."
        "</div>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        card = """
        <div class="hp-card">
            <div class="hp-tag">Deal metrics</div>
            <h4>Quick glance pro forma</h4>
            <ul style="font-size:13px; color:var(--hp-gray-text);">
                <li>Cap rate, cash-on-cash, and DSCR estimates.</li>
                <li>Rent comps pulled from similar beds / baths nearby.</li>
                <li>Expense assumptions you can tweak (taxes, insurance, repairs).</li>
                <li>Exit scenarios: flip vs hold comparison.</li>
            </ul>
        </div>
        """
        st.markdown(card, unsafe_allow_html=True)

    with col2:
        card = """
        <div class="hp-card">
            <div class="hp-tag">Pipeline</div>
            <h4>Prioritize your next 5 deals</h4>
            <ul style="font-size:13px; color:var(--hp-gray-text);">
                <li>AI score based on yield, risk, and renovation complexity.</li>
                <li>Tag deals as wholesale, BRRRR, flip, or buy & hold.</li>
                <li>Export to spreadsheet or share with partners.</li>
            </ul>
        </div>
        """
        st.markdown(card, unsafe_allow_html=True)


# -----------------------------------------------------------
# NEIGHBOR INSIGHTS PAGE
# -----------------------------------------------------------
def page_neighbor_insights():
    st.markdown("### 🏘️ Neighbor insights")
    st.markdown(
        '<div class="hp-section-subtitle">'
        "Understand the block, not just the house."
        "</div>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        card = """
        <div class="hp-card">
            <div class="hp-tag">Quality of life</div>
            <h4>AI neighborhood snapshot</h4>
            <ul style="font-size:13px; color:var(--hp-gray-text);">
                <li>Safety, school rating, and walkability score.</li>
                <li>Commute time to downtown or major job centers.</li>
                <li>Nearby grocery, parks, and health care.</li>
            </ul>
        </div>
        """
        st.markdown(card, unsafe_allow_html=True)

    with col2:
        card = """
        <div class="hp-card">
            <div class="hp-tag">Trends</div>
            <h4>Watch how an area is changing</h4>
            <ul style="font-size:13px; color:var(--hp-gray-text);">
                <li>Price growth and days-on-market trend.</li>
                <li>Rent trend for similar properties.</li>
                <li>Renovation activity and permit volume.</li>
            </ul>
        </div>
        """
        st.markdown(card, unsafe_allow_html=True)


# -----------------------------------------------------------
# REPAIR ESTIMATOR PAGE
# -----------------------------------------------------------
def page_repair_estimator():
    st.markdown("### 🔧 Repair estimator")
    st.markdown(
        '<div class="hp-section-subtitle">'
        "Phase 2 idea — fast rehab ranges from photos and checklists."
        "</div>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        card = """
        <div class="hp-card">
            <div class="hp-tag">Scope of work</div>
            <h4>Room-by-room estimator</h4>
            <ul style="font-size:13px; color:var(--hp-gray-text);">
                <li>Kitchens, baths, roof, HVAC, electrical, and more.</li>
                <li>Choose light, medium, or heavy update level.</li>
                <li>Costs auto-adjust to local labor and material ranges.</li>
            </ul>
        </div>
        """
        st.markdown(card, unsafe_allow_html=True)

    with col2:
        card = """
        <div class="hp-card">
            <div class="hp-tag">Planned AI</div>
            <h4>Upload photos → get budget bands</h4>
            <ul style="font-size:13px; color:var(--hp-gray-text);">
                <li>Vision model flags dated finishes and big-ticket items.</li>
                <li>Generates best-case, likely, and high-risk scenarios.</li>
                <li>Exports into the investor deal analysis page.</li>
            </ul>
        </div>
        """
        st.markdown(card, unsafe_allow_html=True)


# -----------------------------------------------------------
# RENT & MOVING TOOLS PAGE
# -----------------------------------------------------------
def page_rent_and_moving():
    st.markdown("### 🚚 Rent & moving tools")
    st.markdown(
        '<div class="hp-section-subtitle">'
        "Help renters and relocators land in the right neighborhood."
        "</div>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        card = """
        <div class="hp-card">
            <div class="hp-tag">Rent band finder</div>
            <h4>See what “comfortable” rent looks like</h4>
            <ul style="font-size:13px; color:var(--hp-gray-text);">
                <li>Backs into rent ranges from take-home pay.</li>
                <li>Shows tradeoffs between location, size, and amenities.</li>
                <li>Highlights neighborhoods where you get more for your budget.</li>
            </ul>
        </div>
        """
        st.markdown(card, unsafe_allow_html=True)

    with col2:
        card = """
        <div class="hp-card">
            <div class="hp-tag">Moving toolkit</div>
            <h4>Relocation helper</h4>
            <ul style="font-size:13px; color:var(--hp-gray-text);">
                <li>Move checklist by week (60, 30, 7 days out).</li>
                <li>Track quotes from movers, cleaners, and storage.</li>
                <li>Neighborhood “vibe” summary based on your lifestyle profile.</li>
            </ul>
        </div>
        """
        st.markdown(card, unsafe_allow_html=True)


# -----------------------------------------------------------
# ROUTER – DECIDE WHICH PAGE TO SHOW
# -----------------------------------------------------------
active = st.session_state["active_page"]

if active == "Home dashboard":
    page_home_dashboard()
elif active == "First-time buyer friendly":
    page_first_time_buyer()
elif active == "Investor deal analysis":
    page_investor_analysis()
elif active == "Neighbor insights":
    page_neighbor_insights()
elif active == "Repair estimator":
    page_repair_estimator()
elif active == "Rent & moving tools":
    page_rent_and_moving()
















