import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="HomePathAI Demo",
    page_icon="🏠",
    layout="wide",
)

# Hide Streamlit chrome and tighten padding
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>HomePathAI Demo</title>

<style>
:root {
  --bg: #e9f1f4;
  --card: #ffffff;
  --primary: #0b7899;
  --primary-dark: #075e78;
  --accent: #f97316;
  --text-main: #123047;
  --text-sub: #5f7d95;
}

/* global */
*,
*::before,
*::after { box-sizing:border-box; }

body {
  margin:0;
  font-family: system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  background:var(--bg);
  color:var(--text-main);
}

/* page wrapper */
.hp-page {
  min-height:100vh;
  padding:24px 24px 40px;
}

/* header bar */
.hp-header-inner {
  max-width:1120px;
  margin:0 auto 16px;
  padding:16px 20px;
  background:var(--card);
  border-radius:999px;
  display:flex;
  align-items:center;
  gap:20px;
  box-shadow:0 8px 24px rgba(13,55,87,0.08);
}

.hp-logo {
  display:flex;
  align-items:center;
  gap:10px;
}

.hp-logo-icon {
  width:40px;
  height:40px;
  border-radius:12px;
  background:var(--primary);
  display:flex;
  align-items:center;
  justify-content:center;
  color:#fff;
  font-weight:700;
}

.hp-logo-text {
  font-weight:700;
  font-size:18px;
}

/* tabs */
.hp-top-tabs {
  display:flex;
  flex-wrap:wrap;
  gap:8px;
}

.hp-top-tabs button {
  border:0;
  border-radius:999px;
  padding:8px 14px;
  background:#e0f3f8;
  color:var(--text-main);
  font-size:13px;
  cursor:pointer;
}

.hp-top-tabs button.is-active {
  background:var(--primary);
  color:#fff;
}

/* hero card */
.hp-hero {
  max-width:1120px;
  margin:0 auto 20px;
  background:var(--card);
  border-radius:20px;
  padding:20px 24px;
  box-shadow:0 18px 40px rgba(9,33,62,0.08);
}

.hp-hero-title {
  font-size:20px;
  margin:0 0 4px;
}

.hp-hero-sub {
  margin:0 0 18px;
  font-size:13px;
  color:var(--text-sub);
}

/* search bar */
.hp-search-container {
  max-width:1120px;
  margin:0 auto 20px;
  background:var(--card);
  border-radius:16px;
  padding:16px 18px;
  box-shadow:0 18px 40px rgba(9,33,62,0.06);
}

.hp-search-box {
  display:flex;
  gap:10px;
}

.hp-search-input {
  flex:1;
  padding:10px 14px;
  border-radius:999px;
  border:1px solid #d4e2ec;
  font-size:14px;
}

.hp-search-btn {
  border-radius:999px;
  border:0;
  padding:10px 22px;
  background:var(--primary);
  color:#fff;
  cursor:pointer;
  font-weight:600;
}

/* trending */
.hp-section {
  max-width:1120px;
  margin:0 auto 32px;
}

.hp-section-header {
  display:flex;
  align-items:center;
  gap:6px;
  font-size:16px;
  margin-bottom:12px;
}

.hp-section-header span.emoji {
  font-size:18px;
}

.hp-trending-grid {
  display:grid;
  grid-template-columns: minmax(0,1.15fr) minmax(0,1fr);
  gap:18px;
}

/* map & cards */
.hp-map-card,
.hp-home-card {
  background:var(--card);
  border-radius:18px;
  overflow:hidden;
  box-shadow:0 18px 40px rgba(9,33,62,0.10);
}

.hp-map-img,
.hp-home-img {
  display:block;
  width:100%;
  height:220px;
  object-fit:cover;
}

.hp-home-body {
  padding:16px 18px 18px;
}

.hp-home-price {
  margin:0 0 4px;
  font-size:20px;
}

.hp-home-details {
  margin:0 0 10px;
  font-size:13px;
  color:var(--text-sub);
}

.hp-home-metrics {
  display:flex;
  flex-wrap:wrap;
  gap:10px 20px;
  font-size:13px;
  margin-bottom:14px;
}

.hp-metric-label {
  display:block;
  color:var(--text-sub);
  font-size:11px;
  text-transform:uppercase;
  letter-spacing:0.04em;
}

.hp-metric-value {
  font-weight:600;
  color:var(--text-main);
}

.hp-metric-positive {
  color:#169c4b;
}

.hp-const-btn {
  border:0;
  border-radius:999px;
  padding:8px 16px;
  background:var(--primary-dark);
  color:#fff;
  font-size:13px;
  font-weight:600;
  cursor:pointer;
}
</style>
</head>
<body>
  <div class="hp-page">
    <!-- HEADER -->
    <header class="hp-header">
      <div class="hp-header-inner">
        <div class="hp-logo">
          <div class="hp-logo-icon">AI</div>
          <div>
            <div class="hp-logo-text">HomePathAI</div>
            <div style="font-size:12px;color:#5f7d95;">A.I. that thinks like a local.</div>
          </div>
        </div>
        <nav class="hp-top-tabs">
          <button class="is-active">First time buyer friendly</button>
          <button>Investor deal analysis</button>
          <button>Neighbor insights</button>
          <button>Repair estimator</button>
          <button>Rent &amp; moving</button>
          <button>Rent &amp; moving tools</button>
        </nav>
      </div>
    </header>

    <!-- HERO -->
    <section class="hp-hero">
      <h1 class="hp-hero-title">Find your next home with AI that actually thinks like a local.</h1>
      <p class="hp-hero-sub">
        HomePathAI analyzes neighborhoods, repairs, and numbers so you don’t have to guess.
      </p>
    </section>

    <!-- SEARCH -->
    <section class="hp-search-container">
      <div class="hp-search-box">
        <input class="hp-search-input" type="text" placeholder="Search city, neighborhood, or ZIP" />
        <button class="hp-search-btn">Search</button>
      </div>
      <p style="margin:8px 4px 0;font-size:12px;color:#5f7d95;">
        Your AI-powered home search companion for smarter buying.
      </p>
    </section>

    <!-- TRENDING -->
    <section class="hp-section">
      <div class="hp-section-header">
        <span class="emoji">🔥</span>
        <span>Trending homes near you</span>
      </div>

      <div class="hp-trending-grid">
        <!-- LEFT: heatmap -->
        <article class="hp-map-card">
          <img
            class="hp-map-img"
            src="https://i.ibb.co/ct3gmL6/heatmap-demo.png"
            alt="Neighborhood heatmap"
          />
          <div class="hp-home-body">
            <h3 style="margin:0 0 8px;font-size:16px;">Neighborhood snapshot</h3>
            <div style="display:flex;gap:20px;font-size:13px;">
              <div>
                <span class="hp-metric-label">Safety score</span>
                <span class="hp-metric-value">78</span>
              </div>
              <div>
                <span class="hp-metric-label">Median home price</span>
                <span class="hp-metric-value">$340,000</span>
              </div>
            </div>
          </div>
        </article>

        <!-- RIGHT: featured home -->
        <article class="hp-home-card">
          <img
            class="hp-home-img"
            src="https://i.ibb.co/9Y7Q653/house-night.jpg"
            alt="Featured home"
          />
          <div class="hp-home-body">
            <h3 class="hp-home-price">$579,900</h3>
            <p class="hp-home-details">
              4 bd | 3 ba | 2,580 sq ft<br/>
              Downtown, Detroit, MI
            </p>
            <div class="hp-home-metrics">
              <div>
                <span class="hp-metric-label">Nete score</span>
                <span class="hp-metric-value">88</span>
              </div>
              <div>
                <span class="hp-metric-label">Est. value</span>
                <span class="hp-metric-value">$340,000</span>
              </div>
              <div>
                <span class="hp-metric-label">5-yr growth</span>
                <span class="hp-metric-value hp-metric-positive">+5.2%</span>
              </div>
            </div>
            <button class="hp-const-btn">Constrain this deal</button>
          </div>
        </article>
      </div>
    </section>
  </div>
</body>
</html>
"""

components.html(html, height=950, scrolling=True)

