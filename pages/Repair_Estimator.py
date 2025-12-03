import streamlit as st
st.set_page_config(page_title="Repair Estimator", layout="wide")
st.title("Repair estimator")
st.write("### Address")
st.write("123 Main St, Detroit, MI · Single-family")
sqft = st.number_input("Total square footage", value=1800)
st.write("### Estimated total repair cost: **$51,800**")
col1, col2 = st.columns(2)
with col1:
    st.write("## Repair costs breakdown")
    st.write("""
**Roof:** $9,500
**HVAC:** $7,800
**Kitchen:** $15,000
**Bathrooms:** $10,500
**Interior paint:** $3,500
**Landscaping:** $5,500
""")
with col2:
    st.write("## Comparable homes")
    st.write("""
**456 Maple Rd**, Detroit MI — **$240,000**, 1,750 sq ft
**28 Grand Ave**, Detroit MI — **$265,000**, 1,900 sq ft
**788 Elmwood Dr**, Detroit MI — **$230,000**, 1,850 sq ft
""")
