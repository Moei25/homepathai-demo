# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="HomePathAI Demo",
    layout="wide"
)

# ------------------------------------------------
# THEME COLORS (Option B)
# ------------------------------------------------
PRIMARY = "#00688B"    # deep blue / teal
DARK = "#00485F"
ACCENT = "#00A3A6"
LIGHT_BG = "#F0F6FA"
CARD_BG = "#FFFFFF"

# ------------------------------------------------
# GLOBAL STYLES
# ------------------------------------------------
st.markdown(
    f"""
<style>
    html, body, [class^="css"]  {{
        font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    main {{
        background-color: {LIGHT_BG};
    }}

    .hp-header-logo {{
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 4px;
    }}

    .hp-logo-box {{
        width: 34px;
        height: 34px;
        border-radius: 10px;
        background: {PRIMARY};
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 700;
        font-size: 18px;
    }}

    .hp-title {{
        font-size: 22px;
        font-weight: 700;
        color: {DARK};
    }}

    .hp-tagline {{
        font-size: 13px;
        color: #6B7280;
    }}

    .hp-nav-row {{
        margin: 12px 0 22px 0;
    }}

    /* Make the Streamlit buttons look like pills */
    .stButton > button {{
        background: #E0F4FF;
        color: {DARK};
        border-radius: 999px;
        border: none;
        padding: 8px 18px;
        font-size: 13px;
        font-weight: 500;
        box-shadow: none;
    }}

    .stButton > button:hover {{
        background: #CBE8FF;
        color: {DARK};
    }}

    .hp-card {{
        background: {CARD_BG};
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
    }}

    .hp-card-simple {{
        background: {CARD_BG};
        padding: 16px 18px;
        border-radius: 14px;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
    }}

    .hp-metric-card {{
        background: {CARD_BG};
        padding: 18px;
        border-radius: 14px;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
        text-align: center;
    }}

    .hp-metric-label {{
        font-size: 14px;
        color: #4B5563;
        margin-bottom: 6px;
    }}

    .hp-metric-value {{
        font-size: 20px;
        font-weight: 700;
        color: #111827;
    }}

    .hp-section-title {{
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 4px;
        color: #111827;
    }}

    .hp-section-sub {{
        font-size: 13px;
        color: #6B7280;
        margin-bottom: 12px;
    }}

    .hp-pill {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 16px;
        font-weight: 600;
    }}

    .hp-icon-pill {{
        width: 34px;
        height: 34px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        margin-right: 10px;
    }}

    .hp-ai-button {{
        background: {PRIMARY};
        color: white;
        border-radius: 999px;
        padding: 10px 22px;
        border: none;
        font-size: 14px;
        font-weight: 600;
        cursor: pointer;
    }}

</style>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------
# NAV PAGES
# ------------------------------------------------
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

# ------------------------------------------------
# HEADER + NAV
# ------------------------------------------------
def render_header_and_nav():
    col_logo, col_empty = st.columns([1, 3])

    with col_logo:
        st.markdown(
            f"""
            <div class="hp-header-logo">
                <div class="hp-logo-box">AI</div>
                <div>
                    <div class="hp-title">HomePathAI</div>
                    <div class="hp-tagline">Neighborhood &amp; home insight assistant</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="hp-nav-row">', unsafe_allow_html=True)
    nav_cols = st.columns(len(PAGES))
    for idx, page in enumerate(PAGES):
        with nav_cols[idx]:
            if st.button(page, key=f"nav_{page}"):
                st.session_state["active_page"] = page
    st.markdown("</div>", unsafe_allow_html=True)


# ------------------------------------------------
# HOME DASHBOARD
# ------------------------------------------------
def render_home_dashboard():
    # Hero card with search + tagline
    st.markdown(
        f"""
        <div class="hp-card" style="margin-top:10px;">
            <h1 style="font-size:32px;font-weight:700;margin:0 0 8px 0;color:white;
                       padding:24px 24px 0 24px;
                       background: linear-gradient(135deg, {PRIMARY}, {ACCENT}); 
                       border-radius:12px 12px 0 0;">
                Smart search for your next home — powered by AI.
            </h1>

            <div style="padding:0 24px 24px 24px;
                        background: linear-gradient(135deg, {PRIMARY}, {ACCENT});
                        border-radius:0 0 12px 12px;color:white;">
                <p style="opacity:0.95;font-size:15px;margin-top:6px;">
                    Neighborhood insights, investor-grade numbers, repair tools, moving resources,
                    and first-time buyer help – all in one experience built for real people.
                </p>

                <div style="margin-top:18px;display:flex;gap:10px;">
                    <input placeholder="Search city, neighborhood, or ZIP"
                        style="flex:1;padding:14px;border-radius:10px;border:1px solid #e5e7eb;font-size:15px;" />
                    <button style="padding:14px 24px;border-radius:10px;border:none;
                                   background:#00B37A;color:white;font-size:15px;font-weight:600;">
                        Search
                    </button>
                </div>

                <div style="margin-top:10px;font-size:12px;opacity:0.9;">
                    Your AI-powered home search companion for smarter buying.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.markdown("### 🔥 Trending homes near you")
    st.write("Sample homes across Detroit and nearby areas — demo data only.")

    # Layout: heatmap + listing card
    left, right = st.columns([1.7, 1.3])

    # --- Heatmap (left) ---
    with left:
        st.subheader("Neighborhood snapshot")
        st.caption("Safety, price, and walkability at a glance – demo heatmap.")

        # Demo lat/lon around Detroit area
        df = pd.DataFrame(
            {
                "lat": np.random.uniform(42.28, 42.42, 250),
                "lon": np.random.uniform(-83.25, -82.9, 250),
                "value": np.random.uniform(0, 1, 250),
            }
        )

        layer = pdk.Layer(
            "HeatmapLayer",
            df,
            get_position=["lon", "lat"],
            get_weight="value",
            radius_pixels=40,
            opacity=0.9,
        )

        deck = pdk.Deck(
            layers=[layer],
            initial_view_state=pdk.ViewState(
                latitude=42.33,
                longitude=-83.1,
                zoom=9,
                pitch=40,
            ),
            map_style="mapbox://styles/mapbox/light-v9",
        )

        st.pydeck_chart(deck)

    # --- Listing card (right) ---
    with right:
        st.markdown(
            f"""
            <div class="hp-card" style="margin-top:22px;">
                <img src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg"
                     style="width:100%;border-radius:14px;margin-bottom:18px;" />

                <div style="font-size:22px;font-weight:700;">$579,900</div>
                <div style="color:#6B7280;font-size:13px;margin-top:2px;">
                    4 bd | 3 ba | 2,580 sq ft
                </div>
                <div style="color:{ACCENT};margin-top:8px;margin-bottom:18px;font-size:13px;">
                    Downtown, Detroit, MI
                </div>

                <div style="display:flex;justify-content:space-between;margin-bottom:10px;font-size:12px;">
                    <div>
                        <div class="hp-metric-label" style="text-transform:uppercase;color:#6B7280;">HomePathAI score</div>
                        <div class="hp-metric-value" style="color:{ACCENT};">88</div>
                    </div>
                    <div>
                        <div class="hp-metric-label" style="text-transform:uppercase;color:#6B7280;">Est. value</div>
                        <div class="hp-metric-value">$340,000</div>
                    </div>
                    <div>
                        <div class="hp-metric-label" style="text-transform:uppercase;color:#6B7280;">5-yr growth</div>
                        <div class="hp-metric-value" style="color:#059669;">+5.2%</div>
                    </div>
                </div>

                <button style="width:100%;padding:13px;border-radius:10px;
                               background:{PRIMARY};color:white;border:none;
                               font-size:14px;font-weight:600;cursor:pointer;">
                    Constrain this deal
                </button>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.caption(
        "This is a non-functional visual demo for HomePathAI – colors, layout, map, and card match the investor concept."
    )


# ------------------------------------------------
# FIRST-TIME BUYER PAGE
# ------------------------------------------------
def render_first_time_buyer():
    st.markdown(
        """
        <div class="hp-pill">
            <span class="hp-icon-pill" style="background:#FEE2E2;">🏡</span>
            <span style="font-size:22px;font-weight:700;">First-time buyer friendly 👋</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("AI resources & beginner-friendly tips")
    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="hp-card-simple">
                <div style="display:flex;align-items:center;gap:14px;">
                    <div class="hp-icon-pill" style="background:#DBEAFE;">📘</div>
                    <div>
                        <div style="font-weight:700;">First-time buyer basics</div>
                        <div style="font-size:13px;color:#6B7280;">
                            Buying your first home? Start here.
                        </div>
                    </div>
                </div>
                <ul style="font-size:13px;margin-top:10px;color:#4B5563;">
                    <li>What you can really afford</li>
                    <li>Down payment options</li>
                    <li>Closing costs explained</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="hp-card-simple">
                <div style="display:flex;align-items:center;gap:14px;">
                    <div class="hp-icon-pill" style="background:#FDE68A;">📋</div>
                    <div>
                        <div style="font-weight:700;">Step-by-step guides</div>
                        <div style="font-size:13px;color:#6B7280;">
                            Understand each phase of buying.
                        </div>
                    </div>
                </div>
                <ol style="font-size:13px;margin-top:10px;color:#4B5563;">
                    <li>Get pre-approved</li>
                    <li>Tour homes</li>
                    <li>Make offers</li>
                    <li>Close smoothly</li>
                </ol>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    col3, col4 = st.columns(2)

    with col3:
        st.markdown(
            """
            <div class="hp-card-simple">
                <div style="display:flex;align-items:center;gap:14px;">
                    <div class="hp-icon-pill" style="background:#DCFCE7;">🧮</div>
                    <div>
                        <div style="font-weight:700;">Affordability calculator</div>
                        <div style="font-size:13px;color:#6B7280;">
                            See what you can comfortably afford.
                        </div>
                    </div>
                </div>
                <p style="font-size:13px;margin-top:10px;color:#4B5563;">
                    Connect income, debts, and HOA dues to estimate a comfortable payment.
                    In a full build, this would tie into real mortgage rate APIs.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            """
            <div class="hp-card-simple">
                <div style="display:flex;align-items:center;gap:14px;">
                    <div class="hp-icon-pill" style="background:#E0F2FE;">📄</div>
                    <div>
                        <div style="font-weight:700;">Mortgage pre-approval</div>
                        <div style="font-size:13px;color:#6B7280;">
                            Get pre-approved for better rates.
                        </div>
                    </div>
                </div>
                <p style="font-size:13px;margin-top:10px;color:#4B5563;">
                    Demo-only CTA that would link to lender partners or an in-house mortgage flow.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.markdown(
        """
        <div style="text-align:center;margin-top:24px;">
            <p style="font-size:16px;font-weight:600;margin-bottom:10px;">Have questions?</p>
            <button class="hp-ai-button">Ask our AI assistant</button>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ------------------------------------------------
# INVESTOR DEAL ANALYSIS
# ------------------------------------------------
def render_investor_analysis():
    st.markdown(
        f"""
        <h2 class="hp-section-title">Compare cities for investing</h2>
        <p class="hp-section-sub">
            Understanding key differences before you invest or move – demo numbers only.
        </p>
        """,
        unsafe_allow_html=True,
    )

    col_city1, col_city2, col_button = st.columns([2, 2, 1])

    with col_city1:
        city_a = st.selectbox("Select city A", ["Detroit, MI", "Grand Rapids, MI", "Pittsburgh, PA"])

    with col_city2:
        city_b = st.selectbox("Select city B", ["Detroit, MI", "Grand Rapids, MI", "Pittsburgh, PA"], index=2)

    with col_button:
        st.write("")
        st.write("")
        st.button("Compare", use_container_width=True)

    st.write("")
    mc1, mc2, mc3 = st.columns(3)

    with mc1:
        st.markdown(
            """
            <div class="hp-metric-card">
                <div class="hp-metric-label">Cost of living</div>
                <div class="hp-metric-value">8% above average</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with mc2:
        st.markdown(
            """
            <div class="hp-metric-card">
                <div class="hp-metric-label">Crime rate</div>
                <div class="hp-metric-value">High</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with mc3:
        st.markdown(
            """
            <div class="hp-metric-card">
                <div class="hp-metric-label">Schools</div>
                <div class="hp-metric-value">6.4 rating</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.caption("Future build: plug in live crime, school, and rent yield data APIs to power this view.")


# ------------------------------------------------
# NEIGHBORHOOD INSIGHTS
# ------------------------------------------------
def render_neighbor_insights():
    st.markdown(
        """
        <h2 class="hp-section-title">Neighborhood insights</h2>
        <p class="hp-section-sub">
            Quick snapshot of safety, schools, and lifestyle — localized for your buyers.
        </p>
        """,
        unsafe_allow_html=True,
    )

    col_left, col_right = st.columns([1.4, 1.6])

    with col_left:
        city = st.selectbox("Neighborhood", ["Downtown Detroit", "Midtown", "Ferndale", "Royal Oak"])
        st.write("")
        st.markdown(
            """
            <div class="hp-card-simple">
                <p style="font-size:13px;color:#4B5563;">
                    Demo description of the area – walkability, nightlife, commute, and typical home styles.
                    In a real build, this would be AI-generated based on local data and user profile.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_right:
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Safety score", "78", "↑ 4 vs last year")
        with c2:
            st.metric("Median price", "$340k", "+5.1%")
        with c3:
            st.metric("Rent yield", "7.8%", "+0.3%")

    st.write("")
    st.caption("This page is a placeholder to show how local neighborhood scoring could look.")


# ------------------------------------------------
# REPAIR ESTIMATOR
# ------------------------------------------------
def render_repair_estimator():
    st.markdown(
        """
        <h2 class="hp-section-title">Repair estimator</h2>
        <p class="hp-section-sub">
            Rough repair budget based on similar homes (demo numbers only).
        </p>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        address = st.text_input("Address", "123 Main St, Detroit, MI")
        sqft = st.number_input("Total square footage", value=1800, step=50)

    with col2:
        st.markdown("**Estimated repair budget**")
        demo_budget = 51800
        st.markdown(f"<h1 style='margin:4px 0;'>{demo_budget:,.0f}</h1>", unsafe_allow_html=True)
        st.caption("Based on similar homes in your area (demo only).")

    items = ["Roof", "HVAC", "Kitchen", "Bathrooms", "Interior paint", "Landscaping"]
    costs = [9500, 7800, 15000, 10500, 3500, 5500]

    df = pd.DataFrame({"Item": items, "Estimated cost ($)": costs})
    st.write("#### Repair cost breakdown (demo)")
    st.dataframe(df, use_container_width=True)


# ------------------------------------------------
# RENT & MOVING TOOLS
# ------------------------------------------------
def render_rent_and_moving():
    st.markdown(
        """
        <h2 class="hp-section-title">Rent & moving tools</h2>
        <p class="hp-section-sub">
            Browse rentals and budget your move (demo only).
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Rent listings")
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

    with col1:
        city = st.text_input("City or ZIP", "Detroit, MI")

    with col2:
        max_rent = st.number_input("Max rent", value=1800, step=50)

    with col3:
        beds = st.selectbox("Beds", ["Any", "1+", "2+", "3+"])

    with col4:
        baths = st.selectbox("Baths", ["Any", "1+", "2+"])

    st.write("")
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
                High-level view of a few sample rentals vs your max budget – real app would pull from live feeds.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ------------------------------------------------
# RENDER PAGE
# ------------------------------------------------
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













