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
# GLOBAL STYLE
# -------------------------------------------------------------
st.markdown(
    """
    <style>
        body {
            background-color: #F5F5FA;
        }
        .hp-card {
            background: white;
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }
        .nav-btn {
            background: #E0F4FF;
            color: #004F6E;
            padding: 10px 18px;
            border-radius: 20px;
            border: none;
            margin-right: 8px;
            cursor: pointer;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------------------
# NAVIGATION
# -------------------------------------------------------------
if "active_page" not in st.session_state:
    st.session_state["active_page"] = "Home dashboard"

def render_header_and_nav():
    st.title("HomePathAI")
    st.caption("Neighborhood & home insight assistant")

    pages = [
        "Home dashboard",
        "First-time buyer friendly",
        "Investor deal analysis",
        "Neighbor insights",
        "Repair estimator",
        "Rent & moving tools",
    ]

    cols = st.columns(len(pages))
    for i, p in enumerate(pages):
        if cols[i].button(p):
            st.session_state["active_page"] = p

# -------------------------------------------------------------
# HOME DASHBOARD (Phase 1 placeholder)
# -------------------------------------------------------------
def render_home_dashboard():

    st.subheader("Phase 1 - Listing Card (Placeholder)")

    st.markdown(
        """
        <div class="hp-card">
            <p style="font-size:15px; color:#687280;">
                Phase 1 placeholder — Listing card AI will generate here.<br>
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

    # ----------- SECTION TITLE -----------
    st.markdown("### 🔥 Trending homes near you")
    st.write("Sample homes across Detroit and nearby areas — demo data only.")

    # ----------- HEATMAP -----------
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
                pitch=40,
            ),
        )

        st.pydeck_chart(deck)

    with right:
        st.subheader("Phase 1 - Listing Card (Placeholder)")
        st.write("This area will later show the AI-scored property card.")

# -------------------------------------------------------------
# OTHER PAGES (unchanged – placeholders)
# -------------------------------------------------------------
def render_first_time_buyer():
    st.subheader("First-time buyer friendly 🧭")
    st.write("AI resources & beginner tips.")

def render_investor_analysis():
    st.subheader("Investor deal analysis 💼")
    st.write("Deal analysis tools coming soon.")

def render_neighbor_insights():
    st.subheader("Neighbor insights 🏘️")
    st.write("Local area insight tools coming soon.")

def render_repair_estimator():
    st.subheader("Repair estimator 🔧")
    st.write("AI repair estimate tools coming soon.")

def render_rent_and_moving():
    st.subheader("Rent & moving tools 🚚")
    st.write("Relocation & renting tools coming soon.")

# -------------------------------------------------------------
# PAGE ROUTER
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














