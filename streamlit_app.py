import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# ---------------------------------------------------
# PAGE CONFIG + THEME FIX
# ---------------------------------------------------
st.set_page_config(page_title="HomePathAI Demo", layout="wide")

# GLOBAL THEME CSS
st.markdown("""
<style>

body {
    background-color: #F7F9FB;
    font-family: 'Inter', sans-serif;
}

/* NAVIGATION BAR */
.navbar {
    display: flex;
    gap: 12px;
    margin-bottom: 30px;
}

.navbtn {
    padding: 12px 18px;
    border-radius: 8px;
    border: none;
    background: #0A395A22;
    color: #0A395A;
    font-weight: 600;
    font-size: 14px;
    cursor: pointer;
}

.navbtn:hover {
    background: #0A395A33;
}

.active {
    background: #0A395A !important;
    color: white !important;
}

/* CARD STYLE */
.card {
    background: white;
    padding: 26px;
    border-radius: 14px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

/* HEADINGS */
h2, h3 {
    color: #0A395A;
    font-weight: 700;
}

/* METRICS */
.metric {
    font-size: 34px;
    font-weight: 700;
    color: #0A395A;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# NAVIGATION HANDLER
# ---------------------------------------------------
PAGES = [
    "Buyer Hub",
    "Investor Hub",
    "Neighborhood Insights",
    "Repair Estimator",
    "Rent & Moving"
]

if "active_page" not in st.session_state:
    st.session_state.active_page = "Buyer Hub"

# NAV BAR RENDER
st.markdown("<div class='navbar'>", unsafe_allow_html=True)
for p in PAGES:
    css = "navbtn active" if p == st.session_state.active_page else "navbtn"
    if st.button(p, key=p):
        st.session_state.active_page = p
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# PAGE DEFINITIONS
# ---------------------------------------------------

def page_buyer():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## First-time buyer friendly 👋")
    st.caption("AI resources & beginner-friendly tips")
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📘 First-time buyer basics")
        st.caption("Buying your first home? Start here.")
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📝 Step-by-step guides")
        st.caption("Understand each phase of buying.")
        st.markdown("</div>", unsafe_allow_html=True)

    c3, c4 = st.columns(2)
    with c3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🧮 Affordability calculator")
        st.caption("See what you can comfortably afford.")
        st.markdown("</div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🏦 Mortgage pre-approval")
        st.caption("Get pre-approved for better rates.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Have questions?")
    st.button("Ask our AI assistant")
    st.markdown("</div>", unsafe_allow_html=True)


def page_investor():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## Compare Cities")
    st.caption("Understanding key differences before you invest or move.")
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,2,1])
    col1.selectbox("Select a city", ["Detroit, MI", "Chicago, IL", "Miami, FL"])
    col2.selectbox("Compare with", ["Pittsburgh, PA", "Cleveland, OH", "Dallas, TX"])
    col3.button("Compare")

    st.write("")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 💵 Cost of living")
        st.markdown("<div class='metric'>8%</div>", unsafe_allow_html=True)
        st.caption("Above average")
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🛡 Crime rate")
        st.markdown("<div class='metric'>High</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🏫 Schools")
        st.markdown("<div class='metric'>6.4</div>", unsafe_allow_html=True)
        st.caption("Average rating")
        st.markdown("</div>", unsafe_allow_html=True)


def page_neighborhood():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## Neighborhood snapshot")
    st.caption("Safety, price, and walkability at a glance — demo map.")
    st.markdown("</div>", unsafe_allow_html=True)

    df = pd.DataFrame({
        "lat": np.random.uniform(42.28, 42.42, 250),
        "lon": np.random.uniform(-83.5, -83.0, 250),
        "value": np.random.uniform(0, 1, 250),
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
            zoom=8,
            pitch=40,
        )
    )

    st.pydeck_chart(deck)


def page_repair():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## Repair estimator")
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Repair costs breakdown")
        st.write("""
        - Roof — **$9,500**
        - HVAC — **$7,800**
        - Kitchen — **$15,000**
        - Bathrooms — **$5,500**
        - Interior Paint — **$3,500**
        - Landscaping — **$5,500**
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Comparable homes")
        st.write("""
        - 456 Maple Rd — **$240k**
        - 28 Grand Ave — **$265k**
        - 788 Elmwood — **$230k**
        """)
        st.markdown("</div>", unsafe_allow_html=True)


def page_rent():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## Rent Listings")
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([2,1,1])
    c1.text_input("City or ZIP", "Detroit, MI")
    c2.text_input("Budget", "$1,800")
    c3.button("Search")

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Rent Budget Helper")
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------
# RENDER ACTIVE PAGE
# ---------------------------------------------------
if st.session_state.active_page == "Buyer Hub":
    page_buyer()
elif st.session_state.active_page == "Investor Hub":
    page_investor()
elif st.session_state.active_page == "Neighborhood Insights":
    page_neighborhood()
elif st.session_state.active_page == "Repair Estimator":
    page_repair()
elif st.session_state.active_page == "Rent & Moving":
    page_rent()











