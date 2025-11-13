
import streamlit as st

st.set_page_config(page_title="HomePathAI Demo", layout="wide")

st.title("🏡 HomePathAI – Live Demo (Phases 1–3)")
st.write("This is a functional placeholder demo showing:")
st.write("- Neighborhood Scoring (Phase 1)")
st.write("- Property Repair Estimator (Phase 2)")
st.write("- Homebuyer AI Assistant (Phase 3)")

st.subheader("Neighborhood Score (Mock)")
city = st.text_input("Enter a city")
if city:
    st.success(f"Mock score for {city}: 82/100")

st.subheader("Repair Estimator (Mock)")
uploaded = st.file_uploader("Upload a property image")
if uploaded:
    st.info("AI mock analysis: Estimated repairs: $18,500")

st.subheader("AI Homebuyer Assistant (Mock)")
question = st.text_input("Ask a homebuying question")
if question:
    st.write("AI Response (mock): This is where the assistant would reply.")
