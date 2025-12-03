import streamlit as st
import pandas as pd
import pydeck as pdk

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(
    page_title="HomePathAI Demo",
    page_icon="🏠",
    layout="wide",
)

# ------------------------------------------------------------
# GLOBAL CSS (colors + layout to match your screenshot)
# ------------------------------------------------------------
st.markdown(
    """
<style>
/* Make background light grey like the mockup */
[data-testid="stAppViewContainer"] {
    background-color: #f4f7f9;
}

/* Center the main content and give it breathing room */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Logo row */
.hp-header-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 18px;
}

.hp-logo-circle {
    width: 36px;
    height: 36px;
    border-radius: 10px;
    background: #007f9f;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 700;
    font-size: 16px;
    font-family: system-ui, sans-serif;
}

.hp-logo-text {
    font-size: 24px;
    font-weight: 700;
    color: #064457;
    font-family: system-ui, sans-serif;
}

/* Main hero card */
.hp-hero-card {
    background: white;
    border-radius: 18px;
    padding: 26px 28px 30px 28px;
    box-shadow: 0 10px 28px rgba(15, 68, 88, 0.18);
    position: relative;
    overflow: hidden;
}

/* Teal gradient bar behind content */
.hp-hero-banner {
    background: linear-gradient(135deg, #0f92ce, #0d8fab, #14c5d9);
    border-radius: 18px;
    padding: 26px 28px 30px 28px;
    color: white;
}

/* Top nav pills row */
.hp-nav-pill-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 20px;
}

.hp-nav-pill {
    padding: 10px 16px;
    border-radius: 999px;
    border: none;
    background: rgba(255, 255, 255, 0.16);
    color: white;
    font-size: 13px;
    font-weight: 500;
    cursor: pointer;
    white-space: nowrap;
}

/* Main hero title */
.hp-hero-title {
    font-size: 26px;
    font-weight: 700;
    margin: 6px 0 4px 0;
}

/* Hero tagline (white on teal) */
.hp-hero-tagline {
    font-size: 13px;
    opacity: 0.95;
    max-width: 580px;
}

/* Search row */
.hp-search-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 18px;
}

.hp-search-input {
    flex: 1;
    padding: 11px 14px;
    border-radius: 999px;
    border: none;
    font-size: 14px;
    outline: none;
}

.hp-search-btn {
    padding: 11px 26px;
    border-radius: 999px;
    border: none;
    background: #008bb6;
    color: white;
    font-weight: 600;
    font-size: 14px;
    cursor: pointer;
}

/* Small helper text under search */
.hp-search-caption {
    margin-top: 10px;
    font-size: 12px;
    opacity: 0.95;
}

/* Section titles */
.hp-section-title {
    font-size: 18px;
    font-weight: 700;
    margin-top: 26px;
    margin-bottom: 4px;
}

.hp-section-caption {
    font-size: 12px;
    color: #56616a;
    margin-bottom: 10px;
}

/* Trending homes container */
.hp-trending-card {
    background: white;
    border-radius: 18px;
    padding: 18px 18px 20px 18px;
    box-shadow: 0 8px 22px rgba(0, 0, 0, 0.06);
}

/* Listing card on the right */
.hp-listing-card {
    background: #f7fafc;
    border-radius: 18px;
    overflow: hidden;
    font-family: system-ui, sans-serif;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.10);
}

.hp-listing-image {
    width: 100%;
    height: 190px;
    object-fit: cover;
    display: block;
}

.hp-listing-body {
    padding: 14px 16px 18px 16px;
}

.hp-listing-price {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 4px;
}

.hp-listing-meta {
    font-size: 12px;
    color: #56616a;
    margin-bottom: 3px;
}

.hp-listing-city {
    font-size: 12px;
    color: #7b8794;
    margin-bottom: 10px;
}

/* Score rows */
.hp-pill-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 12px;
}

.hp-score-pill {
    display: flex;
    flex-direction: column;
    padding: 8px 10px;
    border-radius: 10px;
    background: white;
    min-width: 110px;
}

.hp-score-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    color: #7b8794;
    margin-bottom: 2px;
}

.hp-score-value {
    font-size: 14px;
    font-weight: 600;
    color: #0b7285;
}

/* Growth pill (green) */
.hp-score-growth {
    font-size: 14px;
    font-weight: 600;
    color: #0c8a4b;
}

/* Constrain button */
.hp-constrain-btn {
    margin-top: 12px;
    padding: 9px 16px;
    border-radius: 999px;
    border: none;
    background: #008bb6;
    color: white;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
}

</style>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# HERO HEADER BLOCK (matches screenshot layout + colors)
# ------------------------------------------------------------
hero_html = """
<div class="hp-header-row">
  <div class="hp-logo-circle">AI</div>
  <div class="hp-logo-text">HomePathAI</div>
</div>

<div class="hp-hero-card">
  <div class="hp-hero-banner">

    <div class="hp-nav-pill-row">
      <button class="hp-nav-pill">First time buyer friendly</button>
      <button class="hp-nav-pill">Investor deal analysis</button>
      <button class="hp-nav-pill">Neighbor insights</button>
      <button class="hp-nav-pill">Repair estimator</button>
      <button class="hp-nav-pill">Rent &amp; moving tools</button>
    </div>

    <div class="hp-hero-title">
      Smart search for your next home — powered by AI.
    </div>

    <div class="hp-hero-tagline">
      Neighborhood insights, investor-grade numbers, repair tools, moving resources,
      and first-time buyer help — all in one experience built for real people.
    </div>

    <div class="hp-search-row">
      <input class="hp-search-input" placeholder="Search city, neighborhood, or ZIP" />
      <button class="hp-search-btn">Search</button>
    </div>

    <div class="hp-search-caption">
      Your AI-powered home search companion for smarter buying.
    </div>

  </div>
</div>
"""

st.markdown(hero_html, unsafe_allow_html=True)

# ------------------------------------------------------------
# TRENDING HOMES SECTION – TITLE & CAPTION
# ------------------------------------------------------------
st.markdown('<div class="hp-section-title">🔥 Trending homes near you</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hp-section-caption">Sample homes across Detroit and nearby areas – demo data only.</div>',
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# TRENDING HOMES LAYOUT: LEFT = MAP, RIGHT = LISTING CARD
# ------------------------------------------------------------
left_col, right_col = st.columns([1.15, 0.85])

# ---- LEFT: HEATMAP / NEIGHBORHOOD SNAPSHOT ----
with left_col:
    st.markdown(
        '<div class="hp-trending-card"><div class="hp-section-caption" '
        'style="margin-bottom:4px;">Neighborhood snapshot</div>'
        '<div class="hp-section-caption" style="margin-bottom:12px;">'
        'Safety, price, and walkability at a glance – demo heatmap.'
        '</div>',
        unsafe_allow_html=True,
    )

    # Demo points (roughly around Detroit / SE Michigan)
    map_df = pd.DataFrame(
        {
            "lat": [42.3314, 42.38, 42.30, 42.43, 42.28, 42.36, 42.32, 42.35],
            "lon": [-83.0458, -83.10, -83.06, -83.02, -83.09, -82.99, -83.15, -83.20],
            "weight": [0.8, 0.5, 0.9, 0.6, 0.4, 0.7, 0.9, 0.3],
        }
    )

    heat_layer = pdk.Layer(
        "HeatmapLayer",
        data=map_df,
        get_position="[lon, lat]",
        get_weight="weight",
        radius_pixels=60,
    )

    view_state = pdk.ViewState(
        latitude=42.3314,
        longitude=-83.0458,
        zoom=9,
        pitch=0,
    )

    deck = pdk.Deck(
        layers=[heat_layer],
        initial_view_state=view_state,
        map_style="mapbox://styles/mapbox/light-v9",
        tooltip={"text": "Demo intensity"},
    )

    st.pydeck_chart(deck, use_container_width=True)

    # Close the white card div started above
    st.markdown("</div>", unsafe_allow_html=True)

# ---- RIGHT: LISTING CARD ----
with right_col:
    listing_html = """
    <div class="hp-listing-card">
      <img class="hp-listing-image"
           src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=1200"
           alt="Home exterior" />
      <div class="hp-listing-body">

        <div class="hp-listing-price">$579,900</div>
        <div class="hp-listing-meta">4 bd | 3 ba | 2,580 sq ft</div>
        <div class="hp-listing-city">Downtown, Detroit, MI</div>

        <div class="hp-pill-row">
          <div class="hp-score-pill">
            <div class="hp-score-label">HomePathAI score</div>
            <div class="hp-score-value">88</div>
          </div>
          <div class="hp-score-pill">
            <div class="hp-score-label">Est. value</div>
            <div class="hp-score-value">$340,000</div>
          </div>
          <div class="hp-score-pill">
            <div class="hp-score-label">5-yr growth</div>
            <div class="hp-score-growth">+5.2%</div>
          </div>
        </div>

        <button class="hp-constrain-btn">Constrain this deal</button>

      </div>
    </div>
    """

    st.markdown(listing_html, unsafe_allow_html=True)

# ------------------------------------------------------------
# FOOTNOTE FOR INVESTORS
# ------------------------------------------------------------
st.write("")
st.caption(
    "This is a non-functional visual demo for HomePathAI – colors, layout, map, and card "
    "match the concept you can show to investors."
)









