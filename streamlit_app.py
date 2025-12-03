import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="HomePathAI Demo",
    layout="wide",
)

PRIMARY_TEAL = "#00A3A6"
DARK_TEAL = "#008b93"
LIGHT_BG = "#F5FAFC"

# ---------------- GLOBAL STYLES ----------------
st.markdown(
    f"""
    <style>
        .main {{
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
            color:#6b7280;
        }}

        .hp-nav-row {{
            margin:10px 0 16px 0;
        }}

        /* Make the top buttons look like pills */
        .stButton > button {{
            background:#E0F4F5;
            color:#084C61;
            border-radius:999px;
            border:none;
            padding:8px 18px;
            font-size:13px;
            font-weight:500;
        }}

        .hp-card {{
            background:white;
            padding:20px;
            border-radius:16px;
            box-shadow:0 8px 24px rgba(15,23,42,0.08);
        }}

        .hp-metric-card {{
            background:white;
            padding:18px;
            border-radius:14px;
            box-shadow:0 8px 24px rgba(15,23,42,0.06);
            text-align:center;
        }}

        .hp-metric-label {{
            font-size:14px;
            color:#4b5563;
            margin-bottom:6px;
        }}

        .hp-metric-value {{
            font-size:28px;
            font-weight:700;
            color:#111827;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- NAV PAGES ----------------
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


# ---------------- HEADER + NAV ----------------
def render_header_and_nav():
    col_logo, _ = st.columns([1, 3])
    with col_logo:
        st.markdown(
            """
            <div class="hp-header-logo">
                <div style="width:34px;height:34px;border-radius:10px;background:#0A9BAA;
                            display:flex;align-items:center;justify-content:center;
                            color:white;font-weight:700;font-size:18px;">
                    AI
                </div>
                <div>
                    <div style="font-size:22px;font-weight:700;color:#064663;">HomePathAI</div>
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


# ---------------- HOME DASHBOARD ----------------
def render_home_dashboard():
    # Hero card
    st.markdown(
        """
        <div class="hp-card" style="margin-top:10px;
             background:linear-gradient(135deg,#0086b3,#00aeca,#14c5d9);color:white;">
            <h1 style="font-size:36px;font-weight:700;margin:0 0 6px 0;">
                Smart search for your next home — powered by AI.
            </h1>
            <p style="opacity:0.95;font-size:18px;margin:0 0 18px 0;">
                Neighborhood insights, investor-grade numbers, repair tools, moving resources,
                and first-time buyer help — all in one experience built for real people.
            </p>

            <div style="margin-top:18px;display:flex;gap:10px;">
                <input placeholder="Search city, neighborhood, or ZIP"
                       style="flex:1;padding:14px;border-radius:10px;
                              border:1px solid #e5e7eb;font-size:15px;" />
                <button style="padding:14px 26px;border-radius:10px;border:none;
                               background:#00A3A6;color:white;font-size:15px;font-weight:600;">
                    Search
                </button>
            </div>

            <div style="margin-top:10px;font-size:12px;opacity:0.9;">
                Your AI-powered home search companion for smarter buying.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.markdown("### 🔥 Trending homes near you")
    st.write("Sample homes across Detroit and nearby areas — demo data only.")

    left, right = st.columns([1.2, 1])

    # Heatmap section
    with left:
        st.subheader("Neighborhood snapshot")
        st.caption("Safety, price, and walkability at a glance — demo map.")

        df = pd.DataFrame(
            {
                "lat": np.random.uniform(42.28, 42.42, 250),
                "lon": np.random.uniform(-83.25, -82.95, 250),
                "value": np.random.uniform(0, 1, 250),
            }
        )

        layer = pdk.Layer(
            "HeatmapLayer",
            data=df,
            get_position="[lon, lat]",
            get_weight="value",
            radius_pixels=40,
            opacity=0.9,
        )

        deck = pdk.Deck(
            layers=[layer],
            initial_view_state=pdk.ViewState(
                latitude=42.35,
                longitude=-83.05,
                zoom=9,
                pitch=40,
            ),
            tooltip={"text": "Demo hot spot"},
        )

        st.pydeck_chart(deck)

    # Listing card
    with right:
        st.markdown(
            """
            <div class="hp-card">
                <img src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=1200"
                     style="width:100%;border-radius:16px;margin-bottom:15px;">

                <div style="font-size:22px;font-weight:700;">$579,900</div>
                <div style="color:#6b7280;margin-bottom:6px;">4 bd | 3 ba | 2,580 sq ft</div>
                <div style="color:#0A9BAA;margin-bottom:16px;">Downtown, Detroit, MI</div>

                <div style="display:flex;justify-content:space-between;margin-bottom:12px;">
                    <div>
                        <div style="text-transform:uppercase;font-size:11px;color:#6b7280;">
                            HomePathAI score
                        </div>
                        <div style="font-size:20px;font-weight:700;">88</div>
                    </div>
                    <div>
                        <div style="text-transform:uppercase;font-size:11px;color:#6b7280;">
                            Est. value
                        </div>
                        <div style="font-size:20px;font-weight:700;">$340,000</div>
                    </div>
                    <div>
                        <div style="text-transform:uppercase;font-size:11px;color:#6b7280;">
                            5-yr growth
                        </div>
                        <div style="font-size:20px;font-weight:700;color:#059669;">+5.2%</div>
                    </div>
                </div>

                <button style="width:100%;padding:13px;border-radius:10px;border:none;
                               background:#0A9BAA;color:white;font-size:15px;font-weight:600;">
                    Constrain this deal
                </button>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.caption(
        "This is a non-functional visual demo for HomePathAI — colors, layout, map, "
        "and cards match the investor concept."
    )


# ---------------- HUB PAGES ----------------
def render_first_time_buyer():
    st.markdown("## First-time buyer friendly 👋")
    st.write("AI resources & beginner-friendly tips")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class="hp-card">
                <h4>First-time buyer basics</h4>
                <p style="color:#4b5563;font-size:13px;">
                    Buying your first home? Start here.
                </p>
                <ul style="color:#4b5563;font-size:13px;">
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
            <div class="hp-card">
                <h4>Step-by-step guides</h4>
                <p style="color:#4b5563;font-size:13px;">
                    Understand each phase of buying.
                </p>
                <ol style="color:#4b5563;font-size:13px;">
                    <li>Get pre-approved</li>
                    <li>Tour homes</li>
                    <li>Make offers</li>
                    <li>Close smoothly</li>
                </ol>
            </div>
            """,
            unsafe_allow_html=True,
        )

    col3, col4 = st.columns(2)
    with col3:
        st.markdown(
            """
            <div class="hp-card">
                <h4>Affordability calculator</h4>
                <p style="color:#4b5563;font-size:13px;">
                    See what you can comfortably afford based on income and debts.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col4:
        st.markdown(
            """
            <div class="hp-card">
                <h4>Mortgage pre-approval</h4>
                <p style="color:#4b5563;font-size:13px;">
                    Compare lenders and rates side-by-side.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.markdown(
        """
        <div style="margin-top:20px;text-align:center;">
            <div style="font-weight:600;margin-bottom:8px;">Have questions?</div>
            <button style="padding:12px 22px;border-radius:999px;border:none;
                           background:#0A9BAA;color:white;font-weight:600;">
                Ask our AI assistant
            </button>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_investor_analysis():
    st.markdown("## Investor deal analysis")
    st.write("Quick compare cities before you invest or move.")

    _ = st.selectbox("Select a city", ["Detroit, MI", "Grand Rapids, MI", "Pittsburgh, PA"])
    st.write("")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class="hp-metric-card">
              <div class="hp-metric-label">Cost of living</div>
              <div class="hp-metric-value">8%</div>
              <div style="font-size:13px;color:#6b7280;">above average</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="hp-metric-card">
              <div class="hp-metric-label">Crime rate</div>
              <div class="hp-metric-value">High</div>
              <div style="font-size:13px;color:#6b7280;">vs national average</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class="hp-metric-card">
              <div class="hp-metric-label">Schools</div>
              <div class="hp-metric-value">6.4</div>
              <div style="font-size:13px;color:#6b7280;">average rating</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_neighbor_insights():
    st.markdown("## Neighborhood insights")
    st.write("Compare areas on safety, price, and walkability — demo numbers only.")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("#### Compare cities")
        _ = st.selectbox("City A", ["Detroit, MI", "Grand Rapids, MI", "Ann Arbor, MI"])
        _ = st.selectbox("City B", ["Cleveland, OH", "Columbus, OH", "Chicago, IL"])

        data = pd.DataFrame(
            {
                "Metric": ["Median price", "5-yr growth", "Crime", "Schools"],
                "City A": ["$240k", "+4.8%", "High", "6.2"],
                "City B": ["$310k", "+5.6%", "Medium", "7.1"],
            }
        )
        st.table(data)
    with col2:
        st.markdown(
            """
            <div class="hp-card">
              <h4 style="margin-top:0;">Snapshot</h4>
              <p style="color:#4b5563;font-size:13px;">
                Simple side-by-side view of two metros with AI notes on risk &amp; upside.
              </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_repair_estimator():
    st.markdown("## Repair estimator")
    st.write("Rough repair budget based on similar homes (demo numbers).")

    col1, col2 = st.columns([2, 1])
    with col1:
        _ = st.text_input("Address", "123 Main St, Detroit, MI")
        _ = st.number_input("Total square footage", value=1800, step=50)
    with col2:
        st.markdown("Estimated repair budget")
        st.markdown("### $51,800")
        st.caption("Based on similar homes in your area (demo only).")

    items = ["Roof", "HVAC", "Kitchen", "Bathrooms", "Interior paint", "Landscaping"]
    costs = [9500, 7800, 15000, 10500, 3500, 5500]
    df = pd.DataFrame({"Item": items, "Estimated cost ($)": costs})
    st.write("#### Repair cost breakdown (demo)")
    st.dataframe(df, use_container_width=True)


def render_rent_and_moving():
    st.markdown("## Rent & moving tools")
    st.write("Browse rentals and budget your move (demo only).")

    st.markdown("#### Rent listings")
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    with col1:
        _ = st.text_input("City or ZIP", "Detroit, MI")
    with col2:
        _ = st.number_input("Max rent", value=1800, step=50)
    with col3:
        _ = st.selectbox("Beds", ["Any", "1+", "2+", "3+"])
    with col4:
        _ = st.selectbox("Baths", ["Any", "1+", "2+"])

    st.write("")

    listings = pd.DataFrame(
        {
            "Address": ["123 Elm St", "456 Maple Rd", "322 Oak Ave"],
            "City": ["Detroit, MI", "Dearborn, MI", "Ferndale, MI"],
            "Beds": [2, 3, 1],
            "Baths": [1, 2, 1],
            "Rent ($/mo)": [1650, 1850, 1450],
        }
    )
    st.dataframe(listings, use_container_width=True)

    st.write("")
    st.markdown(
        """
        <div class="hp-card" style="margin-top:16px;">
          <h4 style="margin-top:0;">Rent budget helper</h4>
          <p style="color:#4b5563;font-size:13px;">
            High-level view of a few sample rentals vs your max budget —
            real app would pull from live feeds.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------- RENDER PAGE ----------------
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












