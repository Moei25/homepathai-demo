import streamlit as st

st.set_page_config(page_title="First-Time Buyer Guide", layout="wide")

st.markdown("""
<div style='padding: 40px; background: linear-gradient(135deg, #0f92ce, #0d9fab, #14c5d9); 
            border-radius: 16px; color: white; box-shadow: 4px 12px rgba(0,0,0,0.15);'>
    <h1 style='font-size: 40px; font-weight: 700; margin-bottom: 10px;'>
        First-Time Buyer Hub
    </h1>
    <p style='font-size: 20px; opacity: 0.9;'>
        Tools, guidance, and AI insights designed to make your first home purchase simple and confident.
    </p>
</div>
<br>
""", unsafe_allow_html=True)

st.subheader("🧭 Getting Started")
st.write("What you need to know before buying your first home.")

st.subheader("💰 Budget & Affordability Tools")
st.write("AI-driven calculators to understand what you can comfortably afford.")

st.subheader("📄 Loan Programs")
st.write("Breakdown of FHA, VA, USDA, and first-time buyer programs.")
