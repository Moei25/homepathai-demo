import streamlit as st

st.set_page_config(page_title="Repair Estimator", layout="wide")

st.markdown("""
<div style='padding: 40px; background: linear-gradient(135deg, #0f92ce, #0d9fab, #14c5d9);
            border-radius: 16px; color: white; box-shadow: 4px 12px rgba(0,0,0,0.15);'>
    <h1 style='font-size: 40px; font-weight: 700; margin-bottom: 10px;'>
        Repair Estimator
    </h1>
    <p style='font-size: 20px; opacity: 0.9;'>
        Estimate renovation and repair costs based on real data and comparable properties.
    </p>
</div>
<br>
""", unsafe_allow_html=True)

st.subheader("🛠 Repair Costs Breakdown")
st.write("Coming soon — AI-powered cost estimator.")
