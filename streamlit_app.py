import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(
    page_title="HomePathAI Demo",
    layout="wide"
)

# Brand colors
PRIMARY_TEAL = "#00A3A6"
DARK_TEAL = "#00839B"
LIGHT_BG = "#F5FAFC"

# ------------------------------------------------------
# GLOBAL STYLES
# ------------------------------------------------------
st.markdown(
    f"""
    <style>
        main {{
            background-color: {LIGHT_BG};
        }}

        .hp-header-logo {{
            display:flex;
            align-items:center;
            gap:12px;
            margin-bottom:4px;
        }}

        .hp-tagline {{
            font-size:12px;
            color:#6B7280;
        }}

        .hp-nav-row {{
            margin: 10px 0 16px 0;
        }}

        /* Make the top buttons look like pills */
        .stButton > button {{
            background:#E0F4F5;
            color:#0B4C61;
            border-radius:999px;
            border:none;
            padding:8px 18px;
            font-size:13px;
            font-weight:500;
        }}

        .stButton > button:hover {{
            background:#C8E9EE;
        }}

        /* Active pill look (we'll use inline styles too) */
        .hp-active-pill > button {{
            background:{PRIMARY_TEAL} !important;
            color:white !important;
        }}

        .hp-card {{
            background:white;
            border-radius:16px;
            padding:20px;
            box-shadow:0 8px 24px rgba(15,23,42,0.08);
        }}

        .hp-metric-card {{
            background:white;
            border-radius:14px;
            padding:18px;
            box-shadow:0 8px 24px rgba(15,23,42,0.06);
            text-align:center;
        }}

        .hp-metric-label {{
            font-size:14px;
            color:#4B5563;
            margin-bottom:6px;
        }}

        .hp-metric-value {{
            font-size:20px;
            font-weight:700;
            color:#111827;
        }}

        .hp-section-title {{
            font-size:20px;
            font-weight:700;
            margin-bottom:4px;
        }}

        .hp-section-subtitle {{
            font-size:12px;
            color:#6B7280;
            margin-bottom:12px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------
# NAV PAGES
# ------------------------------------------------------
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


# ------------------------------------------------------
# HEADER + NAV
# ------------------------------------------------------
def render_header_and_nav():
    col_logo, col_nav = st.columns([1, 3])

    with col_logo:
        st.markdown(
            f"""
            <div class="hp-header-logo">
                <div style="
                    width:34px;
                    height:34px;
                    border-radius:10px;
                    background:{PRIMARY_TEAL};
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    color:white;
                    font-weight:700;
                    font-size:18px;">
                    AI
                </div>
                <div>
                    <div style="font-size:20px;font-weight:700;">HomePathAI</div>
                    <div class="hp-tagline">
                        Neighborhood &amp; home insight assistant
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_nav:
        st.markdown('<div class="hp-nav-row">', unsafe_allow_html=True)
        nav_cols = st.columns(len(PAGES))
        for idx, page in enumerate(PAGES):
            col = nav_cols[idx]

            # Add a CSS class to highlight active pill
            if page == st.session_state["active_page"]:
                with col:
                    st.markdown(
                        "<div class='hp-active-pill'>",
                        unsafe_allow_html=True,
                    )
                    if st.button(page, key=f"nav_{page}"):
                        st.session_state["active_page"] = page
                    st.markdown("</div>", unsafe_allow_html=True)
            else:
                with col:
                    if st.button(page, key=f"nav_{page}"):
                        st.session_state["active_page"] = page
        st.markdown("</div>", unsafe_allow_html=True)


# ------------------------------------------------------
# HOME DASHBOARD (hero + heatmap + listing card)
# ------------------------------------------------------
# -----------------------------------------------------------
# HOME DASHBOARD (Hero + Heatmap + Listing Card)
# -----------------------------------------------------------


def render_home_dashboard():

    # -------------- HERO SECTION --------------

    # Phase 1 - Listing Card Placeholder
    st.subheader("Phase 1 - Listing Card (Placeholder)")
    st.markdown(
        """
        <div style="
            background:white;
            padding:20px;
            border-radius:16px;
            box-shadow:0 4px 10px rgba(0,0,0,0.08);
        ">
            <p style="font-size:15px; color:#687280;">
                Phase 1 placeholder — Listing card AI will generate here.
                This space will later show:
            </p>

            <ul style="color:#687280; font-size:14px;">
                <li>AI-generated property scores</li>
                <li>AI-estimated repair/upgrade costs</li>
                <li>AI-estimated ARV (after repair value)</li>
                <li>Neighborhood insight metrics</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
   

    # ---------------- SECTION TITLE ----------------
    st.markdown("### 🔥 Trending homes near you")
    st.write("Sample homes across Detroit and nearby areas — demo data only.")
    st.write("")

    # ---------------- HEATMAP ----------------
    left, right = st.columns([1.2, 1])

    with left:
        st.subheader("Neighborhood snapshot")
        st.caption("Safety, price, and walkability at a glance — demo map.")

        df = pd.DataFrame({
            "lat": np.random.uniform(42.28, 42.42, 250),
            "lon": np.random.uniform(-83.5, -83.0, 250),
            "value": np.random.uniform(0, 1, 250)
        })

        layer = pdk.Layer(
            "HeatmapLayer",
            df,
            get_position='[lon, lat]',
            opacity=0.9,
            threshold=0.2
        )

        deck = pdk.Deck(
            layers=[layer],
            initial_view_state=pdk.ViewState(
                latitude=42.33,
                longitude=-83.1,
                zoom=9,
                pitch=40
            )
        )

        st.pydeck_chart(deck)

    # ---------------- LISTING CARD ----------------
    with right:
        st.subheader("Phase 1 · Listing Card (Placeholder)")
    st.markdown(
        """
        <div style="
            background:white;
            padding:20px;
            border-radius:16px;
            box-shadow:0 4px 10px rgba(0,0,0,0.08);
            ">
            <p style="font-size:15px; color:#687280;">
                Phase 1 placeholder — Listing card AI will generate here.
                This space will later show:
            </p>
            <ul style="color:#687280; font-size:14px;">
                <li>AI-generated property scores</li>
                <li>AI-estimated repair/upgrade costs</li>
                <li>AI-estimated ARV (after repair value)</li>
                <li>Neighborhood insight metrics</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
      
     
    st.caption("This is a visual demo for HomePathAI — colors, map, layout, and card match the investor concept.")

# ------------------------------------------------------
def render_first_time_buyer():
    st.markdown(
        """
        <h2>First-time buyer friendly 👋</h2>
        <p class="hp-section-subtitle">
            AI resources &amp; beginner-friendly tips.
        </p>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="hp-card">
                <h4>📘 First-time buyer basics</h4>
                <p style="font-size:13px; color:#4B5563;">
                    Buying your first home? Start here – curated checklists and explainers.
                </p>
                <ul style="font-size:13px; color:#4B5563; padding-left:18px;">
                    <li>What you can really afford</li>
                    <li>Down payment options</li>
                    <li>Closing costs explained in plain language</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="hp-card" style="margin-top:14px;">
                <h4>🧮 Affordability calculator</h4>
                <p style="font-size:13px; color:#4B5563;">
                    See what you can comfortably afford – not just what the bank approves.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="hp-card">
                <h4>📝 Step-by-step guides</h4>
                <p style="font-size:13px; color:#4B5563;">
                    Understand each phase of buying:
                </p>
                <ol style="font-size:13px; color:#4B5563; padding-left:20px;">
                    <li>Get pre-approved</li>
                    <li>Tour homes &amp; compare</li>
                    <li>Make offers with confidence</li>
                    <li>Close smoothly</li>
                </ol>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="hp-card" style="margin-top:14px;">
                <h4>🏦 Mortgage pre-approval</h4>
                <p style="font-size:13px; color:#4B5563;">
                    Demo-only CTA that could link to lender partners or an in-house flow.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.markdown(
        """
        <div style="margin-top:22px; text-align:center;">
            <div style="font-weight:600; margin-bottom:8px;">Have questions?</div>
            <button style="
                padding:10px 24px;
                border-radius:999px;
                border:none;
                background:#007E8A;
                color:white;
                font-weight:600;
                cursor:pointer;
            ">
                Ask our AI assistant
            </button>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ------------------------------------------------------
# INVESTOR ANALYSIS PAGE
# ------------------------------------------------------
def render_investor_analysis():
    st.markdown(
        """
        <h2>Investor deal analysis 📊</h2>
        <p class="hp-section-subtitle">
            Quick cash-flow &amp; equity snapshots for small-to-mid sized investors (demo).
        </p>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            """
            <div class="hp-card">
                <h4>Deal at a glance</h4>
                <p style="font-size:13px; color:#4B5563;">
                    Plug in rent, price, and expenses to see whether a deal pencils out.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")
        price = st.number_input("Purchase price ($)", value=220000, step=5000)
        rent = st.number_input("Monthly rent ($)", value=1900, step=50)
        taxes = st.number_input("Monthly taxes + insurance ($)", value=350, step=25)
        repairs = st.number_input("Maintenance / reserves ($)", value=175, step=25)

        noi = rent - taxes - repairs
        cap_rate = (noi * 12 / price) * 100 if price else 0
        cash_on_cash = cap_rate * 1.3  # playful demo assumption

        st.write("")
        st.markdown("#### Quick metrics (demo logic only)")
        st.write(f"**Estimated monthly NOI:** ${noi:,.0f}")
        st.write(f"**Cap rate (rough):** {cap_rate:0.1f}%")
        st.write(f"**Cash-on-cash proxy:** {cash_on_cash:0.1f}%")

    with col2:
        st.markdown(
            """
            <div class="hp-metric-card">
                <div class="hp-metric-label">Target cap rate</div>
                <div class="hp-metric-value">7–10%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="hp-metric-card" style="margin-top:14px;">
                <div class="hp-metric-label">Hold period (yrs)</div>
                <div class="hp-metric-value">3–7</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ------------------------------------------------------
# NEIGHBOR INSIGHTS PAGE
# ------------------------------------------------------
def render_neighbor_insights():
    st.markdown(
        """
        <h2>Neighbor insights 🧭</h2>
        <p class="hp-section-subtitle">
            Compare cities or neighborhoods before you move or invest (demo layout).
        </p>
        """,
        unsafe_allow_html=True,
    )

    col_top1, col_top2, col_top3 = st.columns([2, 2, 1])

    with col_top1:
        st.selectbox("Select a city", ["Detroit, MI", "Grand Rapids, MI", "Pittsburgh, PA"])

    with col_top2:
        st.selectbox(
            "Compare to",
            ["Pittsburgh, PA", "Cleveland, OH", "Indianapolis, IN"],
        )

    with col_top3:
        st.button("Compare")

    st.write("")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="hp-metric-card">
                <div class="hp-metric-label">Cost of living</div>
                <div class="hp-metric-value">8% above avg</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="hp-metric-card">
                <div class="hp-metric-label">Crime rate</div>
                <div class="hp-metric-value">High</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="hp-metric-card">
                <div class="hp-metric-label">Schools</div>
                <div class="hp-metric-value">6.4 rating</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ------------------------------------------------------
# REPAIR ESTIMATOR PAGE
# ------------------------------------------------------
def render_repair_estimator():
    st.markdown(
        """
        <h2>Repair estimator 🛠</h2>
        <p class="hp-section-subtitle">
            Rough repair budget based on similar homes (demo numbers only).
        </p>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        address = st.text_input("Address", "123 Main St, Detroit, MI")
        sqft = st.number_input("Total square footage", value=1800, step=50)

        st.write("")
        st.markdown("#### Estimated repair budget (demo)")
        base_cost = 51800
        st.write(f"**${base_cost:,.0f}** based on similar homes in your area (demo only).")

        items = ["Roof", "HVAC", "Kitchen", "Bathrooms", "Interior paint", "Landscaping"]
        costs = [9500, 7800, 15000, 8500, 3500, 5500]
        df = pd.DataFrame({"Item": items, "Estimated cost ($)": costs})
        st.write("")
        st.write("**Repair cost breakdown (demo)**")
        st.dataframe(df, use_container_width=True)

    with col2:
        st.markdown(
            """
            <div class="hp-card">
                <h4>Next step ideas</h4>
                <ul style="font-size:13px; color:#4B5563; padding-left:18px;">
                    <li>Upload photos for smarter estimates</li>
                    <li>Compare quotes from local contractors</li>
                    <li>Link to funding options for heavy rehabs</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ------------------------------------------------------
# RENT & MOVING PAGE
# ------------------------------------------------------
def render_rent_and_moving():
    st.markdown(
        """
        <h2>Rent &amp; moving tools 🚚</h2>
        <p class="hp-section-subtitle">
            Browse rentals and budget your move (demo only).
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### 🏘 Rent listings (demo)")
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

    with col1:
        st.text_input("City or ZIP", "Detroit, MI")
    with col2:
        st.number_input("Max rent", value=1800, step=50)
    with col3:
        st.selectbox("Beds", ["Any", "1+", "2+", "3+"])
    with col4:
        st.selectbox("Baths", ["Any", "1+", "2+"])

    listings = pd.DataFrame(
        {
            "Address": ["123 Elm St", "456 Maple Rd", "322 Oak Ave"],
            "City": ["Detroit, MI", "Dearborn, MI", "Ferndale, MI"],
            "Beds": [2, 3, 1],
            "Baths": [1, 2, 1],
            "Rent ($/mo)": [1600, 1850, 1450],
        }
    )
    st.dataframe(listings, use_container_width=True)

    st.write("")
    st.markdown(
        """
        <div class="hp-card" style="margin-top:16px;">
            <h4 style="margin-top:0;">Rent budget helper</h4>
            <p style="color:#4B5563;font-size:13px;">
                High-level view of a few sample rentals vs your max budget –
                real app would pull from live feeds.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ------------------------------------------------------
# RENDER PAGE ROUTER
# ------------------------------------------------------
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














