import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# ---------------------------------------------------
# PAGE SETUP
# ---------------------------------------------------
st.set_page_config(page_title="HomePathAI Demo", layout="wide")

# ---------------------------------------------------
# TOP NAVIGATION PILLS (CLICKABLE)
# ---------------------------------------------------
PAGES = [
    "Buyer Hub",
    "Investor Hub",
    "Neighborhood Insights",
    "Repair Estimator",
    "Rent & Moving"
]

st.markdown("""
<style>
.navbar {
    display:flex;
    gap:10px;
    margin-bottom:25px;
}
.navbtn {
    padding:12px 18px;
    background:#0A395A15;
    border-radius:8px;
    border:none;
    font-size:14px;
    color:#0A395A;
    cursor:pointer;
    font-weight:600;
}
.navbtn:hover {
    background:#0A395A22;
}
.active {
    background:#0A395A;
    color:white !important;
}
</style>
""", unsafe_allow_html=True)

# Store active page
if "active_page" not in st.session_state:
    st.session_state.active_page = "Buyer Hub"

st.markdown("<div class='navbar'>", unsafe_allow_html=True)

for p in PAGES:
    css = "navbtn active" if p == st.session_state.active_page else "navbtn"
    if st.button(p, key=p, help=p, use_container_width=False):
        st.session_state.active_page = p
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# PAGE RENDER FUNCTIONS
# ---------------------------------------------------

# ---------- BUYER HUB ----------
def page_buyer():
    st.image("https://i.imgur.com/hp7bSAS.png", width=60)
    st.markdown("## First-time buyer friendly 👋")
    st.markdown("AI resources & beginner-friendly tips")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📘 First-time buyer basics")
        st.caption("Buying your first home? Start here.")
        st.write("---")
    with col2:
        st.markdown("### 📝 Step-by-step guides")
        st.caption("Understand each phase of buying.")
        st.write("---")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("### 🧮 Affordability calculator")
        st.caption("See what you can comfortably afford.")
    with col4:
        st.markdown("### 🏦 Mortgage pre-approval")
        st.caption("Get pre-approved for better rates.")

    st.write("")
    st.markdown("### Have questions?")
    st.button("Ask our AI assistant")

# ---------- INVESTOR HUB ----------
def page_investor():
    st.markdown("## Compare Cities")
    st.caption("Understanding key differences before you invest or move.")

    col1, col2, col3 = st.columns([2,2,1])
    col1.selectbox("Select a city", ["Detroit, MI","Chicago, IL","Miami, FL"])
    col2.selectbox("Compare with", ["Pittsburgh, PA","Cleveland, OH","Dallas, TX"])
    col3.button("Compare")

    st.write("---")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### 💵 Cost of living")
        st.metric("", "8%", "above avg")
    with c2:
        st.markdown("### 🛡 Crime rate")
        st.metric("", "High")
    with c3:
        st.markdown("### 🏫 Schools")
        st.metric("", "6.4", "avg rating")

# ---------- NEIGHBORHOOD INSIGHTS ----------
def page_neighborhood():
    st.markdown("## Neighborhood snapshot")
    st.caption("Safety, price, and walkability at a glance.")

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

# ---------- REPAIR ESTIMATOR ----------
def page_repair():
    st.image("https://i.imgur.com/hp7bSAS.png", width=55)
    st.markdown("## Repair estimator")

    st.write("### $51,800")
    st.caption("Based on analysis of similar homes")

    left, right = st.columns(2)
    with left:
        st.markdown("### Repair costs breakdown")
        st.write("""
        - Roof — **$9,500**  
        - HVAC — **$7,800**  
        - Kitchen — **$15,000**  
        - Bathrooms — **$5,500**  
        - Interior Paint — **$3,500**  
        - Landscaping — **$5,500**
        """)

    with right:
        st.markdown("### Comparable homes")
        st.write("""
        - 456 Maple Rd — **$240k**  
        - 28 Grand Ave — **$265k**  
        - 788 Elmwood — **$230k**
        """)

# ---------- RENT & MOVING ----------
def page_rent():
    st.image("https://i.imgur.com/hp7bSAS.png", width=55)
    st.markdown("## Rent Listings")

    c1, c2, c3 = st.columns([2,1,1])
    c1.text_input("City or ZIP", "Detroit, MI")
    c2.text_input("Budget", "$1,800")
    c3.button("Search")

    st.write("---")
    st.markdown("### Rent Budget Helper")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### $1,600/mo — Detroit, MI")
    with col2:
        st.markdown("#### $1,750/mo — Dearborn, MI")

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











