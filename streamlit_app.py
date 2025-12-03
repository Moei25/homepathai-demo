import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# ------------------------#
#  BASIC CONFIG
# ------------------------#
st.set_page_config(
    page_title="HomePathAI Demo",
    page_icon="🏠",
    layout="wide",
)

# Brand colors (approx from your mockups)
PRIMARY_TEAL = "#00A3A5"
PRIMARY_DARK = "#003E52"
LIGHT_BG = "#F5FBFD"


# ------------------------#
#  GLOBAL STYLES
# ------------------------#
st.markdown(
    f"""
    <style>
        body {{
            background-color: {LIGHT_BG};
        }}

        .hp-topbar {{
            display:flex;
            align-items:center;
            justify-content:space-between;
            padding:18px 32px 4px 32px;
        }}
        .hp-logo {{
            display:flex;
            align-items:center;
            gap:10px;
        }}
        .hp-logo-icon {{
            width:38px;
            height:38px;
            border-radius:10px;
            background: {PRIMARY_TEAL};
            display:flex;
            align-items:center;
            justify-content:center;
            color:white;
            font-weight:800;
            font-size:20px;
            box-shadow:0 4px 10px rgba(0,0,0,0.15);
        }}
        .hp-logo-text-main {{
            font-size:26px;
            font-weight:800;
            color:{PRIMARY_DARK};
        }}
        .hp-logo-text-sub {{
            font-size:11px;
            color:#4B6B7A;
            margin-top:-4px;
        }}

        /* Make the radio buttons look like pills */
        div[role="radiogroup"] > label {{
            border-radius:999px;
            padding:6px 18px;
            border:1px solid #d0e4ea;
            background-color:#E3F3F6;
            color:{PRIMARY_DARK};
            font-size:13px;
            font-weight:600;
            margin-right:6px;
        }}
        div[role="radiogroup"] > label[data-checked="true"] {{
            background-color:{PRIMARY_TEAL} !important;
            color:white !important;
            border-color:{PRIMARY_TEAL} !important;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------#
#  TOP BAR + NAV
# ------------------------#
top_l, top_r = st.columns([2, 3])
with top_l:
    st.markdown(
        """
        <div class="hp-topbar">
          <div class="hp-logo">
            <div class="hp-logo-icon">AI</div>
            <div>
              <div class="hp-logo-text-main">HomePathAI</div>
              <div class="hp-logo-text-sub">Neighborhood &amp; home insight assistant</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with top_r:
    st.write("")  # spacing on the right

TABS = [
    "First-time buyer friendly",
    "Investor deal analysis",
    "Neighbor insights",
    "Repair estimator",
    "Rent & moving tools",
]

active_tab = st.radio(
    "Navigation",
    TABS,
    horizontal=True,
    label_visibility="collapsed",
    key="active_tab",
)


# ------------------------#
#  SECTIONS
# ------------------------#
def first_time_buyer_section():
    st.markdown("## First-time buyer friendly 👋")
    st.caption("AI resources & beginner-friendly tips")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            ### 🧠 First-time buyer basics  
            Buying your first home? Start here.

            • What you can really afford  
            • Down payment options  
            • Closing costs explained  
            """,
        )
        st.markdown(
            """
            ### 🧮 Affordability calculator  
            See what you can comfortably afford.
            """,
        )

    with col2:
        st.markdown(
            """
            ### 📋 Step-by-step guides  
            Understand each phase of buying:

            1. Get pre-approved  
            2. Tour homes  
            3. Make offers  
            4. Close smoothly  
            """,
        )
        st.markdown(
            """
            ### 🧾 Mortgage pre-approval  
            Get pre-approved for better rates.
            """,
        )

    st.divider()
    st.markdown("#### Have questions?")
    st.button("Ask our AI assistant")


def investor_section():
    st.markdown("## Investor deal analysis")
    st.caption("Quick numbers for flips & long-term holds (demo only)")

    cols = st.columns(3)
    with cols[0]:
        st.metric("Target ROI", "18%", "+3.2% vs market")
    with cols[1]:
        st.metric("Cash-on-cash", "11.5%", "Demo")
    with cols[2]:
        st.metric("Vacancy risk", "Low", "Demo")

    st.write("")
    st.subheader("Sample deal breakdown (demo numbers)")

    df = pd.DataFrame(
        {
            "Item": ["Purchase price", "Renovation budget", "Holding costs", "Projected ARV"],
            "Amount ($)": [210_000, 55_000, 12_000, 320_000],
        }
    )
    st.table(df)


def neighbor_insights_section():
    st.markdown("## Neighbor insights")
    st.caption("Understand cost of living, crime, and schools before you move (demo)")

    top, map_row = st.container(), st.container()

    with top:
        col1, col2 = st.columns([2, 3])
        with col1:
            city = st.selectbox("Select a city", ["Detroit, MI", "Grand Rapids, MI", "Ann Arbor, MI"])
            compare_to = st.selectbox("Compare to", ["Pittsburgh, PA", "Chicago, IL", "Columbus, OH"])
            st.write(f"Comparing **{city}** vs **{compare_to}** (demo only).")

        with col2:
            metrics = pd.DataFrame(
                {
                    "Metric": ["Cost of living", "Crime rate", "School rating"],
                    "Value": ["8% above avg", "High", "6.4 / 10"],
                }
            )
            st.table(metrics)

    with map_row:
        st.subheader("Neighborhood snapshot (demo heatmap)")
        st.caption("Safety, price, and walkability at a glance – demo map only.")

        # Fake lat/lon points roughly around Detroit for demo
        df = pd.DataFrame(
            {
                "lat": np.random.uniform(42.28, 42.45, 250),
                "lon": np.random.uniform(-83.3, -82.9, 250),
                "value": np.random.uniform(0, 1, 250),
            }
        )

        layer = pdk.Layer(
            "HeatmapLayer",
            data=df,
            get_position="[lon, lat]",
            get_weight="value",
            radius_pixels=40,
        )

        view_state = pdk.ViewState(
            latitude=42.35,
            longitude=-83.05,
            zoom=9,
            pitch=0,
        )

        deck = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "Demo hotspot"})
        st.pydeck_chart(deck)


def repair_estimator_section():
    st.markdown("## Repair estimator")
    st.caption("Rough repair budget based on similar homes (demo numbers)")

    col1, col2 = st.columns([2, 3])
    with col1:
        st.text_input("Address", "123 Main St, Detroit, MI")
        st.number_input("Square footage", 600, 5000, 1800, step=50)

    with col2:
        st.metric("Estimated repair budget", "$51,800")
        st.write("Based on similar homes in your area (demo only).")

    st.write("")
    st.subheader("Repair cost breakdown (demo)")
    df = pd.DataFrame(
        {
            "Item": ["Roof", "HVAC", "Kitchen", "Bathrooms", "Interior paint", "Landscaping"],
            "Estimated cost ($)": [9_500, 7_800, 15_000, 10_500, 3_500, 5_500],
        }
    )
    st.table(df)


def rent_moving_section():
    st.markdown("## Rent & moving tools")
    st.caption("Plan rentals, budgets, and moving day (demo)")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Rent listings (demo)")
        st.text_input("City or ZIP", "Detroit, MI")
        st.number_input("Target rent ($/mo)", 400, 5000, 1800, step=50)
        st.selectbox("Beds", ["Any", "1+", "2+", "3+"])
        st.selectbox("Baths", ["Any", "1+", "2+"])
        st.button("Search rentals (demo)")

    with col2:
        st.markdown("### Rent budget helper")
        listings = pd.DataFrame(
            {
                "Address": ["Studio – Downtown", "3bd – Dearborn", "2bd – Ferndale"],
                "Rent ($/mo)": [1600, 1750, 1500],
                "Beds": [1, 3, 2],
            }
        )
        st.table(listings)


# ------------------------#
#  ROUTE TO SECTION
# ------------------------#
if active_tab == "First-time buyer friendly":
    first_time_buyer_section()
elif active_tab == "Investor deal analysis":
    investor_section()
elif active_tab == "Neighbor insights":
    neighbor_insights_section()
elif active_tab == "Repair estimator":
    repair_estimator_section()
else:
    rent_moving_section()












