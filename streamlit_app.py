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
    --hp-teal: #0C7680;
    --hp-deep-teal: #07525A;
    --hp-pill: #0C7680;
    --hp-pill-text: #FFFFFF;
    --hp-gray-text: #687280;
}

/* Page background */
[data-testid="stAppViewContainer"] {
    background-color: var(--hp-bg);
}

/* Top nav buttons */
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

/* Hero input + button */
.hp-hero-input {
    width: 70%;
    padding: 14px;
    border-radius: 10px;
    border: none;
    font-size: 16px;
}
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
    color: #0C7680;
    background: #E0F4F7;
    margin-bottom: 4px;
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------
# NAV STATE
# -----------------------------------------------------------
pages = [
    "Home dashboard",
    "First-time buyer friendly",
    "Investor deal analysis",
    "Neighbor insights",
    "Repair estimator",
    "Rent & moving tools",
]

if "page" not in st.session_state:
    st.session_state["page"] = "Home dashboard"

# -----------------------------------------------------------
# NAV BAR
# -----------------------------------------------------------
nav_cols = st.columns(len(pages))
for i, label in enumerate(pages):
    with nav_cols[i]:
        if st.button(label, key=f"nav-{label}"):
            st.session_state["page"] = label

st.write("")  # tiny spacer

# -----------------------------------------------------------
# PAGE: HOME DASHBOARD
# -----------------------------------------------------------
def page_home_dashboard():
    # HERO (this is where HTML was showing as text before)
    st.markdown(
        """
        <div class="hp-hero">
            <h2>Smart search for your next home — powered by AI.</h2>
            <p>
                Neighborhood insights, investor-grade numbers, repair tools,
                and first-time buyer help — all in one experience built for real people.
            </p>

            <div style="display:flex; gap:12px; margin-top:16px;">
                <input class="hp-hero-input" placeholder="Search city, neighborhood, or ZIP" type="text" />
                <button class="hp-hero-btn">Search</button>
            </div>

            <div style="margin-top:12px; font-size:12px; opacity:0.9;">
                Your AI-powered home search companion for smarter buying.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🔥 Trending homes near you")
    st.markdown(
        '<div class="hp-section-subtitle">Sample homes across Detroit — demo data only.</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.3, 1])

    # --- Map on the left ---
    with left:
        st.markdown("#### Neighborhood snapshot")
        st.markdown(
            '<div class="hp-section-subtitle">Safety, price, and walkability at a glance — demo map.</div>',
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
            opacity=0.85,
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

    # --- Listing card on the right ---
    with right:
        st.markdown(
            """
            <div class="hp-card">
                <img src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg"
                     style="width:100%; border-radius:12px; margin-bottom:12px;" />

                <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
                    <div>
                        <div style="font-size:22px; font-weight:700;">$579,900</div>
                        <div class="hp-label">4 bd | 3 ba | 2,580 sq ft</div>
                        <div class="hp-label">Downtown, Detroit, MI</div>
                    </div>
                    <div>
                        <button style="
                            padding:10px 18px;
                            background:#0C7680;
                            color:white;
                            border:none;
                            border-radius:999px;
                            font-size:13px;
                            font-weight:600;
                            cursor:pointer;
                        ">
                            Constrain this deal
                        </button>
                    </div>
                </div>

                <div style="display:flex; justify-content:space-between; margin-top:14px;">
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
# PAGE: FIRST-TIME BUYER
# -----------------------------------------------------------
def page_first_time_buyer():
    st.markdown("### 🧭 First-time buyer friendly")
    st.markdown(
        '<div class="hp-section-subtitle">AI-powered guidance so new buyers do not feel lost.</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns(2)

    with left:
        st.markdown(
            """
            <div class="hp-card">
                <div class="hp-tag">Buyer journey</div>
                <h4>Step-by-step path to your first home</h4>
                <p class="hp-section-subtitle">
                    Clear stages from saving for a down payment to closing day.
                    Each step can become tasks with reminders.
                </p>
                <ul>
                    <li>Affordability check and budget setup</li>
                    <li>Lender pre-approval and rate shopping</li>
                    <li>Touring homes with AI deal summaries</li>
                    <li>Offer, inspection, and closing checklist</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            """
            <div class="hp-card">
                <div class="hp-tag">AI tools</div>
                <h4>What HomePathAI will do for first-time buyers</h4>
                <ul>
                    <li>Payment coach: translate listing price into monthly payment bands.</li>
                    <li>Risk radar: flag high taxes, weak schools, or unusual crime trends.</li>
                    <li>Comparison view: line up three homes side by side with scores.</li>
                    <li>Co-buyer mode: share a link and vote on favorites together.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------------------------------------
# PAGE: INVESTOR DEAL ANALYSIS
# -----------------------------------------------------------
def page_investor_analysis():
    st.markdown("### 💼 Investor deal analysis")
    st.markdown(
        '<div class="hp-section-subtitle">Quick reads on cash flow, equity, and risk.</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns(2)

    with left:
        st.markdown(
            """
            <div class="hp-card">
                <div class="hp-tag">Deal snapshot</div>
                <h4>Cap rate & cash-on-cash at a glance</h4>
                <ul>
                    <li>Rent comps vs purchase price</li>
                    <li>Taxes, insurance, utilities, and maintenance baked in</li>
                    <li>Financing scenarios: cash, 20% down, or house-hack</li>
                    <li>Break-even vacancy and worst-case stress test</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            """
            <div class="hp-card">
                <div class="hp-tag">BRRRR / value-add</div>
                <h4>Flip & BRRRR-style analysis</h4>
                <ul>
                    <li>Repair budget bands from photos & checklists</li>
                    <li>After-repair value estimates using nearby solds</li>
                    <li>Timeline and carrying-cost calculator</li>
                    <li>Exit options: flip, refi-and-rent, or sell to another investor</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------------------------------------
# PAGE: NEIGHBOR INSIGHTS
# -----------------------------------------------------------
def page_neighbor_insights():
    st.markdown("### 🏘️ Neighbor insights")
    st.markdown(
        '<div class="hp-section-subtitle">Understand the block, not just the house.</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns(2)

    with left:
        st.markdown(
            """
            <div class="hp-card">
                <div class="hp-tag">Quality of life</div>
                <h4>AI neighborhood snapshot</h4>
                <ul>
                    <li>Safety, school rating, and walkability score</li>
                    <li>Commute time to downtown or major job centers</li>
                    <li>Nearby groceries, parks, and healthcare</li>
                    <li>Internet, cell coverage, and noise level signals</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            """
            <div class="hp-card">
                <div class="hp-tag">Trends</div>
                <h4>Watch how an area is changing</h4>
                <ul>
                    <li>Price growth and days-on-market trend</li>
                    <li>Rent trend for similar properties</li>
                    <li>Renovation activity and permit volume</li>
                    <li>New construction and zoning changes nearby</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------------------------------------
# PAGE: REPAIR ESTIMATOR
# -----------------------------------------------------------
def page_repair_estimator():
    st.markdown("### 🔧 Repair estimator")
    st.markdown(
        '<div class="hp-section-subtitle">Phase 2 idea — fast rehab ranges from photos and checklists.</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns(2)

    with left:
        st.markdown(
            """
            <div class="hp-card">
                <div class="hp-tag">Scope of work</div>
                <h4>Room-by-room estimator</h4>
                <ul>
                    <li>Kitchen, baths, roof, HVAC, electrical, and more</li>
                    <li>Choose light, medium, or heavy update level</li>
                    <li>Costs auto-adjust to local labor and material ranges</li>
                    <li>Exports into the investor deal analysis page</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            """
            <div class="hp-card">
                <div class="hp-tag">Planned AI</div>
                <h4>Upload photos → get budget bands</h4>
                <ul>
                    <li>Vision model flags dated finishes and big-ticket items</li>
                    <li>Generates best-case, likely, and high-risk scenarios</li>
                    <li>Highlights surprises: foundation, moisture, or roof issues</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------------------------------------
# PAGE: RENT & MOVING TOOLS
# -----------------------------------------------------------
def page_rent_and_moving():
    st.markdown("### 🚚 Rent & moving tools")
    st.markdown(
        '<div class="hp-section-subtitle">Help people compare renting vs buying and plan a move.</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns(2)

    with left:
        st.markdown(
            """
            <div class="hp-card">
                <div class="hp-tag">Rent vs buy</div>
                <h4>Compare rent vs owning over 3–7 years</h4>
                <ul>
                    <li>Down payment and closing costs vs up-front rent</li>
                    <li>Principal pay-down and equity build-up</li>
                    <li>Maintenance, taxes, and insurance included</li>
                    <li>Side-by-side chart for 2–3 scenarios</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            """
            <div class="hp-card">
                <div class="hp-tag">Move planning</div>
                <h4>Stress-less move checklist</h4>
                <ul>
                    <li>Timeline for utilities, mail, and address changes</li>
                    <li>Budget planner for movers, trucks, and supplies</li>
                    <li>“First night box” suggestions so you are not hunting for basics</li>
                    <li>Export checklist to your phone as simple tasks</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------------------------------------
# ROUTER
# -----------------------------------------------------------
page = st.session_state["page"]

if page == "Home dashboard":
    page_home_dashboard()
elif page == "First-time buyer friendly":
    page_first_time_buyer()
elif page == "Investor deal analysis":
    page_investor_analysis()
elif page == "Neighbor insights":
    page_neighbor_insights()
elif page == "Repair estimator":
    page_repair_estimator()
elif page == "Rent & moving tools":
    page_rent_and_moving()















