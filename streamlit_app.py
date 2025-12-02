import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="HomePathAI Demo",
    page_icon="🏠",
    layout="wide",
)

# ============================================
# SIDEBAR NAVIGATION (Matches screenshot)
# ============================================
st.sidebar.title("HomePathAI")
st.sidebar.caption("AI home assistant for buyers, renters, investors & agents.")
st.sidebar.write("---")
st.sidebar.markdown("### Navigate")
st.sidebar.button("Buyer Hub")
st.sidebar.button("Investor Hub")
st.sidebar.button("Neighbor Hub")
st.sidebar.button("Repair & Moving")
st.sidebar.button("Agent Hub")
st.sidebar.button("Help / About")

# ============================================
# HERO HEADER (Matches your screenshot style)
# ============================================
st.markdown(
    """
    <div style="padding: 28px; background:#0f1c2e; border-radius:12px; color:white;">
        <h1 style="margin:0px;">Find your next home with AI that actually thinks like a local.</h1>
        <p style="opacity:0.9;">Smart search, investor-grade numbers, repair tools — all in one experience built for first-time buyers, flippers, house hackers, and renters.</p>

        <div style="margin-top:12px;">
            <span style="padding:8px 14px; background:#1d2f49; border-radius:8px; margin-right:6px;">First-time buyer friendly</span>
            <span style="padding:8px 14px; background:#1d2f49; border-radius:8px; margin-right:6px;">Investor deal analysis</span>
            <span style="padding:8px 14px; background:#1d2f49; border-radius:8px; margin-right:6px;">Neighborhood insights</span>
            <span style="padding:8px 14px; background:#1d2f49; border-radius:8px; margin-right:6px;">Repair estimator</span>
            <span style="padding:8px 14px; background:#1d2f49; border-radius:8px;">Rent & moving tools</span>
        </div>

        <div style="margin-top:18px;">
            <input placeholder="SmartSearch — conversational search" 
                   style="width:70%; padding:12px; border-radius:8px; border:none;"/>
            <button style="padding:12px 18px; background:#4ca1ff; border:none; border-radius:8px; margin-left:8px; color:white;">
                Search
            </button>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ============================================
# SMARTSEARCH QUICK DEMO
# ============================================
col1, col2 = st.columns([3,1])
with col1:
    st.text_input(
        "Describe what you're looking for", 
        placeholder="Eg. 3 bed under $250k in a safe Detroit suburb with good schools"
    )
with col2:
    st.selectbox("I'm searching as a:", ["Buyer", "Investor", "Renter", "Moving"])

st.button("Run SmartSearch (demo)", type="primary")

st.write("---")

# ============================================
# TRENDING HOMES
# ============================================
st.subheader("🔥 Trending homes near you")

home_data = [
    {
        "price": "$289,000",
        "beds": "3 bd | 2 ba | 1,900 sq ft",
        "city": "Detroit, MI",
        "score": 78,
        "est_value": "$310,000",
        "growth": "+5.4%",
        "img": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7"
    },
    {
        "price": "$420,000",
        "beds": "4 bd | 2 ba | 2,300 sq ft",
        "city": "Grand Rapids, MI",
        "score": 82,
        "est_value": "$440,000",
        "growth": "+6.1%",
        "img": "https://images.unsplash.com/photo-1572120360610-d971b9d7767c"
    },
    {
        "price": "$365,000",
        "beds": "3 bd | 2 ba | 1,850 sq ft",
        "city": "Chicago, IL",
        "score": 80,
        "est_value": "$390,000",
        "growth": "+4.2%",
        "img": "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd"
    },
]

cols = st.columns(3)
for col, house in zip(cols, home_data):
    with col:
        st.image(house["img"], use_column_width=True)
        st.markdown(f"### {house['price']}")
        st.write(house["beds"])
        st.caption(house["city"])

        st.write(f"**HomePathAI Score:** {house['score']}")
        st.write(f"**Est. value:** {house['est_value']}")
        st.write(f"**5-yr growth:** {house['growth']}")

        st.button("Constrain this deal", key=house["price"])

st.write("---")

# ============================================
# INTERACTIVE HEATMAP (REAL MAP)
# ============================================
st.subheader("🗺️ Neighborhood snapshot")

lat_center = 42.3314
lon_center = -83.0458

heat_df = pd.DataFrame({
    "lat": np.random.normal(lat_center, 0.02, 300),
    "lon": np.random.normal(lon_center, 0.02, 300),
})

st.map(heat_df, zoom=10)
st.caption("Safety, price, and walkability at a glance — demo heatmap.")

st.write("---")

# ============================================
# REPAIR ESTIMATOR PREVIEW
# ============================================
st.subheader("🛠️ Repair estimator preview")
st.write("Upload home photos and instantly estimate AI repair costs (demo).")

st.image(
    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c",
    caption="Sample property"
)

st.write("---")


