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
      </section>

      <!-- INVESTOR DEAL ANALYSIS TAB -->
      <section id="tab-investor" class="hp-tab-panel">
        <div class="hp-card hp-panel-card">
          <h1 class="hp-page-title">Investor deal analysis</h1>
          <p class="hp-page-subtitle">
            Quickly understand cash flow, returns, and risk on any deal.
          </p>

          <div class="hp-grid-2">
            <div class="hp-investor-card">
              <h2>Deal snapshot</h2>
              <p class="hp-muted">
                Enter a sample deal below to see projected returns.
              </p>
              <div class="hp-form-grid">
                <div class="hp-form-group">
                  <label>Purchase price</label>
                  <input type="text" placeholder="$250,000" />
                </div>
                <div class="hp-form-group">
                  <label>Estimated rent</label>
                  <input type="text" placeholder="$2,100 / mo" />
                </div>
                <div class="hp-form-group">
                  <label>Down payment</label>
                  <input type="text" placeholder="20%" />
                </div>
                <div class="hp-form-group">
                  <label>Interest rate</label>
                  <input type="text" placeholder="6.5%" />
                </div>
              </div>
              <button class="hp-primary-btn hp-btn-inline">
                Run quick analysis
              </button>
            </div>

            <div class="hp-investor-card">
              <h2>Projected returns</h2>
              <ul class="hp-metrics-list">
                <li>
                  <span>Monthly cash flow</span>
                  <strong>$380</strong>
                </li>
                <li>
                  <span>Cash-on-cash return</span>
                  <strong>9.4%</strong>
                </li>
                <li>
                  <span>Cap rate</span>
                  <strong>7.1%</strong>
                </li>
                <li>
                  <span>5-year equity built</span>
                  <strong>$52,000</strong>
                </li>
              </ul>
              <p class="hp-muted">
                Numbers shown are sample outputs only for demo purposes.
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- NEIGHBORHOOD / COMPARE CITIES TAB -->
      <section id="tab-neighborhood" class="hp-tab-panel">
        <div class="hp-card hp-panel-card">
          <div class="hp-panel-header-row">
            <h1 class="hp-page-title">Compare Cities</h1>
            <div class="hp-logo-small">HomePathAI</div>
          </div>
          <p class="hp-page-subtitle">
            Understanding key differences before you invest or move.
          </p>

          <div class="hp-compare-controls">
            <div class="hp-form-group">
              <label>Select a city</label>
              <select>
                <option>Detroit, MI</option>
                <option>Grand Rapids, MI</option>
                <option>Chicago, IL</option>
                <option>Cleveland, OH</option>
              </select>
            </div>
            <div class="hp-form-group">
              <label>Compare with</label>
              <select>
                <option>Pittsburgh, PA</option>
                <option>Columbus, OH</option>
                <option>Indianapolis, IN</option>
              </select>
            </div>
            <button class="hp-primary-btn hp-btn-compare">Compare</button>
          </div>

          <div class="hp-grid-3 hp-compare-cards">
            <div class="hp-stat-card">
              <div class="hp-stat-icon">💲</div>
              <h2>Cost of living</h2>
              <p class="hp-stat-main">8%</p>
              <p class="hp-muted">above average</p>
            </div>

            <div class="hp-stat-card">
              <div class="hp-stat-icon">🛡️</div>
              <h2>Crime rate</h2>
              <p class="hp-stat-main">High</p>
              <p class="hp-muted">vs national average</p>
            </div>

            <div class="hp-stat-card">
              <div class="hp-stat-icon">🏫</div>
              <h2>Schools</h2>
              <p class="hp-stat-main">6.4</p>
              <p class="hp-muted">average rating</p>
            </div>
          </div>
        </div>
      </section>

      <!-- REPAIR ESTIMATOR TAB -->
      <section id="tab-repair" class="hp-tab-panel">
        <div class="hp-card hp-panel-card">
          <div class="hp-panel-header-row">
            <div class="hp-logo-left">
              <div class="hp-logo-icon">
                <span class="hp-logo-house">A</span>
              </div>
              <span class="hp-logo-text">HomePathAI</span>
            </div>
            <div class="hp-panel-links">
              <a href="#">View comps</a>
              <a href="#">Explore funding options</a>
            </div>
          </div>

          <h1 class="hp-page-title">Repair estimator</h1>

          <div class="hp-repair-header">
            <div class="hp-form-group">
              <label>Address</label>
              <div class="hp-readonly-input">
                123 Main St, Detroit, MI · Single-family
              </div>
            </div>
            <div class="hp-form-group">
              <label>Total square footage</label>
              <input type="text" value="1,800" />
            </div>
          </div>

          <div class="hp-grid-2 hp-repair-body">
            <div>
              <p class="hp-repair-amount">$51,800</p>
              <p class="hp-muted">
                Based on analysis of similar homes
              </p>

              <h2 class="hp-section-title">Repair costs breakdown</h2>
              <table class="hp-table">
                <thead>
                  <tr>
                    <th>Item</th>
                    <th>Estimated cost</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td>Roof</td><td>$9,500</td></tr>
                  <tr><td>HVAC</td><td>$7,800</td></tr>
                  <tr><td>Kitchen</td><td>$15,000</td></tr>
                  <tr><td>Bathrooms</td><td>$8,500</td></tr>
                  <tr><td>Interior paint</td><td>$3,500</td></tr>
                  <tr><td>Landscaping</td><td>$5,500</td></tr>
                </tbody>
              </table>
            </div>

            <div>
              <h2 class="hp-section-title">Comparable homes</h2>
              <ul class="hp-comps-list">
                <li>
                  <div>
                    <strong>456 Maple Rd</strong><br />
                    Detroit, MI
                  </div>
                  <div class="hp-comp-meta">
                    <span>$240,000</span>
                    <span>1,750 sq ft</span>
                  </div>
                </li>
                <li>
                  <div>
                    <strong>28 Grand Ave</strong><br />
                    Detroit, MI
                  </div>
                  <div class="hp-comp-meta">
                    <span>$265,000</span>
                    <span>1,900 sq ft</span>
                  </div>
                </li>
                <li>
                  <div>
                    <strong>788 Elmwood Dr</strong><br />
                    Detroit, MI
                  </div>
                  <div class="hp-comp-meta">
                    <span>$230,000</span>
                    <span>1,850 sq ft</span>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <!-- RENT & MOVING TAB -->
      <section id="tab-rent" class="hp-tab-panel">
        <div class="hp-card hp-panel-card">
          <div class="hp-panel-header-row">
            <div class="hp-logo-left">
              <div class="hp-logo-icon">
                <span class="hp-logo-house">A</span>
              </div>
              <span class="hp-logo-text">Rent &amp; Moving</span>
            </div>
          </div>

          <div class="hp-rent-top">
            <div class="hp-rent-search">
              <h2>Rent Listings</h2>
              <p class="hp-muted">
                Browse rentals from MLS feeds that meet your budget
              </p>

              <div class="hp-form-grid hp-form-grid-3">
                <div class="hp-form-group">
                  <label>City or ZIP</label>
                  <input type="text" value="Detroit, MI" />
                </div>
                <div class="hp-form-group">
                  <label>Budget</label>
                  <input type="text" value="$1,800" />
                </div>
                <div class="hp-form-group hp-form-group-button">
                  <label>&nbsp;</label>
                  <button class="hp-primary-btn hp-full-width">
                    Search
                  </button>
                </div>
              </div>

              <div class="hp-form-grid hp-form-grid-2">
                <div class="hp-form-group">
                  <label>Beds</label>
                  <select>
                    <option>Any</option>
                    <option>1+</option>
                    <option>2+</option>
                    <option>3+</option>
                  </select>
                </div>
                <div class="hp-form-group">
                  <label>Bath</label>
                  <select>
                    <option>Any</option>
                    <option>1+</option>
                    <option>2+</option>
                  </select>
                </div>
              </div>
            </div>

            <aside class="hp-rent-side">
              <h3>Moving Hub: <span>Funding</span></h3>
              <p class="hp-muted">
                Explore funding options, rental deposits, and moving grants
                available in your area.
              </p>
            </aside>
          </div>
        </div>

        <div class="hp-card hp-panel-card hp-rent-budget-card">
          <h2 class="hp-section-title with-icon">
            <span class="hp-house-icon">🏠</span>
            Rent Budget Helper
          </h2>

          <div class="hp-grid-2 hp-rent-cards">
            <div class="hp-rent-card">
              <div class="hp-rent-image"></div>
              <div class="hp-rent-body">
                <p class="hp-rent-price">$1,600/mo</p>
                <p class="hp-muted">Studio, 1 bath · Detroit, MI</p>
                <p class="hp-rent-label">Rent only</p>
              </div>
            </div>

            <div class="hp-rent-card">
              <div class="hp-rent-image hp-rent-image-house"></div>
              <div class="hp-rent-body">
                <p class="hp-rent-price">$1,750/mo</p>
                <p class="hp-muted">
                  3 bd | 1,450 sq ft · Dearborn, MI
                </p>
                <p class="hp-rent-label">$750/mo after house-hack</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- RENT & MOVING TOOLS TAB -->
      <section id="tab-renttools" class="hp-tab-panel">
        <div class="hp-card hp-panel-card">
          <h1 class="hp-page-title">Rent &amp; moving tools</h1>
          <p class="hp-page-subtitle">
            Quick calculators and helpers for renters and people relocating.
          </p>

          <div class="hp-grid-3 hp-renttools-grid">
            <div class="hp-feature-card hp-feature-card-tight">
              <div class="hp-feature-icon-block">📍</div>
              <div class="hp-feature-text">
                <h2>Best areas for renters</h2>
                <p>Find renter-friendly neighborhoods by budget.</p>
              </div>
            </div>

            <div class="hp-feature-card hp-feature-card-tight">
              <div class="hp-feature-icon-block">📦</div>
              <div class="hp-feature-text">
                <h2>Moving cost estimator</h2>
                <p>Get a rough estimate of moving expenses.</p>
              </div>
            </div>

            <div class="hp-feature-card hp-feature-card-tight">
              <div class="hp-feature-icon-block">⚖️</div>
              <div class="hp-feature-text">
                <h2>Rent vs. buy helper</h2>
                <p>Compare long-term costs of renting vs buying.</p>
              </div>
            </div>

            <div class="hp-feature-card hp-feature-card-tight">
              <div class="hp-feature-icon-block">🤝</div>
              <div class="hp-feature-text">
                <h2>Roommate matcher (demo)</h2>
                <p>See how AI could match you with compatible roommates.</p>
              </div>
            </div>

            <div class="hp-feature-card hp-feature-card-tight">
              <div class="hp-feature-icon-block">🔐</div>
              <div class="hp-feature-text">
                <h2>Deposit planner</h2>
                <p>Plan for deposits, fees, and move-in costs.</p>
              </div>
            </div>

            <div class="hp-feature-card hp-feature-card-tight">
              <div class="hp-feature-icon-block">🗺️</div>
              <div class="hp-feature-text">
                <h2>Relocation checklist</h2>
                <p>Stay organized through your move.</p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>

  <script>
  document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".hp-tab-button");
    const panels = {
      buyer: document.getElementById("tab-buyer"),
      investor: document.getElementById("tab-investor"),
      neighborhood: document.getElementById("tab-neighborhood"),
      repair: document.getElementById("tab-repair"),
      rent: document.getElementById("tab-rent"),
      renttools: document.getElementById("tab-renttools"),
    };

    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const target = btn.dataset.tab;

        buttons.forEach((b) => b.classList.remove("is-active"));
        btn.classList.add("is-active");

        Object.values(panels).forEach((p) =>
          p.classList.remove("is-active")
        );
        panels[target].classList.add("is-active");
      });
    });
  });
  </script>
</body>
</html>
"""

components.html(html, height=950, scrolling=True)






