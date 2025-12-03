import streamlit as st
import pandas as pd
import numpy as np

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="HomePathAI Demo",
    page_icon="🏡",
    layout="wide",
)

# ==========================
# SIDEBAR NAVIGATION (Interactive)
# ==========================
st.sidebar.title("HomePathAI")
st.sidebar.caption("AI assistant for buyers, renters, investors & agents.")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "👤 Buyer Hub",
        "💰 Investor Hub",
        "📍 Neighborhood Hub",
        "🚚 Rent & Moving",
        "🛠️ Repair Estimator",
        "ℹ️ Help / About"
    ]
)

# ==========================
# HOME PAGE (Hero Section + Pills + Demo Table)
# ==========================
if page == "🏠 Home":

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
            Neighborhood insights, investor-grade numbers, repair tools,
            moving resources, and first-time buyer help – all in one experience.
        </p>

        <div style="margin-top: 20px;">
            <span style="padding:10px 18px; background:#15d2e9; border-radius:12px; margin-right:10px;">First-time buyer friendly</span>
            <span style="padding:10px 18px; background:#15d2e9; border-radius:12px; margin-right:10px;">Investor deal analysis</span>
            <span style="padding:10px 18px; background:#15d2e9; border-radius:12px; margin-right:10px;">Neighborhood insights</span>
            <span style="padding:10px 18px; background:#15d2e9; border-radius:12px; margin-right:10px;">Repair estimator</span>
            <span style="padding:10px 18px; background:#15d2e9; border-radius:12px; margin-right:10px;">Rent & moving tools</span>
        </div>
    </div>
    """

    st.markdown(hero_html, unsafe_allow_html=True)

    st.write("")
    st.subheader("⭐ Recommended Tools")
    st.write("Use the navigation to explore buyer tools, investor calculators, and neighborhood insights.")

    st.write("")
    st.subheader("📊 Quick Market Insight (Demo Data)")

    demo_df = pd.DataFrame({
        "City": ["Detroit", "Grand Rapids", "Ann Arbor"],
        "Avg Price": [185000, 320000, 450000],
        "YoY Change": ["+7.4%", "+5.1%", "+6.8%"],
    })
    st.dataframe(demo_df, use_container_width=True)

# ==========================
# BUYER HUB
# ==========================
elif page == "👤 Buyer Hub":
    st.title("Buyer Hub")
    st.write("Everything first-time buyers need (AI tools coming next).")

# ==========================
# INVESTOR HUB
# ==========================
elif page == "💰 Investor Hub":
    st.title("Investor Hub")
    st.write("Deal analyzer, ROI calculator, cap rates, rental estimates…")

# ==========================
# NEIGHBORHOOD HUB
# ==========================
elif page == "📍 Neighborhood Hub":
    st.title("Neighborhood Insights")
    st.write("Interactive maps & neighborhood scoring coming next.")

# ==========================
# RENT & MOVING
# ==========================
elif page == "🚚 Rent & Moving":
    st.title("Rent & Moving Tools")
    st.write("Rent calculator + moving company finder soon.")

# ==========================
# REPAIR ESTIMATOR
# ==========================
elif page == "🛠️ Repair Estimator":
    st.title("Repair Estimator")
    st.write("AI-powered repair cost estimator coming next.")

# ==========================
# HELP / ABOUT
# ==========================
elif page == "ℹ️ Help / About":
    st.title("About HomePathAI")
    st.write("Built for buyers, renters, investors & agents.")







