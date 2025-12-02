import streamlit as st

st.set_page_config(
    page_title="HomePathAI Demo",
    page_icon="🏠",
    layout="wide",
)

# ---------- GLOBAL CSS (LOOK & FEEL) ----------
st.markdown(
    """
<style>
/* Remove Streamlit padding & gray background */
.main > div {
    padding-top: 0rem;
}
body {
    background: #e9f1f4;
}

/* Page wrapper */
.hp-page {
    max-width: 1200px;
    margin: 0 auto;
    padding: 24px 16px 40px;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    color: #123047;
}

/* HEADER */
.hp-header {
    background: #e9f1f4;
    margin-bottom: 10px;
}

.hp-header-inner {
    background: #ffffff;
    border-radius: 16px;
    padding: 14px 20px;
    box-shadow: 0 8px 20px rgba(15, 35, 52, 0.08);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
}

.hp-logo {
    display: flex;
    align-items: center;
    gap: 10px;
}

.hp-logo-icon {
    width: 34px;
    height: 34px;
    border-radius: 999px;
    background: #0b7899;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    font-weight: 700;
    font-size: 18px;
}

.hp-logo-text {
    font-weight: 800;
    font-size: 22px;
    color: #123047;
}

.hp-logo-sub {
    font-size: 13px;
    color: #577086;
}

/* Make Streamlit tabs look like your top navigation */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 999px;
    background: #cbe5f0;
    color: #0b3a4a;
    padding: 6px 16px;
    font-weight: 600;
    border: none;
}

.stTabs [aria-selected="true"] {
    background: #0b7899 !important;
    color: #ffffff !important;
    box-shadow: 0 4px 10px rgba(6, 59, 89, 0.4);
}

/* SEARCH AREA */
.hp-search-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 22px 24px 18px;
    box-shadow: 0 8px 22px rgba(10, 35, 52, 0.08);
    margin: 18px 0 26px 0;
}

.hp-hero-title {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 10px;
}

.hp-hero-sub {
    font-size: 14px;
    color: #577086;
    margin-bottom: 16px;
}

.hp-search-row {
    display: flex;
    gap: 10px;
    margin-bottom: 6px;
}

.hp-search-input {
    flex: 1;
    border-radius: 999px;
    border: 1px solid #ccd6e4;
    padding: 10px 14px;
    font-size: 14px;
    outline: none;
}

.hp-search-btn {
    border-radius: 999px;
    border: none;
    background: #0b7899;
    color: #ffffff;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    white-space: nowrap;
}

/* TRENDING HOMES */
.hp-section-heading {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 17px;
    font-weight: 700;
    margin: 4px 0 14px 0;
}

.hp-section-heading span {
    font-size: 20px;
}

.hp-trending-grid {
    display: grid;
    grid-template-columns: minmax(0, 1.05fr) minmax(0, 1.1fr);
    gap: 20px;
    margin-bottom: 28px;
}

/* Map / snapshot card */
.hp-map-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 16px;
    box-shadow: 0 6px 18px rgba(15, 35, 52, 0.08);
}

.hp-map-img {
    width: 100%;
    border-radius: 12px;
    margin-bottom: 10px;
}

.hp-map-title {
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 4px;
}

.hp-map-text {
    font-size: 13px;
    color: #577086;
}

/* Home preview card */
.hp-home-card {
    background: #ffffff;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(15, 35, 52, 0.08);
    overflow: hidden;
}

.hp-home-img {
    width: 100%;
    height: 210px;
    object-fit: cover;
}

.hp-home-body {
    padding: 16px 16px 18px;
}

.hp-home-price {
    font-size: 22px;
    font-weight: 700;
    margin: 0 0 4px;
}

.hp-home-details {
    font-size: 13px;
    color: #52677b;
    margin: 0 0 10px;
}

.hp-home-metrics {
    display: flex;
    justify-content: space-between;
    font-size: 13px;
    margin-bottom: 10px;
}

.hp-metric-label {
    color: #6b7c8b;
}

.hp-metric-value {
    font-weight: 600;
}

.hp-positive {
    color: #169c4b;
}

.hp-const-btn {
    width: 100%;
    border-radius: 10px;
    background: #0b7899;
    color: #ffffff;
    border: none;
    padding: 10px 16px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
}

/* Simple content blocks inside tabs */
.hp-tab-content-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 20px 22px 18px;
    box-shadow: 0 6px 18px rgba(15, 35, 52, 0.06);
    margin-top: 14px;
}

.hp-tab-title {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 6px;
}

.hp-tab-text {
    font-size: 14px;
    color: #52677b;
}
</style>
    """,
    unsafe_allow_html=True,
)

# ---------- PAGE WRAPPER ----------
st.markdown('<div class="hp-page">', unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown(
    """
<div class="hp-header">
  <div class="hp-header-inner">
    <div class="hp-logo">
      <div class="hp-logo-icon">A</div>
      <div>
        <div class="hp-logo-text">HomePathAI</div>
        <div class="hp-logo-sub">AI that thinks like a local.</div>
      </div>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ---------- TOP TABS (REAL STREAMLIT TABS, STYLED LIKE NAV) ----------
tab_labels = [
    "First time buyer friendly",
    "Investor deal analysis",
    "Neighbor insights",
    "Repair estimator",
    "Rent & moving",
    "Rent & moving tools",
]
tabs = st.tabs(tab_labels)

# TAB 1
with tabs[0]:
    st.markdown(
        """
<div class="hp-tab-content-card">
  <div class="hp-tab-title">First-time buyer friendly 🏡</div>
  <div class="hp-tab-text">
    Compare payments, understand trade-offs, and let AI explain things in plain English —
    from pre-approval to closing day.
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

# TAB 2
with tabs[1]:
    st.markdown(
        """
<div class="hp-tab-content-card">
  <div class="hp-tab-title">Investor deal analysis 📈</div>
  <div class="hp-tab-text">
    Run instant rental and flip scenarios — cap rate, cash-on-cash, and exit strategy
    drafts you can send to lenders or partners.
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

# TAB 3
with tabs[2]:
    st.markdown(
        """
<div class="hp-tab-content-card">
  <div class="hp-tab-title">Neighborhood insights 🧭</div>
  <div class="hp-tab-text">
    Lifestyle scores, school overlays, crime heatmaps, and commute filters so you don't
    move somewhere that looks good on Zillow but feels wrong in person.
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

# TAB 4
with tabs[3]:
    st.markdown(
        """
<div class="hp-tab-content-card">
  <div class="hp-tab-title">Repair estimator 🔧</div>
  <div class="hp-tab-text">
    Upload walkthrough photos, get a rough scope and budget before you even call a
    contractor. Great for flips and fixer-uppers.
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

# TAB 5
with tabs[4]:
    st.markdown(
        """
<div class="hp-tab-content-card">
  <div class="hp-tab-title">Rent & moving 🚚</div>
  <div class="hp-tab-text">
    Estimate rent ranges, moving truck size, and monthly costs when you're not ready
    to buy yet — still powered by the same engine.
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

# TAB 6
with tabs[5]:
    st.markdown(
        """
<div class="hp-tab-content-card">
  <div class="hp-tab-title">Moving tools & checklists ✅</div>
  <div class="hp-tab-text">
    Turn-by-turn checklist from “thinking about moving” to “first night in your new place”
    so nothing falls through the cracks.
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

# ---------- HOMEPAGE HERO + SEARCH (STATIC DEMO) ----------
st.markdown(
    """
<div class="hp-search-card">
  <div class="hp-hero-title">
    Find your next home with AI that actually thinks like a local.
  </div>
  <div class="hp-hero-sub">
    HomePathAI analyzes neighborhoods, repairs, and numbers so you don't have to guess.
  </div>

  <div class="hp-search-row">
    <input class="hp-search-input" placeholder="Search city, neighborhood, or ZIP" />
    <button class="hp-search-btn">Search</button>
  </div>

  <div class="hp-hero-sub">
    Your AI-powered home search companion for smarter buying.
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ---------- TRENDING HOMES + MAP ----------
st.markdown(
    """
<div class="hp-section-heading">
  <span>🔥</span> <div>Trending homes near you</div>
</div>
""",
    unsafe_allow_html=True,
)

col_map, col_home = st.columns([1, 1])

with col_map:
    st.markdown(
        """
<div class="hp-map-card">
  <img src="https://i.ibb.co/4tgzm16/heatmap-demo.png" class="hp-map-img" />
  <div class="hp-map-title">Neighborhood snapshot</div>
  <div class="hp-map-text">
    Safety: <b>78</b> · Median price: <b>$340,000</b><br/>
    Mixed-income area with strong 5-year appreciation trends.
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

with col_home:
    st.markdown(
        """
<div class="hp-home-card">
  <img src="https://i.ibb.co/QYP06SJ/house-night.jpg" class="hp-home-img" />
  <div class="hp-home-body">
    <div class="hp-home-price">$579,900</div>
    <div class="hp-home-details">
      4 bd · 3 ba · 2,580 sq ft<br/>
      Downtown · Detroit, MI
    </div>

    <div class="hp-home-metrics">
      <div>
        <div class="hp-metric-label">Value score</div>
        <div class="hp-metric-value">$340,000</div>
      </div>
      <div>
        <div class="hp-metric-label">5-yr growth</div>
        <div class="hp-metric-value hp-positive">+5.2%</div>
      </div>
    </div>

    <button class="hp-const-btn">Constrain this deal</button>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

# ---------- CLOSE PAGE WRAPPER ----------
st.markdown("</div>", unsafe_allow_html=True)
