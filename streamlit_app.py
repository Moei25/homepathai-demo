import streamlit as st

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(
    page_title="HomePathAI",
    layout="wide",
)

# ------------------------------------------------------------
# HERO CSS + GLOBAL STYLES
# ------------------------------------------------------------
st.markdown("""
<style>

body {
    font-family: 'Inter', sans-serif;
}

/* HERO SECTION */
.hero-section {
    position: relative;
    width: 100%;
    height: 420px;
    border-radius: 14px;
    overflow: hidden;
    margin-bottom: 35px;
    box-shadow: 0px 4px 16px rgba(0,0,0,0.15);
}

/* Background image (replace later with your uploaded logo assets) */
.hero-bg {
    background-image: url('https://images.unsplash.com/photo-1600585154526-990dced4db0d');
    background-size: cover;
    background-position: center;
    opacity: 0.30;
    position: absolute;
    inset: 0;
}

.hero-content {
    position: relative;
    z-index: 2;
    padding: 40px;
    color: #0A2A33;
}

.hero-title {
    font-size: 40px;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 10px;
}

.hero-subtitle {
    font-size: 18px;
    font-weight: 400;
    max-width: 650px;
    margin-bottom: 20px;
}

.hero-chip-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 20px;
}

.hero-chip {
    padding: 6px 14px;
    background: white;
    border-radius: 20px;
    font-size: 14px;
    border: 1px solid #dcdcdc;
    box-shadow: 0px 1px 3px rgba(0,0,0,0.1);
}

.hero-search-wrapper {
    margin-top: 8px;
}

.hero-search {
    width: 60%;
    padding: 14px 18px;
    border-radius: 10px;
    border: 1px solid #ccc;
    font-size: 16px;
}

/* FOOTER */
.hp-footer {
    text-align: left;
    margin-top: 20px;
    font-size: 14px;
}

.hp-tagline-1 {
    font-weight: 600;
    font-size: 18px;
    color: #06383A;
}

.hp-tagline-2 {
    color: #555;
    margin-left: 6px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# RENDER FOOTER FUNCTION
# ------------------------------------------------------------
def render_footer():
    st.markdown(
        """
        <div class="hp-footer">
            <span class="hp-tagline-1">For you</span>
            <span class="hp-tagline-2">Built to make your home buying simple.</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------------
# HOME PAGE
# ------------------------------------------------------------
def page_home():

    # HERO
    st.markdown(
        """
        <div class="hero-section">
            <div class="hero-bg"></div>
            <div class="hero-content">

                <div class="hero-title">
                    Rentals. Homes. Agents. Loans. <br/>All in one AI path.
                </div>

                <div class="hero-subtitle">
                    HomePathAI helps you compare neighborhoods, estimate repairs, and navigate buying or renting 
                    — with tools built for first-time buyers, investors, and renters.
                </div>

                <div class="hero-chip-row">
                    <div class="hero-chip">🏡 First-time homebuyer friendly</div>
                    <div class="hero-chip">📊 Investor-grade deal analysis</div>
                    <div class="hero-chip">🔍 Neighborhood insights</div>
                    <div class="hero-chip">💬 Agents • Lenders • Moving tools</div>
                </div>

                <div class="hero-search-wrapper">
                    <input class="hero-search" type="text" placeholder="Enter a city, neighborhood, or ZIP"/>
                </div>

            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---------------------------------------------------------
    # Trending Homes (Demo Section)
    # ---------------------------------------------------------
    st.markdown("### 🔥 Trending homes near you (demo)")

    col1, col2 = st.columns(2)

    with col1:
        st.image("https://images.unsplash.com/photo-1568605114967-8130f3a36994", use_container_width=True)
        st.markdown("""
        **$289,900**  
        3 bed • 2 bath • 1,540 sq ft  
        Detroit, MI  
        """)

    with col2:
        st.image("https://images.unsplash.com/photo-1572120360610-d971b9d7767c", use_container_width=True)
        st.markdown("""
        **$344,200**  
        4 bed • 2 bath • 1,890 sq ft  
        Grand Rapids, MI  
        """)

    # ---------------------------------------------------------
    # Neighborhood Snapshot (Demo)
    # ---------------------------------------------------------
    st.markdown("### 🏘️ Neighborhood snapshot (demo)")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Safety score", "7.8 / 10", "+0.3 vs avg")
    with c2:
        st.metric("School rating", "B+ tier", "")
    with c3:
        st.metric("Affordability", "Moderate", "")

    # FOR YOU SECTION
    st.markdown("### ❤️ For you today (demo feed)")
    st.write("""
    ⭐ **First-time buyer coach** – What lenders look for  
    🔧 **Repair estimator** – Upload a photo  
    📈 **Investor plays** – BRRRR / flips / rentals  
    🌎 **Relocation ideas** – Compare cities  
    """)

    render_footer()

# ------------------------------------------------------------
# BUYER HUB
# ------------------------------------------------------------
def page_buyer():
    st.title("🏡 Buyer Hub – First-Time & Repeat Buyers")

    tabs = st.tabs([
        "Smart Search",
        "First-Time Buyer Coach",
        "Repair Estimator (demo)",
        "Neighborhood Insights (demo)",
        "Mortgage & Affordability (demo)"
    ])

    with tabs[0]:
        st.subheader("Smart Search (demo)")

    with tabs[1]:
        st.subheader("First-time buyer coach (demo)")

    with tabs[2]:
        st.subheader("Repair Estimator (demo)")

    with tabs[3]:
        st.subheader("Neighborhood Insights (demo)")

    with tabs[4]:
        st.subheader("Mortgage tools (demo)")

# ------------------------------------------------------------
# RENTER HUB
# ------------------------------------------------------------
def page_renter():
    st.title("🏠 Renter Hub")

    tabs = st.tabs([
        "Find Rentals (demo)",
        "Section 8 Resources",
        "Moving Companies",
        "Affordability for Renters (demo)"
    ])

    with tabs[0]:
        st.write("Rental search tools (demo).")

    with tabs[1]:
        st.write("Section 8: eligibility, documentation, income calculations.")

    with tabs[2]:
        st.write("Top moving companies + instant quotes (demo).")

    with tabs[3]:
        st.write("Rent affordability calculator (demo).")

# ------------------------------------------------------------
# INVESTOR HUB
# ------------------------------------------------------------
def page_investor():
    st.title("📈 Investor Hub")

    tabs = st.tabs([
        "Deal Analyzer (demo)",
        "Skip Tracing (demo)",
        "Lead Scoring (demo)",
        "BRRRR Tools (demo)",
        "Flip Calculator (demo)"
    ])

    with tabs[0]:
        st.write("Investor deal analyzer mockup.")

    with tabs[1]:
        st.write("Skip tracing mockup.")

    with tabs[2]:
        st.write("Lead scoring (demo).")

    with tabs[3]:
        st.write("BRRRR calculator (demo).")

    with tabs[4]:
        st.write("Flip estimation tools (demo).")

# ------------------------------------------------------------
# PAGE ROUTING
# ------------------------------------------------------------
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Buyers", "Renters", "Investors"]
)

if menu == "Home":
    page_home()
elif menu == "Buyers":
    page_buyer()
elif menu == "Renters":
    page_renter()
elif menu == "Investors":
    page_investor()




