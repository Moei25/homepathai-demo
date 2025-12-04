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
    font-family: 'Segoe UI', sans-serif;
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
    margin-right: 12px;
}

/* HERO */
.hp-hero {
    background: #0D7680;
    color: white;
    padding: 34px;
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
    padding: 14px 28px;
    background:#07525A;
    border-radius: 10px;
    border: none;
    color:white;
    font-weight:700;
    cursor:pointer;
}

/* PROPERTY CARD */
.hp-card {
    background: white;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-top: 18px;
}

/* SMALL METRIC LABELS */
.hp-label {
    color:#8890A0; 
    font-size:13px;
}

.hp-value {
    font-weight:700; 
    font-size:15px;
}

.hp-green {
    color:#0B9D4A;
}

.hp-pill-btn {
    background:#0A6C75;
    color:white;
    font-weight:600;
    padding:10px 18px;
    border-radius:8px;
    border:none;
    cursor:pointer;
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
    if cols[i].button(p, key=p):
        st.session_state.active = p

# -----------------------------------------------------------
# HOME PAGE
# -----------------------------------------------------------
def page_home():

    # HERO SECTION
    st.markdown("""
<div class="hp-hero">

    <h2>Smart search for your next home — powered by AI.</h2>
    <p>Neighborhood insights, investor-grade numbers, repair tools,
       and first-time buyer help — all in one place.</p>

    <div style="display:flex; gap:12px; margin-top:20px;">
        <input class="hp-hero-input" placeholder="Search city, neighborhood, or ZIP" />
        <button class="hp-hero-btn">Search</button>
    </div>

</div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔥 Trending homes near you")

    left, right = st.columns([1.3, 1])

    # MAP
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
            opacity=0.85
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

    # LISTING CARD
    with right:

        st.markdown("""
<div class="hp-card">

    <img src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg"
         width="100%" style="border-radius:12px; margin-bottom:12px;" />

    <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
        <div>
            <div style="font-size:22px; font-weight:700;">$579,900</div>
            <div>4 bd | 3 ba | 2,580 sq ft</div>
            <div>Downtown, Detroit, MI</div>
        </div>
        <button class="hp-pill-btn">Constrain</button>
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
        """, unsafe_allow_html=True)

# -----------------------------------------------------------
# ROUTER
# -----------------------------------------------------------
if st.session_state.active == "Home dashboard":
    page_home()
else:
    st.title(st.session_state.active)
    st.write("Page coming soon.")













