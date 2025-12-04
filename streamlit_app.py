import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(page_title="HomePathAI", layout="wide")

# -----------------------------------------------------------
# GLOBAL CSS
# -----------------------------------------------------------
st.markdown("""
<style>

body {
    background-color: #F5F8FA;
}

/* NAV BUTTONS */
.hp-nav-btn {
    background: #0D7680;
    padding: 12px 22px;
    border-radius: 10px;
    color: white;
    font-weight: 600;
    border: none;
    cursor: pointer;
    margin-right: 10px;
}

/* HERO CARD */
.hp-hero {
    background: #0D7680;
    color: white;
    padding: 32px;
    border-radius: 14px;
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

/* LISTING CARD */
.hp-card {
    background: white;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# NAV BAR
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
    if cols[i].button(p, key=p, help="", use_container_width=True):
        st.session_state.active = p

# -----------------------------------------------------------
# HOME DASHBOARD
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

    # SECTION TITLE
    st.markdown("### 🔥 Trending homes near you")

    # MAP + LISTING
    left, right = st.columns([1.3, 1])

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
            opacity=0.8
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

    with right:

        st.markdown("""
        <div class="hp-card">
            <img src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg"
                 width="100%" style="border-radius:12px; margin-bottom:12px;" />

            <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                <div>
                    <div style="font-size:22px; font-weight:700;">$579,900</div>
                    <div>4 bd | 3 ba | 2,580 sq ft</div>
                    <div>Downtown, Detroit, MI</div>
                </div>
                <button class="hp-pill-btn">Constrain</button>
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
                    <div style="font-weight:700; color:#0B9D4A;">+5.2%</div>
                </div>
            </div>

        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------
# PAGE ROUTING
# -----------------------------------------------------------
if st.session_state.active == "Home dashboard":
    page_home()
else:
    st.title(st.session_state.active)
    st.write("Page coming soon.")












