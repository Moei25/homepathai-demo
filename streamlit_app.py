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
    body {
        background: #e9f1f4;
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
  <title>HomePathAI Demo</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
  *,
  *::before,
  *::after {
    box-sizing: border-box;
  }

  body {
    margin: 0;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
      sans-serif;
    background: #e9f1f4;
    color: #123047;
  }

  .hp-page {
    min-height: 100vh;
    padding: 24px 16px 40px;
  }

  .hp-header {
    margin-bottom: 16px;
  }

  .hp-header-inner {
    max-width: 1120px;
    margin: 0 auto;
    background: #ffffff;
    border-radius: 16px;
    padding: 16px 20px 20px;
    box-shadow: 0 8px 20px rgba(15, 35, 52, 0.08);
  }

  .hp-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 16px;
  }

  .hp-logo-icon {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: #0b7899;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    font-weight: 700;
    font-size: 16px;
  }

  .hp-logo-house {
    font-size: 15px;
  }

  .hp-logo-text {
    font-weight: 700;
    font-size: 20px;
    color: #123047;
  }

  .hp-top-tabs {
    display: flex;
    flex-wrap: nowrap;
    gap: 10px;
  }

  .hp-tab-button {
    border: none;
    border-radius: 999px;
    padding: 10px 18px;
    background: #0b7899;
    color: #e7f6fb;
    font-size: 14px;
    cursor: pointer;
    white-space: nowrap;
    transition: background 0.15s ease, box-shadow 0.15s ease;
  }

  .hp-tab-button.is-active {
    background: #0a607a;
    box-shadow: 0 4px 10px rgba(6, 59, 89, 0.4);
  }

  .hp-tab-button:not(.is-active):hover {
    background: #0d86ad;
  }

  .hp-main {
    max-width: 1120px;
    margin: 12px auto 0;
  }

  .hp-tab-panel {
    display: none;
  }

  .hp-tab-panel.is-active {
    display: block;
  }

  .hp-card {
    background: #ffffff;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(12, 37, 58, 0.12);
  }

  .hp-panel-card {
    padding: 24px 28px 28px;
    margin-bottom: 18px;
  }

  .hp-page-title {
    margin: 0 0 4px;
    font-size: 26px;
    font-weight: 700;
    color: #123047;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .hp-emoji-wave {
    font-size: 24px;
  }

  .hp-page-subtitle {
    margin: 0 0 20px;
    color: #50657a;
  }

  .hp-grid-2 {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
  }

  .hp-grid-3 {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 14px;
  }

  .hp-feature-card {
    border: none;
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 16px 18px;
    background: #f7fbfd;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(8, 31, 48, 0.06);
    cursor: pointer;
    text-align: left;
  }

  .hp-feature-card-tight {
    cursor: default;
  }

  .hp-feature-icon-block {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    background: #0b7899;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    color: #ffffff;
  }

  .hp-feature-text h2 {
    margin: 0 0 4px;
    font-size: 16px;
  }

  .hp-feature-text p {
    margin: 0;
    font-size: 14px;
    color: #52677b;
  }

  .hp-cta-section {
    margin-top: 28px;
    text-align: center;
  }

  .hp-cta-question {
    margin-bottom: 10px;
    font-weight: 600;
  }

  .hp-primary-btn {
    border: none;
    border-radius: 999px;
    padding: 10px 22px;
    font-size: 15px;
    font-weight: 600;
    background: #0b7899;
    color: #ffffff;
    cursor: pointer;
    box-shadow: 0 6px 15px rgba(10, 76, 105, 0.5);
  }

  .hp-btn-inline {
    margin-top: 12px;
  }

  .hp-primary-btn:hover {
    background: #0a607a;
  }

  .hp-muted {
    color: #6b8195;
    font-size: 14px;
  }

  .hp-panel-header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
  }

  .hp-logo-left {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .hp-panel-links {
    display: flex;
    gap: 18px;
    font-size: 14px;
  }

  .hp-panel-links a {
    color: #0b7899;
    text-decoration: none;
  }

  .hp-panel-links a:hover {
    text-decoration: underline;
  }

  .hp-logo-small {
    font-size: 14px;
    font-weight: 600;
    color: #123047;
  }

  .hp-compare-controls {
    display: grid;
    grid-template-columns: 1.1fr 1.1fr auto;
    gap: 10px;
    margin-bottom: 18px;
  }

  .hp-form-group {
    display: flex;
    flex-direction: column;
    gap: 4px;
    font-size: 14px;
  }

  .hp-form-group label {
    color: #47617a;
  }

  .hp-form-group input,
  .hp-form-group select {
    border-radius: 999px;
    border: 1px solid #c0d1df;
    padding: 8px 12px;
    font-size: 14px;
    outline: none;
  }

  .hp-form-group input:focus,
  .hp-form-group select:focus {
    border-color: #0b7899;
  }

  .hp-btn-compare {
    align-self: flex-end;
    padding-inline: 20px;
  }

  .hp-compare-cards {
    margin-top: 6px;
  }

  .hp-stat-card {
    padding: 16px 16px 18px;
    border-radius: 14px;
    background: #f7fbfd;
    box-shadow: 0 4px 10px rgba(8, 31, 48, 0.06);
    text-align: center;
  }

  .hp-stat-icon {
    font-size: 24px;
    margin-bottom: 6px;
  }

  .hp-stat-main {
    margin: 6px 0 2px;
    font-size: 22px;
    font-weight: 700;
  }

  .hp-repair-header {
    display: grid;
    grid-template-columns: 2.1fr 1.1fr;
    gap: 12px;
    margin-top: 8px;
    margin-bottom: 18px;
  }

  .hp-readonly-input {
    border-radius: 999px;
    border: 1px solid #c0d1df;
    padding: 9px 12px;
    font-size: 14px;
    background: #f7fbfd;
    color: #3f566b;
  }

  .hp-repair-body {
    align-items: flex-start;
  }

  .hp-repair-amount {
    font-size: 34px;
    font-weight: 700;
    margin: 0 0 4px;
    color: #123047;
  }

  .hp-section-title {
    margin: 18px 0 10px;
    font-size: 16px;
  }

  .hp-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
  }

  .hp-table th,
  .hp-table td {
    padding: 8px 4px;
    border-bottom: 1px solid #dde6ee;
    text-align: left;
  }

  .hp-comps-list {
    list-style: none;
    padding: 0;
    margin: 6px 0 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
    font-size: 14px;
  }

  .hp-comps-list li {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    padding-bottom: 8px;
    border-bottom: 1px solid #dde6ee;
  }

  .hp-comp-meta {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 2px;
  }

  .hp-investor-card {
    padding: 16px 18px;
    border-radius: 12px;
    background: #f7fbfd;
    box-shadow: 0 4px 10px rgba(8, 31, 48, 0.06);
  }

  .hp-form-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 10px 12px;
  }

  .hp-metrics-list {
    list-style: none;
    padding: 0;
    margin: 8px 0 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
    font-size: 14px;
  }

  .hp-metrics-list li {
    display: flex;
    justify-content: space-between;
  }

  .hp-rent-top {
    display: grid;
    grid-template-columns: 2.2fr 1.1fr;
    gap: 18px;
  }

  .hp-rent-search h2 {
    margin: 4px 0 4px;
    font-size: 20px;
  }

  .hp-form-grid-3 {
    grid-template-columns: 1.3fr 1.1fr 0.9fr;
    margin-top: 8px;
  }

  .hp-form-grid-2 {
    margin-top: 10px;
  }

  .hp-form-group-button {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
  }

  .hp-full-width {
    width: 100%;
  }

  .hp-rent-side h3 {
    margin: 0 0 4px;
    font-size: 16px;
  }

  .hp-rent-side h3 span {
    color: #0b7899;
  }

  .hp-rent-budget-card {
    margin-top: 12px;
  }

  .with-icon {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .hp-house-icon {
    font-size: 18px;
  }

  .hp-rent-cards {
    margin-top: 10px;
  }

  .hp-rent-card {
    border-radius: 14px;
    overflow: hidden;
    background: #f7fbfd;
    box-shadow: 0 6px 15px rgba(9, 32, 49, 0.15);
  }

  .hp-rent-image {
    height: 150px;
    background: linear-gradient(135deg, #1d3557, #14213d);
  }

  .hp-rent-image-house {
    background: linear-gradient(135deg, #1d3557, #0b7899);
  }

  .hp-rent-body {
    padding: 12px 14px 14px;
  }

  .hp-rent-price {
    margin: 0 0 4px;
    font-weight: 700;
  }

  .hp-rent-label {
    margin: 8px 0 0;
    font-size: 14px;
    color: #1b3a4b;
    font-weight: 500;
  }

  .hp-renttools-grid {
    margin-top: 10px;
  }

  @media (max-width: 900px) {
    .hp-header-inner {
      padding: 14px 14px 16px;
    }

    .hp-top-tabs {
      flex-wrap: wrap;
    }

    .hp-grid-2,
    .hp-grid-3,
    .hp-compare-controls,
    .hp-repair-header,
    .hp-rent-top,
    .hp-form-grid-3 {
      grid-template-columns: 1fr;
    }

    .hp-panel-card {
      padding-inline: 16px;
    }
  }
 /* ===== HOMEPAGE: HERO, SEARCH, TRENDING GRID, MAP & HOME CARD ===== */

.hp-homepage {
    max-width: 1120px;
    margin: 0 auto;
    padding: 24px 0 60px;
}

/* Hero title */
.hp-hero-title {
    font-size: 34px;
    font-weight: 700;
    color: #123047;
    margin-bottom: 12px;
}

/* Search bar box */
.hp-search-container {
    background: #ffffff;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(10, 35, 52, 0.08);
    margin-bottom: 32px;
}

.hp-search-box {
    display: flex;
    gap: 12px;
}

.hp-search-input {
    flex: 1;
    padding: 14px 16px;
    border-radius: 12px;
    border: 1px solid #ccd1df;
    font-size: 16px;
}

.hp-search-btn {
    background: #0b7899;
    border: none;
    color: #fff;
    padding: 14px 26px;
    border-radius: 12px;
    font-weight: 600;
    cursor: pointer;
}

/* Trending homes + map layout */
.hp-section-header {
    font-size: 20px;
    font-weight: 700;
    color: #123047;
    margin: 10px 0 18px;
}

.hp-trending-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
}

/* Left: Map Card */
.hp-map-card {
    background: #fff;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(10, 35, 52, 0.08);
}

.hp-map-img {
    width: 100%;
    border-radius: 12px;
    margin-bottom: 12px;
}

.hp-map-info h3 {
    font-size: 18px;
    margin-bottom: 6px;
}

.hp-metric {
    font-size: 15px;
    margin-bottom: 4px;
}

/* Right: Home card */
.hp-home-card {
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(10, 35, 52, 0.08);
    overflow: hidden;
}

.hp-home-img {
    width: 100%;
    height: 180px;
    object-fit: cover;
}

.hp-home-body {
    padding: 18px 14px;
}

.hp-home-price {
    font-size: 22px;
    font-weight: 700;
    color: #123047;
    margin-bottom: 6px;
}

.hp-home-details {
    font-size: 14px;
    color: #52677b;
    margin-bottom: 12px;
}

.hp-home-metrics {
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.hp-metric-label {
    font-weight: 600;
}

.hp-metric-value {
    margin-left: 6px;
}

.hp-positive {
    color: #169c4b;
    font-weight: 600;
}

.hp-const-btn {
    margin-top: 14px;
    border: none;
    background: #0b7899;
    color: #fff;
    padding: 12px 24px;
    border-radius: 12px;
    cursor: pointer;
    font-weight: 600;
}
 </style>
</head>
<body>
  <div class="hp-page">
    <header class="hp-header">
      <div class="hp-header-inner">
        <div class="hp-logo">
          <div class="hp-logo-icon">
            <span class="hp-logo-house">A</span>
          </div>
          <span class="hp-logo-text">HomePathAI</span>
        </div>

        <nav class="hp-top-tabs">
          <button class="hp-tab-button is-active" data-tab="buyer">
            First time buyer friendly
          </button>
          <button class="hp-tab-button" data-tab="investor">
            Investor deal analysis
          </button>
          <button class="hp-tab-button" data-tab="neighborhood">
            Neighbor insights
          </button>
          <button class="hp-tab-button" data-tab="repair">
            Repair estimator
          </button>
          <button class="hp-tab-button" data-tab="rent">
            Rent &amp; moving
          </button>
          <button class="hp-tab-button" data-tab="renttools">
            Rent &amp; moving tools
          </button>
        </nav>
      </div>
    </header>

    <main class="hp-main">
      <!-- FIRST-TIME BUYER TAB -->
      <section id="tab-buyer" class="hp-tab-panel is-active">
        <div class="hp-card hp-panel-card">
          <h1 class="hp-page-title">
            First-time buyer friendly<span class="hp-emoji-wave">👋</span>
          </h1>
          <p class="hp-page-subtitle">
            AI resources &amp; beginner-friendly tips
          </p>

          <div class="hp-grid-2">
            <button class="hp-feature-card">
              <div class="hp-feature-icon-block">📘</div>
              <div class="hp-feature-text">
                <h2>First-time buyer basics</h2>
                <p>Buying your first home? Start here!</p>
              </div>
            </button>

            <button class="hp-feature-card">
              <div class="hp-feature-icon-block">📋</div>
              <div class="hp-feature-text">
                <h2>Step-by-step guides</h2>
                <p>Understand each phase of buying</p>
              </div>
            </button>

            <button class="hp-feature-card">
              <div class="hp-feature-icon-block">🧮</div>
              <div class="hp-feature-text">
                <h2>Affordability calculator</h2>
                <p>See what you can comfortably afford</p>
              </div>
            </button>

            <button class="hp-feature-card">
              <div class="hp-feature-icon-block">🧾</div>
              <div class="hp-feature-text">
                <h2>Mortgage pre-approval</h2>
                <p>Get pre-approved for better rates</p>
              </div>
            </button>
          </div>

          <div class="hp-cta-section">
            <p class="hp-cta-question">Have questions?</p>
            <button class="hp-primary-btn">Ask our AI assistant</button>
          </div>
        </div>
<!-- HOMEPAGE (NEW) -->
<section class="hp-homepage">

    <!-- Top search section -->
    <div class="hp-search-container">
        <h1 class="hp-hero-title">Find your next home with AI that actually thinks like a local.</h1>

        <div class="hp-search-box">
            <input type="text" placeholder="Search city, neighborhood, or ZIP" class="hp-search-input" />
            <button class="hp-search-btn">Search</button>
        </div>

        <p class="hp-subtext">Your AI-powered home search companion for smarter buying</p>
    </div>


    <!-- Trending homes + map layout -->
    <h2 class="hp-section-header">🔥 Trending homes near you</h2>

    <div class="hp-trending-grid">

        <!-- LEFT: Heatmap card -->
        <div class="hp-map-card">
            <img src="https://i.ibb.co/6tq3mL6/heatmap-demo.png" class="hp-map-img" />
            <div class="hp-map-info">
                <h3>Neighborhood snapshot</h3>
                <p class="hp-metric"><b>78</b> Safety score</p>
                <p class="hp-metric">Median home price <b>$340,000</b></p>
            </div>
        </div>

        <!-- RIGHT: Home card preview -->
        <div class="hp-home-card">
            <img src="https://i.ibb.co/9V7pG5J/house-night.jpg" class="hp-home-img" />
            <div class="hp-home-body">

                <h3 class="hp-home-price">$579,900</h3>
                <p class="hp-home-details">
                    4 bd | 3 ba | 2,580 sq ft <br />
                    Downtown, Detroit, MI
                </p>

                <div class="hp-home-metrics">
                    <div>
                        <span class="hp-metric-label">Nete score</span>
                        <span class="hp-metric-value">$340,000</span>
                    </div>
                    <div>
                        <span class="hp-metric-label">Growth</span>
                        <span class="hp-metric-value hp-positive">+5.2%</span>
                    </div>
                </div>

                <button class="hp-const-btn">Constrain</button>

            </div>
        </div>

    </div>

</section>
<script>
document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".hp-tab-button");
    const panels = {
        buyer: document.getElementById("tab-buyer"),
        investor: document.getElementById("tab-investor"),
        neighborhood: document.getElementById("tab-neighborhood"),
        repair: document.getElementById("tab-repair"),
        rent: document.getElementById("tab-rent"),
        tools: document.getElementById("tab-renttools")
    };

    buttons.forEach((btn) => {
        btn.addEventListener("click", () => {
            const target = btn.dataset.tab;

            buttons.forEach(b => b.classList.remove("is-active"));
            btn.classList.add("is-active");

            Object.values(panels).forEach(p => p.classList.remove("is-active"));
            panels[target].classList.add("is-active");
        });
    });
});
</script>
"""
components.html(html, height=950, scrolling=True)
