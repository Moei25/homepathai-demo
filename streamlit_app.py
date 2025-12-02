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
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>HomePathAI Demo</title>

<style>
*,
*::before,
*::after {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background: #e9f1f4;
    color: #123047;
}

/* PAGE WRAPPER */
.hp-page {
    min-height: 100vh;
    padding: 20px;
}

/* HEADER */
.hp-header {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin-bottom: 20px;
    gap: 16px;
}

.hp-logo {
    display: flex;
    align-items: center;
    gap: 8px;
}

.hp-logo-house {
    background: #1a83c6;
    color: #fff;
    font-weight: 700;
    padding: 8px 12px;
    border-radius: 8px;
}

.hp-logo-text {
    font-size: 22px;
    font-weight: 700;
}

/* TABS */
.hp-top-tabs {
    display: flex;
    gap: 12px;
    margin-bottom: 22px;
}

.hp-tab-button {
    padding: 10px 20px;
    border-radius: 20px;
    background: #c4e7f3;
    border: none;
    cursor: pointer;
    transition: 0.2s ease;
}

.hp-tab-button.is-active {
    background: #1a83c6;
    color: white;
}

/* PANELS */
.hp-tab-panel {
    display: none;
    padding: 20px;
    border-radius: 12px;
    background: white;
}

.hp-tab-panel.is-active {
    display: block;
}

/* DEMO BLOCKS */
.hp-demo-box {
    background: white;
    padding: 24px;
    border-radius: 12px;
    margin-top: 20px;
}
</style>
</head>

<body>
<div class="hp-page">

    <header class="hp-header">
        <div class="hp-logo">
            <span class="hp-logo-house">A</span>
            <span class="hp-logo-text">HomePathAI</span>
        </div>
    </header>

    <nav class="hp-top-tabs">
        <button class="hp-tab-button is-active" data-tab="buyer">First time buyer friendly</button>
        <button class="hp-tab-button" data-tab="investor">Investor deal analysis</button>
        <button class="hp-tab-button" data-tab="neighborhood">Neighbor insights</button>
        <button class="hp-tab-button" data-tab="repair">Repair estimator</button>
        <button class="hp-tab-button" data-tab="rent">Rent & moving</button>
        <button class="hp-tab-button" data-tab="renttools">Rent & moving tools</button>
    </nav>

    <!-- PANELS -->
    <div id="tab-buyer" class="hp-tab-panel is-active">
        <h2>First-time buyer friendly</h2>
        <p>AI resources & beginner-friendly tips.</p>
    </div>

    <div id="tab-investor" class="hp-tab-panel">
        <h2>Investor deal analysis</h2>
        <p>ROI, cash-on-cash, comp analysis coming soon.</p>
    </div>

    <div id="tab-neighborhood" class="hp-tab-panel">
        <h2>Neighborhood insights</h2>
        <p>Heatmaps, safety score, walkability coming soon.</p>
    </div>

    <div id="tab-repair" class="hp-tab-panel">
        <h2>Repair estimator</h2>
        <p>Upload home photos to get AI repair cost estimates.</p>
    </div>

    <div id="tab-rent" class="hp-tab-panel">
        <h2>Rent & moving</h2>
        <p>Tools for moving cost estimates & rent research.</p>
    </div>

    <div id="tab-renttools" class="hp-tab-panel">
        <h2>Moving tools</h2>
        <p>Checklists, truck rentals, packing calculators.</p>
    </div>

</div>
<!-- HOMEPAGE CONTENT BELOW TABS -->

<!-- 🔥 Trending homes near you (demo) -->
<section class="hp-section">
  <h2 class="hp-section-header">🔥 Trending homes near you</h2>

  <div class="hp-trending-grid">
    
    <!-- HOME CARD 1 -->
    <div class="hp-home-card">
      <img src="https://i.ibb.co/jT7HJRL/house-night.jpg" class="hp-home-img" />
      <div class="hp-home-body">
        <h3 class="hp-home-price">$289,000</h3>
        <p class="hp-home-details">
          3 bd | 2 ba | 1,900 sq ft <br />
          Detroit, MI
        </p>

        <div class="hp-home-metrics">
          <div>
            <span class="hp-metric-label">Safety score</span>
            <span class="hp-metric-value">72/100</span>
          </div>
          <div>
            <span class="hp-metric-label">Median price</span>
            <span class="hp-metric-value">$140,000</span>
          </div>
        </div>

        <button class="hp-const-btn">View details</button>
      </div>
    </div>

    <!-- HOME CARD 2 -->
    <div class="hp-home-card">
      <img src="https://i.ibb.co/0YPG657/house-night.jpg" class="hp-home-img" />
      <div class="hp-home-body">
        <h3 class="hp-home-price">$344,900</h3>
        <p class="hp-home-details">
          4 bd | 2 ba | 2,130 sq ft <br />
          Grand Rapids, MI
        </p>

        <div class="hp-home-metrics">
          <div>
            <span class="hp-metric-label">Value score</span>
            <span class="hp-metric-value">$340,000</span>
          </div>
          <div>
            <span class="hp-metric-label">Growth</span>
            <span class="hp-metric-value hp-positive">+5.2%</span>
          </div>
        </div>

        <button class="hp-const-btn">View details</button>
      </div>
    </div>

  </div>
</section>


<!-- 🏙 Neighborhood snapshot (demo) -->
<section class="hp-section">
  <h2 class="hp-section-header">Neighborhood snapshot (demo)</h2>

  <p>Heatmap, schools, crime levels, walkability scores.</p>

  <img src="https://i.ibb.co/4tgzm16/heatmap-demo.png" class="hp-map-img" />

</section>


<!-- 🔧 Repair estimator preview -->
<section class="hp-section">
  <h2 class="hp-section-header">AI repair estimator (demo)</h2>

  <p>Upload home photos and instantly estimate repair costs.</p>

  <img src="https://i.ibb.co/4YPG657/house-night.jpg" class="hp-home-img" />

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
        renttools: document.getElementById("tab-renttools")
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

</body>
</html>
"""
components.html(html, height=950, scrolling=True)
