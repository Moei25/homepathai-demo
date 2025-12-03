import streamlit as st

st.set_page_config(page_title="Neighborhood Insights", layout="wide")

st.markdown("""
<div style='padding: 40px; background: linear-gradient(135deg, #0f92ce, #0d9fab, #14c5d9);
            border-radius: 16px; color: white; box-shadow: 4px 12px rgba(0,0,0,0.15);'>
    <h1 style='font-size: 40px; font-weight: 700; margin-bottom: 10px;'>
        Neighborhood Insights
    </h1>
    <p style='font-size: 20px; opacity: 0.9;'>
        Explore neighborhood safety, pricing trends, walkability, schools, heatmaps, and lifestyle fit.
    </p>
</div>
<br>
""", unsafe_allow_html=True)

st.subheader("📍 Heatmaps")
st.write("Crime, price growth, and school scoring heatmaps.")

st.subheader("📌 Compare Neighborhoods")
st.write("Side-by-side AI comparison of any two cities or areas.")
