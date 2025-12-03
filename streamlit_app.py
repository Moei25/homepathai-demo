import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="HomePathAI Demo",
    page_icon="🏠",
    layout="wide"
)

# ---------------- Sidebar ----------------
st.sidebar.title("HomePathAI")
st.sidebar.caption("AI assistant for buyers, renters, investors & agents.")
st.sidebar.markdown("### 🧭 Navigation")

st.sidebar.button("Buyer Hub")
st.sidebar.button("Investor Hub")
st.sidebar.button("Neighbor Hub")
st.sidebar.button("Rent & Moving")
st.sidebar.button("Repair Estimator")
st.sidebar.button("Agent Hub")
st.sidebar.button("Help / About")

# ---------------- HERO SECTION ----------------
hero_html = """
<div style="
    padding: 40px;
    background: linear-gradient(135deg, #0f92ce, #0d9fab, #14c5d9);
    border-radius: 16px;
    color: white;
    box-shadow: 4px 12px rgba(0,0,0,0.15);
">
    <h1 style="margin-bottom: 6px; font-size: 42px; font-weight: 700;">
        Smart search for your next home — powered by AI.
    </h1>

    <p style="opacity: 0.95; font-size: 20px;">
        Neighborhood insights, investor-grade numbers, repair tools, moving resources,
        and first-time buyer help — all in one experience built for real people.
    </p>

    <div style="margin-top: 20px;">

        <span style="padding:10px 18px; background:#15d2e9; border-radius:12px; margin-right:10px;">
            First-time buyer friendly
        </span>

        <span style="padding:10px 18px; background:#15d2e9; border-radius:12px; margin-right:10px;">
            Investor deal analysis
        </span>

        <span style="padding:10px 18px; background:#15d2e9; border-radius:12px; margin-right:10px;">
            Neighborhood insights
        </span>

        <span style="padding:10px 18px; background:#15d2e9; border-radius:12px; margin-right:10px;">
            Repair estimator
        </span>

        <span style="padding:10px 18px; background:#15d2e9; border-radius:12px; margin-right:10px;">
            Rent & moving tools
        </span>

    </div>
</div>
"""

st.html(hero_html)  # ← THIS forces proper rendering every time

# ---------------- SPACING ----------------
st.write("")
st.write("")

# ---------------- DEMO SECTIONS ----------------
st.subheader("🛠 Recommended Tools")
st.write("Use the navigation on the left to explore buyer tools, investor calculators, and neighborhood insights.")

st.subheader("📊 Quick Market Insight (Demo Data)")
demo_df = pd.DataFrame({
    "City": ["Detroit", "Grand Rapids", "Ann Arbor"],
    "Avg Price": [185000, 320000, 450000],
    "YoY Change": ["+7.4%", "+5.1%", "+6.8%"]
})
st.dataframe(demo_df, use_container_width=True)






