import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="HomePathAI Demo",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# GLOBAL STYLES (colors & layout to match your screenshot)
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    /* Overall page background */
    .stApp {
        background-color: #f4fafb;
    }

    /* Remove default top padding */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Hero wrapper */
    .hero-wrapper {
        margin: 0 auto 1.75rem auto;
    }

    .hero-card {
        background: white;
        border-radius: 18px;
        padding: 24px 28px 26px 28px;
        box-shadow: 0 16px 50px rgba(15, 57, 78, 0.15);
        border: 1px solid #e1f1f5;
    }

    .logo-row {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 18px;
    }

    .logo-icon {
        width: 36px;
        height: 36px;
        border-radius: 10px;
        background: #006d77;
        color: #ffffff;
        font-weight: 700;
        font-size: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.18);
    }

    .logo-text {
        font-size: 24px;
        font-weight: 700;
        color: #0f3447;
    }

    /* Top nav pill buttons (visual only) */
    .nav-pill-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 18px;
    }

    .nav-pill {
        padding: 10px 18px;
        border-radius: 999px;
        border: none;
        background-color: #008a96;
        color: #ffffff;
        font-size: 13px;
        cursor: default;
        white-space: nowrap;
        font-weight: 500;
        box-shadow: 0 6px 16px rgba(0, 90, 102, 0.25);
    }

    /* Search bar row */
    .search-row {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 6px;
    }

    .search-input {
        flex: 1;
        border-radius: 999px;
        border: 1px solid #d6e7ec;
        padding: 12px 18px;
        font-size: 15px;
        outline: none;
    }

    .search-input::placeholder {
        color: #95a4b1;
    }

    .search-button {
        border-radius: 999px;
        background-color: #008a96;
        color: white;
        border: none;
        padding: 11px 26px;
        font-size: 15px;
        font-weight: 600;
        cursor: pointer;
        box-shadow: 0 6px 18px rgba(0, 90, 102, 0.35);
    }

    .search-tagline {
        font-size: 12px;
        color: #70808e;
        margin-top: 2px;
    }

    /* Section title */
    .section-heading {
        font-size: 20px;
        font-weight: 700;
        color: #113d4d;
        margin-top: 10px;
        margin-bottom: 12px;
    }

    .section-subtitle {
        font-size: 12px;
        color: #7b8b96;
        margin-bottom: 10px;
    }

    /* Trending layout */
    .trending-grid {
        display: grid;
        grid-template-columns: minmax(0, 1.1fr) minmax(0, 1.1fr);
        gap: 18px;
        align-items: stretch;
    }

    /* Left card (heatmap) */
    .heatmap-card {
        background: white;
        border-radius: 18px;
        padding: 14px 14px 10px 14px;
        border: 1px solid #e1f1f5;
        box-shadow: 0 10px 30px rgba(23, 66, 88, 0.07);
        height: 100%;
        display: flex;
        flex-direction: column;
    }

    .heatmap-title-row {
        display: flex;
        align-items: center;
        gap: 6px;
        margin-bottom: 2px;
    }

    .heatmap-chip {
        font-size: 11px;
        color: #7b8b96;
    }

    .heatmap-title {
        font-size: 16px;
        font-weight: 700;
        color: #113d4d;
        margin-top: 4px;
        margin-bottom: 4px;
    }

    .heatmap-meta {
        font-size: 11px;
        color: #7b8b96;
    }

    /* Right listing card */
    .listing-card {
        background: white;
        border-radius: 18px;
        border: 1px solid #e1f1f5;
        box-shadow: 0 10px 30px rgba(23, 66, 88, 0.07);
        overflow: hidden;
        display: flex;
        flex-direction: column;
        height: 100%;
    }

    .listing-image {
        width: 100%;
        height: 190px;
        object-fit: cover;
    }

    .listing-body {
        padding: 16px 18px 18px 18px;
        display: flex;
        flex-direction: column;
        gap: 4px;
    }

    .listing-price {
        font-size: 22px;
        font-weight: 700;
        color: #113d4d;
    }

    .listing-meta {
        font-size: 12px;
        color: #70808e;
    }

    .listing-city {
        font-size: 12px;
        color: #7b8b96;
        margin-bottom: 6px;
    }

    .listing-pill-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 6px;
        margin-bottom: 2px;
        font-size: 11px;
        color: #7b8b96;
    }

    .listing-score-label {
        text-transform: uppercase;
        letter-spacing: 0.09em;
        font-size: 10px;
        color: #7b8b96;
    }

    .listing-score-value {
        font-weight: 700;
        color: #113d4d;
        font-size: 13px;
    }

    .listing-growth {
        font-weight: 700;
        color: #039672;
        font-size: 14px;
    }

    .constrain-btn {
        margin-top: 10px;
        display: inline-flex;
        padding: 7px 16px;
        border-radius: 999px;
        border: none;
        background: #0d7f94;
        color: #ffffff;
        font-size: 12px;
        font-weight: 600;
        cursor: pointer;
    }

    /* Make embedded elements full width inside Streamlit columns */
    .full-width {
        width: 100%;
    }

    @media (max-width: 900px) {
        .trending-grid {
            grid-template-columns: minmax(0, 1fr);
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# HERO HEADER (matches Screenshot A style)
# ---------------------------------------------------------
hero_html = """
<div class="hero-wrapper">
  <div class="hero-card">
    <div class="logo-row">
      <div class="logo-icon">AI</div>
      <div class="logo-text">HomePathAI</div>
    </div>

    <div class="nav-pill-row">
      <button class="nav-pill">First time buyer friendly</button>
      <button class="nav-pill">Investor deal analysis</button>
      <button class="nav-pill">Neighbor insights</button>
      <button class="nav-pill">Repair estimator</button>
      <button class="nav-pill">Rent & moving tools</button>
    </div>

    <div style="font-size: 28px; font-weight: 700; color:#113d4d; margin-bottom: 4px;">
      Find your next home with AI that actually thinks like a local.
    </div>

    <div style="font-size: 13px; color:#70808e; margin-bottom: 14px;">
      Neighborhood insights, investor-grade numbers, repair tools, and moving resources —
      all in one experience built for real people.
    </div>

    <div class="search-row">
      <input class="search-input" placeholder="Search city, neighborhood, or ZIP" />
      <button class="search-button">Search</button>
    </div>

    <div class="search-tagline">
      Your AI-powered home search companion for smarter buying.
    </div>
  </div>
</div>
"""

st.markdown(hero_html, unsafe_allow_html=True)

# ---------------------------------------------------------
# "Trending homes near you" SECTION
# ---------------------------------------------------------
st.markdown('<div class="section-heading">🔥 Trending homes near you</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-subtitle">Sample homes across Detroit and nearby areas – demo data only.</div>',
    unsafe_allow_html=True,
)

# Create container for map + listing card
st.markdown('<div class="trending-grid">', unsafe_allow_html=True)

# ----------------- LEFT: HEATMAP CARD --------------------
# We'll use a pydeck heatmap centered roughly near Detroit
np.random.seed(42)
num_points = 200
center_lat, center_lon = 42.3314, -83.0458  # Detroit approx

latitudes = center_lat + 0.25 * (np.random.rand(num_points) - 0.5)
longitudes = center_lon + 0.35 * (np.random.rand(num_points) - 0.5)

heat_df = pd.DataFrame({"lat": latitudes, "lon": longitudes, "weight": np.random.rand(num_points)})

heatmap_layer = pdk.Layer(
    "HeatmapLayer",
    data=heat_df,
    get_position="[lon, lat]",
    aggregation="MEAN",
    get_weight="weight",
    radiusPixels=40,
)

view_state = pdk.ViewState(
    latitude=center_lat,
    longitude=center_lon,
    zoom=8.2,
    pitch=0,
)

deck = pdk.Deck(layers=[heatmap_layer], initial_view_state=view_state, map_style="light")

left_col, right_col = st.columns((1.1, 1.1))

with left_col:
    st.markdown(
        """
        <div class="heatmap-card">
          <div class="heatmap-title-row">
            <span class="heatmap-chip">Heetmap</span>
          </div>
          <div class="heatmap-title">Neighborhood snapshot</div>
          <div class="heatmap-meta">Safety score, price, and walkability at a glance – demo map.</div>
        """,
        unsafe_allow_html=True,
    )

    st.pydeck_chart(deck, use_container_width=True)

    st.markdown(
        """
          <div class="heatmap-meta" style="margin-top:6px;">
            Demo data only. In a real version, this would reflect live HomePathAI scores.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ----------------- RIGHT: LISTING CARD --------------------
with right_col:
    listing_html = """
    <div class="listing-card">
      <img class="listing-image" src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=1200" />
      <div class="listing-body">
        <div class="listing-price">$579,900</div>
        <div class="listing-meta">4 bd | 3 ba | 2,580 sq ft</div>
        <div class="listing-city">Downtown, Detroit, MI</div>

        <div class="listing-pill-row">
          <div>
            <div class="listing-score-label">HomePathAI score</div>
            <div class="listing-score-value">88</div>
          </div>
          <div>
            <div class="listing-score-label">Est. value</div>
            <div class="listing-score-value">$340,000</div>
          </div>
          <div>
            <div class="listing-score-label">5-yr growth</div>
            <div class="listing-growth">+5.2%</div>
          </div>
        </div>

        <button class="constrain-btn">Constrain this deal</button>
      </div>
    </div>
    """
    st.markdown(listing_html, unsafe_allow_html=True)

# Close trending-grid wrapper
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Little footer note
# ---------------------------------------------------------
st.write("")
st.caption(
    "This is a non-functional visual demo for HomePathAI – colors, layout, map, and card match the concept for investors."
)








