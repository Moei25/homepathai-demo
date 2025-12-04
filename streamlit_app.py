import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from streamlit.components.v1 import html

# -----------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------
st.set_page_config(page_title="HomePathAI", layout="wide")

# -----------------------------------------------------------
# GLOBAL CSS — EXACT COLORS FROM SCREENSHOT
# -----------------------------------------------------------
st.markdown("""
<style>

body {
    background-color: #F2F6F7;
}

/* NAV BUTTONS */
.hp-nav-btn {
    background: #0B7682;
    padding: 14px 26px;
    border-radius: 10px;
    color: white;
    font-weight: 600;
    border: none;
    cursor: pointer;
    font-size: 16px;
}

/* ACTIVE NAV */
.hp-active {
    background: #094E56 !important;
}

/* HERO BAR */
.hp-hero {
    background: #0C7682;
    color: white;
    padding: 32px;
    border-radius: 14px;
    margin-top: 10px;
}

/* HERO INPUT */
.hp-hero-input {
    width: 70%;
    padding: 14px;
    border-radius: 10px;
    border: none;
    font-size: 16px;
}

/* HERO BUTTON */
.hp-hero-btn {
    padding: 14px 26px;
    background:#07525A;
    border-radius: 10px;
    border: none;
    color:white;
    font-weight:700;
    cursor:pointer;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# NAVIGATION BAR
# -----------------------------------------------------------
pages = [
    "Home dashboard",
    "First-time buyer friendly",
    "Investor deal analysis",
    "Neighbor insights",
    "Repair estimator",
    "Rent & moving tools"
]

if "active" not in st.session_state:
    st.session_state.active = "Home dashboard"

cols = st.columns(len(pages))
for i, p in enumerate(pages):
    active_class = "hp-active" if st.session_state.active == p else ""
    if cols[i].button(f"{p}", key=p):
        st.session_state.active = p
    cols[i].markdown(
        f"<style>#{p} {{ background:#0B7682; color:white; border-radius:10px; padding:12px; }} #{p}:hover {{ background:#0A606D }}</style>",
        unsafe_allow_html=True,
    )

# -----------------------------------------------------------
# HOME DASHBOARD — REAL SCREENSHOT LAYOUT
# -----------------------------------------------------------
def page_home():

    # HERO SECTION
    st.markdown("""
    <div class="hp-hero">

        <h2>Smart search for your next home — powered by AI.</h2>
        <p>Neighborhood insights, investor-grade numbers, repair tools,
           and first-time buyer help — all in one place.</p>

        <div style="display:flex; gap:12px; margin-top:16px;">
            <input class="hp-hero-input" placeholder="Search city, neighborhood, or ZIP" />
            <button class="hp-hero-btn">Search</button>
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔥 Trending homes near you")
    st.caption("Sample homes across Detroit — demo data only.")

    # MAP + LISTING CARD
    left, right = st.columns([1.3, 1])

    # ------------------------------
    # LEFT: HEATMAP (WORKS)
    # ------------------------------
    with left:
        st.markdown("#### Neighborhood snapshot")
        df = pd.DataFrame({
            "lat": np.random.uniform(42.28, 42.42, 200),
            "lon": np.random.uniform(-83.5, -83.0, 200),
            "value": np.random.uniform(0, 1, 200)
        })

        layer = pdk.Layer(
            "HeatmapLayer",
            df,
            get_position='[lon, lat]',
            threshold=0.2,
            opacity=0.9
        )

        deck = pdk.Deck(
            layers=[layer],
            initial_view_state=pdk.ViewState(
                latitude=42.33,
                longitude=-83.1,
                zoom=9,
                pitch=40,
            )
        )

        st.pydeck_chart(deck)

    # ------------------------------
    # RIGHT: LISTING CARD (TRUE HTML)
    # ------------------------------
    with right:
        html("""
        <div style="
            background:white;
            border-radius:16px;
            padding:18px;
            box-shadow:0 4px 12px rgba(0,0,0,0.10);
        ">

            <img src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg"
                 style="width:100%; border-radius:14px; margin-bottom:12px;" />

            <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                <div>
                    <div style="font-size:22px; font-weight:700;">$579,900</div>
                    <div>4 bd | 3 ba | 2,580 sq ft</div>
                    <div>Downtown, Detroit, MI</div>
                </div>

                <button style="
                    padding:10px 16px;
                    background:#0C7682;
                    border:none;
                    border-radius:8px;
                    color:white;
                    font-weight:600;
                ">Constrain</button>
            </div>

            <div style="display:flex; justify-content:space-between; margin-top:14px;">
                <div>
                    <div style="color:#8890A0;">HomePath score</div>
                    <div style="font-weight:700;">88</div>
                </div>
                <div>
                    <div style="color:#8890A0;">Est. value</div>
                    <div style="font-weight:700;">$340,000</div>
                </div>
                <div>
                    <div style="color:#8890A0;">5-yr growth</div>
                    <div style="font-weight:700; color:#0BB94A;">+5.2%</div>
                </div>
            </div>

        </div>
        """, height=600)

# -----------------------------------------------------------
# PAGE ROUTER
# -----------------------------------------------------------
if st.session_state.active == "Home dashboard":
    page_home()
else:
    st.title(st.session_state.active)
    st.write("Page coming soon.")















