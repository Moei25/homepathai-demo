import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(page_title="HomePathAI", layout="wide")

# -----------------------------------------------------------
# GLOBAL CSS — EXACT COLORS FROM YOUR SCREENSHOT
# -----------------------------------------------------------
st.markdown("""
<style>

body {
    background-color: #F2F6F7;
}

/* TOP NAV BUTTONS */
.hp-nav-btn {
    background: #0C7682;                 /* EXACT screenshot teal */
    padding: 14px 26px;
    border-radius: 12px;
    color: white;
    font-size: 15px;
    font-weight: 600;
    border: none;
    cursor: pointer;
    margin-right: 12px;
    transition: 0.2s;
}

.hp-nav-btn:hover {
    background: #0A5D68;
}

/* ACTIVE BUTTON */
.hp-active {
    background: #094E56 !important;
}

/* HERO BAR */
.hp-hero {
    background: #0C7682;                /* EXACT screenshot blue/teal */
    color: white;
    padding: 32px;
    border-radius: 14px;
    margin-top: 15px;
}

/* HERO INPUT */
.hp-hero-input {
    width: 70%;
    padding: 15px;
    border-radius: 10px;
    border: none;
    font-size: 16px;
}

/* HERO SEARCH BUTTON */
.hp-hero-btn {
    padding: 15px 28px;
    background: #0A5D68;
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
}

/* LABELS */
.hp-label {
    color:#8890A0;
    font-size:14px;
}

.hp-value {
    font-weight:700;
    font-size:16px;
}

.hp-green {
    color:#0B9D4A;
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
    active_class = "hp-active" if st.session_state.active == p else ""
    if cols[i].button(
        p,
        key=p,
        use_container_width=True
    ):
        st.session_state.active = p

    # Apply CSS manually
    cols[i].markdown(
        f"""
        <style>
            div[data-testid="baseButton-secondary"][key="{p}"] button {{
                background: {'#094E56' if st.session_state.active == p else '#0C7682'};
                color: white;
                border-radius: 12px;
                padding: 14px 26px;
                font-size: 15px;
                font-weight: 600;
                border: none;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------------
# HOME PAGE (EXACT SCREENSHOT)
# -----------------------------------------------------------
def page_home():

    # HERO SECTION
    st.markdown("""
    <div class="hp-hero">

        <h2>Smart search for your next home — powered by AI.</h2>
        <p style="margin-top:-5px;">
            Neighborhood insights, investor-grade numbers, repair tools,
            moving resources, and first-time buyer help — all in one experience.
        </p>

        <div style="display:flex; gap:12px; margin-top:16px;">
            <input class="hp-hero-input" placeholder="Search city, neighborhood, or ZIP" />
            <button class="hp-hero-btn">Search</button>
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔥 Trending homes near you")

    left, right = st.columns([1.35, 1])

    # ------------------- HEATMAP (left)
    with left:
        st.markdown("#### Neighborhood snapshot")

        df = pd.DataFrame({
            "lat": np.random.uniform(42.28, 42.42, 250),
            "lon": np.random.uniform(-83.5, -83.0, 250),
            "value": np.random.uniform(0, 1, 250)
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

    # ------------------- LISTING CARD (right)
    with right:

        st.markdown("""
        <div class="hp-card">

            <img src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg"
                 width="100%" style="border-radius:12px; margin-bottom:12px;" />

            <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                <div>
                    <div style="font-size:22px; font-weight:700;">$579,900</div>
                    <div>4 bd | 3 ba | 2,580 sq ft</div>
                    <div>Downtown, Detroit, MI</div>
                </div>

                <button style="
                    background:#0C7682;
                    color:white;
                    border:none;
                    padding:8px 16px;
                    border-radius:10px;
                    font-weight:600;
                ">Constrain</button>
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
        """, unsafe_allow_html=True)

# -----------------------------------------------------------
# ROUTER
# -----------------------------------------------------------
if st.session_state.active == "Home dashboard":
    page_home()
else:
    st.title(st.session_state.active)
    st.write("Page coming soon.")














