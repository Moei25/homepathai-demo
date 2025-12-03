import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="HomePathAI Demo",
    layout="wide",
)

# ---------------------------------------------------
# LOGO + HEADER
# ---------------------------------------------------
st.markdown("""
<div style="display:flex;align-items:center;gap:10px;margin-bottom:25px;">
    <img src="https://i.imgur.com/hp7bS4S.png" width="38">
    <span style="font-size:32px;font-weight:700;color:#0A395A;">HomePathAI</span>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# NAVIGATION PILLS
# ---------------------------------------------------
st.markdown("""
<div style="display:flex;gap:12px;margin-bottom:20px;">
    <button class="pill">First time buyer friendly</button>
    <button class="pill">Investor deal analysis</button>
    <button class="pill">Neighbor insights</button>
    <button class="pill">Repair estimator</button>
    <button class="pill">Rent & moving tools</button>
</div>

<style>
.pill {
    padding: 12px 18px;
    background:#E0F4FF;
    border-radius: 10px;
    border:none;
    color:#0A395A;
    font-size:14px;
    cursor:pointer;
}
.pill:hover {
    background:#c8eaff;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HERO HEADER
# ---------------------------------------------------
st.markdown("""
<div style="
    background: linear-gradient(135deg, #0086b3, #00aeca, #14c5d9);
    padding:40px;
    border-radius:20px;
    color:white;
    margin-bottom:45px;
">
    <h1 style="font-size:40px;font-weight:700;margin-bottom:5px;">
        Smart search for your next home — powered by AI.
    </h1>

    <p style="opacity:0.95;font-size:19px;">
        Neighborhood insights, investor-grade numbers, repair tools, 
        moving resources, and first-time buyer help — all in one experience built for real people.
    </p>

    <!-- SEARCH BAR -->
    <div style="margin-top:25px;display:flex;gap:10px;">
        <input placeholder="Search city, neighborhood, or ZIP" 
               style="flex:1;padding:14px;border-radius:10px;border:1px solid #ccc;font-size:16px;">
        <button style="padding:14px 28px;background:#005F73;color:white;border:none;border-radius:10px;font-size:16px;">
            Search
        </button>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TRENDING HOMES TITLE
# ---------------------------------------------------
st.markdown("## 🔥 Trending homes near you")
st.write("Sample homes across Detroit and nearby areas — demo data only.")

# ---------------------------------------------------
# LAYOUT
# ---------------------------------------------------
left, right = st.columns([1.3, 1])

# ---------------------------------------------------
# LEFT : HEATMAP
# ---------------------------------------------------
with left:
    st.subheader("Neighborhood snapshot")
    st.caption("Safety, price, and walkability at a glance – demo map.")

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
            pitch=40
        )
    )

    st.pydeck_chart(deck)

# ---------------------------------------------------
# RIGHT : LISTING CARD
# ---------------------------------------------------
with right:
    st.markdown("""
    <div style="
        background:white;
        border-radius:18px;
        padding:20px;
        box-shadow:0 4px 18px rgba(0,0,0,0.12);
    ">
        <img src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg"
             style="width:100%;border-radius:15px;margin-bottom:15px;">

        <div style="font-size:22px;font-weight:700;">$579,900</div>
        <div style="color:#666;">4 bd | 3 ba | 2,580 sq ft</div>
        <div style="color:#0A395A;margin-bottom:15px;">Downtown, Detroit, MI</div>

        <!-- SCORE ROW -->
        <div style="display:flex;justify-content:space-between;margin-bottom:10px;">
            <div>
                <div style="text-transform:uppercase;font-size:12px;color:#0A395A;">HomePathAI score</div>
                <div style="font-size:20px;font-weight:700;">88</div>
            </div>

            <div>
                <div style="text-transform:uppercase;font-size:12px;color:#0A395A;">Est. value</div>
                <div style="font-size:20px;font-weight:700;">$340,000</div>
            </div>

            <div>
                <div style="text-transform:uppercase;font-size:12px;color:#0A395A;">5-yr growth</div>
                <div style="font-size:20px;font-weight:700;color:#059669;">+5.2%</div>
            </div>
        </div>

        <button style="
            width:100%;
            padding:14px;
            background:#0A395A;
            color:white;
            border:none;
            border-radius:10px;
            font-size:16px;
            cursor:pointer;
        ">
            Constrain this deal
        </button>

    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.write("")
st.caption("This is a visual demo for HomePathAI — colors, map, layout, and card match the investor concept.")











