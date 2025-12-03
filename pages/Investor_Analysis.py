import streamlit as st

st.set_page_config(page_title="Investor Analysis", layout="wide")

st.markdown("""
<div style='padding: 40px; background: linear-gradient(135deg, #0f92ce, #0d9fab, #14c5d9);
            border-radius: 16px; color: white; box-shadow: 4px 12px rgba(0,0,0,0.15);'>
    <h1 style='font-size: 40px; font-weight: 700; margin-bottom: 10px;'>
        Investor Deal Analyzer
    </h1>
    <p style='font-size: 20px; opacity: 0.9;'>
        Analyze flips, rentals, BRRRR deals, and cash-flow opportunities using AI-powered real estate tools.
    </p>
</div>
<br>
""", unsafe_allow_html=True)

st.subheader("📊 Deal Metrics")
st.write("Cap rate, cash-on-cash, ARV, rehab costs, and more.")

st.subheader("🏘 Investment Strategies")
st.write("Compare long-term rentals, flips, mid-term rentals, and AirBnB.")

st.subheader("📈 Market Insights")
st.write("Neighborhood trends and investor-friendly zip codes.")
