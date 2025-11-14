import streamlit as st

# ================== BASIC PAGE CONFIG ==================

st.set_page_config(
    page_title="HomePathAI – Smart Real Estate Assistant",
    layout="wide",
    page_icon="🏠",
)

# ================== GLOBAL STYLE ==================

APP_BG_IMAGE = (
    "https://images.unsplash.com/photo-1568605114967-8130f3a36994?auto=format&fit=crop&w=1600&q=80"
)

CUSTOM_CSS = f"""
<style>
/* Remove Streamlit default padding at the top */
.main .block-container {{
    padding-top: 1.4rem;
    padding-bottom: 3rem;
}}

/* Zillow-style hero header */
.hero-section {{
    position: relative;
    border-radius: 16px;
    overflow: hidden;
    margin-bottom: 1.75rem;
    color: #ffffff;
}}

.hero-bg {{
    background-image: url('{APP_BG_IMAGE}');
    background-size: cover;
    background-position: center;
    filter: brightness(0.55);
    position: absolute;
    inset: 0;
}}

.hero-content {{
    position: relative;
    padding: 2.5rem 2rem 2.25rem 2rem;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    z-index: 1;
}}

.hero-title {{
    font-size: 2.2rem;
    font-weight: 700;
    text-shadow: 0 2px 6px rgba(0,0,0,0.6);
}}

.hero-subtitle {{
    font-size: 0.98rem;
    opacity: 0.96;
}}

.hero-chip-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-top: 0.25rem;
}}

.hero-chip {{
    font-size: 0.78rem;
    padding: 0.25rem 0.65rem;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.35);
    background: rgba(0,0,0,0.25);
    backdrop-filter: blur(4px);
}}

.hero-search-wrapper {{
    margin-top: 0.9rem;
    max-width: 680px;
}}

.hero-search-label {{
    font-size: 0.82rem;
    margin-bottom: 0.15rem;
    opacity: 0.9;
}}

.hero-footer-row {{
    margin-top: 1.1rem;
    font-size: 0.8rem;
    opacity: 0.9;
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
}}

/* "Trending" cards */
.property-card {{
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #e6edf3;
    background: #ffffff;
    box-shadow: 0 6px 20px rgba(15, 23, 42, 0.04);
}}

.property-card img {{
    width: 100%;
    height: 180px;
    object-fit: cover;
}}

.property-body {{
    padding: 0.85rem 0.9rem 0.9rem 0.9rem;
    font-size: 0.86rem;
}}

.badge-pill {{
    display: inline-block;
    font-size: 0.7rem;
    padding: 0.18rem 0.5rem;
    border-radius: 999px;
    background: #0f766e15;
    color: #0f766e;
    margin-bottom: 0.12rem;
}}

.property-price {{
    font-size: 1.02rem;
    font-weight: 700;
    margin-bottom: 0.1rem;
}}

.property-meta {{
    color: #64748b;
    font-size: 0.8rem;
}}

.section-label {{
    font-size: 0.86rem;
    font-weight: 600;
    color: #0f172a;
    margin-bottom: 0.25rem;
}}

/* Footer / For you section */
.hp-footer {{
    margin-top: 2.7rem;
    padding-top: 0.9rem;
    border-top: 1px solid #e2e8f0;
    font-size: 0.83rem;
    color: #64748b;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 0.4rem;
}}

.hp-footer span.hp-tagline-1 {{
    font-weight: 600;
    color: #0f172a;
}}

.hp-footer span.hp-tagline-2 {{
    font-weight: 500;
    color: #0f766e;
}}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ================== MOCK DATA HELPERS ==================


def get_trending_properties(city: str | None = None):
    # Simple hard-coded examples; in the real app this comes from APIs.
    base = [
        {
            "title": "Modern Bungalow in East Side",
            "city": "Detroit, MI",
            "price": "$289,000",
            "beds": "3",
            "baths": "2",
            "sqft": "1,540",
            "badge": "Trending",
            "image": "https://images.unsplash.com/photo-1600607687920-4e2a534e87f2?auto=format&fit=crop&w=900&q=80",
        },
        {
            "title": "Updated Craftsman Near Downtown",
            "city": "Grand Rapids, MI",
            "price": "$344,900",
            "beds": "4",
            "baths": "2",
            "sqft": "1,980",
            "badge": "Hot this week",
            "image": "https://images.unsplash.com/photo-1568605114967-8130f3a36994?auto=format&fit=crop&w=900&q=80",
        },
        {
            "title": "Starter Home with Big Backyard",
            "city": "Warren, MI",
            "price": "$215,000",
            "beds": "2",
            "baths": "1",
            "sqft": "1,120",
            "badge": "Great for first-time buyers",
            "image": "https://images.unsplash.com/photo-1600585154340-0ef3c08c0632?auto=format&fit=crop&w=900&q=80",
        },
    ]
    if not city:
        return base
    city_lower = city.lower()
    return [p for p in base if city_lower in p["city"].lower()] or base


# ================== PAGE SECTIONS ==================


def render_footer():
    st.markdown(
        """
<div class="hp-footer">
  <span class="hp-tagline-1">For you</span>
  <span class="hp-tagline-2">Built to make your home buying simple.</span>
</div>
""",
        unsafe_allow_html=True,
    )


# ---------- HOME / HERO ----------


def page_home():
    # HERO
    st.markdown(
        """
<div class="hero-section">
  <div class="hero-bg"></div>
  <div class="hero-content">

    <div class="hero-title">Rentals. Homes. Agents. Loans. <br/>All in one AI path.</div>

    <div class="hero-subtitle">
      HomePathAI helps you compare neighborhoods, estimate repairs, and navigate buying or renting
      — with tools built for first-time buyers, investors, and renters.
    </div>

    <div class="hero-chip-row">
      <div class="hero-chip">🏡 First-time homebuyer friendly</div>
      <div class="hero-chip">📊 Investor-grade deal analysis</div>
      <div class="hero-chip">📍 Neighborhood safety & schools</div>
      <div class="hero-chip">🤝 Lenders · Agents · Moving tools</div>
    </div>

    <div class="hero-search-wrapper">
      <div class="hero-search-label">Address, neighborhood, city, or ZIP</div>
    </div>

    <div class="hero-footer-row">
      <span>⭐ Personalized “For you” feed based on your goals.</span>
      <span>🔐 Credit-safe: we only show what lenders may ask for.</span>
    </div>

  </div>
</div>
""",
        unsafe_allow_html=True,
    )

    # The actual Streamlit text_input for the search bar:
    search_query = st.text_input("", placeholder="Try “Detroit, MI” or a ZIP code", key="home_search")

    if search_query:
        st.success(f"Showing sample results for **{search_query}** (demo mode).")

    # TRENDING HOMES SECTION
    st.markdown("### 🔥 Trending homes near you (demo)")
    st.caption("Viewed and saved the most in your area in the last 24 hours (mock data).")

    props = get_trending_properties(search_query)
    cols = st.columns(3)
    for col, p in zip(cols, props):
        with col:
            st.markdown(
                f"""
<div class="property-card">
  <img src="{p['image']}" alt="Home photo" />
  <div class="property-body">
    <div class="badge-pill">{p['badge']}</div>
    <div class="property-price">{p['price']}</div>
    <div class="property-meta">{p['beds']} bd · {p['baths']} ba · {p['sqft']} sq ft</div>
    <div style="margin-top:0.12rem; font-weight:600;">{p['title']}</div>
    <div style="color:#64748b; font-size:0.8rem;">{p['city']}</div>
  </div>
</div>
""",
                unsafe_allow_html=True,
            )

    st.markdown("### 🧭 Neighborhood snapshot (demo)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Safety score (demo)", "7.8 / 10", "+0.3 vs city avg")
        st.caption("Based on crime trends and daytime activity (sample only).")
    with col2:
        st.metric("School rating (demo)", "B+ tier", "3 nearby schools")
        st.caption("Pulled from public school rating data (placeholder).")
    with col3:
        st.metric("Affordability (demo)", "Moderate", "Est. 31% income → housing")
        st.caption("Estimate based on typical mortgage & taxes (demo).")

    st.markdown("### 🎯 For you today (demo feed)")
    st.write(
        """
- 🧑‍💼 **First-time buyer coach** – Learn what lenders look at before you apply.
- 🛠 **Repair estimator** – Upload a property photo to get a ballpark rehab range.
- 💼 **Investor plays** – Quick filters for BRRRR, flips, and long-term rentals.
- 🏘 **Relocation ideas** – Compare neighborhoods by safety, schools, and walkability.
"""
    )

    render_footer()


# ---------- BUYER HUB ----------


def page_buyer():
    st.title("🏡 Buyer Hub – First-Time & Repeat Buyers")

    tabs = st.tabs(
        [
            "Smart Search",
            "First-Time Buyer Coach",
            "Repair Estimator (demo)",
            "Neighborhood Insights (demo)",
            "Mortgage & Affordability (demo)",
        ]
    )

    # --- SMART SEARCH ---
    with tabs[0]:
        st.subheader("Smart Property Search (demo)")
        col1, col2, col3 = st.columns(3)
        with col1:
            location = st.text_input("City, neighborhood, or ZIP", "Detroit, MI", key="buyer_city")
        with col2:
            price_range = st.selectbox("Price range (demo)", ["Any", "< $200k", "$200k – $400k", "$400k – $700k", "$700k+"])
        with col3:
            beds = st.selectbox("Beds (demo)", ["Any", "1+", "2+", "3+", "4+"])

        if st.button("Search sample listings", key="buyer_search_btn"):
            st.success(
                f"Showing **mock** listings for **{location}** "
                f"with filters: **{price_range}**, **{beds} beds**."
            )
            props = get_trending_properties(location)
            for p in props:
                with st.expander(f"{p['price']} · {p['title']} · {p['city']}"):
                    st.write(f"- Beds/Baths: **{p['beds']} / {p['baths']}**")
                    st.write(f"- Sq ft: **{p['sqft']}**")
                    st.write("- Est. monthly payment (demo): **$1,650/mo**")
                    st.write("- Est. taxes & insurance (demo): **$350/mo**")

    # --- FIRST-TIME BUYER COACH ---
    with tabs[1]:
        st.subheader("First-Time Homebuyer Coach (demo)")
        stage = st.radio(
            "Where are you in the process?",
            [
                "Just starting – learning how it works",
                "Figuring out my budget & credit",
                "Actively looking at homes",
                "Ready to make an offer soon",
            ],
        )
        st.write("### Your coaching tips (demo)")

        if stage.startswith("Just starting"):
            st.write(
                """
1. **Get a soft-pull pre-check** (no hard credit hit) so you know your ballpark budget.  
2. **List your monthly debts** – car, cards, loans – lenders care about your DTI ratio.  
3. **Save for more than just down payment** – inspections, appraisal, closing costs.
"""
            )
        elif "budget" in stage:
            st.write(
                """
- Aim for **housing ≤ 33%** of your gross monthly income (demo rule of thumb).  
- Pay down **high-interest cards first** – this often boosts your score the fastest.  
- Avoid new auto loans or big credit moves 3–6 months before applying.
"""
            )
        elif "looking" in stage:
            st.write(
                """
- Get a **pre-approval letter** so sellers take your offers seriously.  
- Walk the **neighborhood at night** and on weekends if you can.  
- Use our repair estimator (demo) to spot budget-killers before you fall in love.
"""
            )
        else:
            st.write(
                """
- Stay under the **max** the lender gave you – leave room for surprises.  
- Ask your agent for a **buyers net sheet** showing your estimated cash to close.  
- Don't waive **critical inspections** unless you're fully aware of the risks.
"""
            )

    # --- REPAIR ESTIMATOR ---
    with tabs[2]:
        st.subheader("Property Repair Estimator (demo)")
        img = st.file_uploader("Upload a photo of the property (front, kitchen, or bath)", type=["jpg", "jpeg", "png"])
        level = st.selectbox(
            "Condition (your best guess, demo)",
            ["Light cosmetic", "Average", "Heavy rehab", "Full gut"],
        )

        if img:
            st.image(img, caption="Uploaded image (demo only)", use_column_width=True)

        if st.button("Run mock repair estimate", key="repair_btn"):
            if level == "Light cosmetic":
                st.success("Estimated repairs (demo): **$8,000 – $18,000**")
            elif level == "Average":
                st.success("Estimated repairs (demo): **$18,000 – $35,000**")
            elif level == "Heavy rehab":
                st.success("Estimated repairs (demo): **$35,000 – $70,000**")
            else:
                st.success("Estimated repairs (demo): **$70,000+**")

            st.caption("Real version would read photos + comps and pull cost data per region.")

    # --- NEIGHBORHOOD INSIGHTS ---
    with tabs[3]:
        st.subheader("Neighborhood Insights (demo)")
        city = st.text_input("City or neighborhood", "Detroit, MI", key="nb_city")
        if st.button("Generate mock neighborhood snapshot", key="nb_btn"):
            st.write(f"### Snapshot for **{city}** (demo only)")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Safety trend", "Improving", "+4% vs last year (demo)")
            with col2:
                st.metric("Family-friendliness", "High", "Parks & schools nearby")
            with col3:
                st.metric("Walkability", "Car dependent", "Some errands require a car")
            st.write(
                """
**What this would include in the real app:**

- Crime heatmaps and trend lines  
- School ratings and enrollment data  
- Commute times to your job or preferred areas  
- Internet speeds and local amenities
"""
            )

    # --- MORTGAGE & AFFORDABILITY ---
    with tabs[4]:
        st.subheader("Mortgage & Affordability (demo)")
        col1, col2, col3 = st.columns(3)
        with col1:
            home_price = st.number_input("Home price", 50000, 1500000, 300000, step=5000)
        with col2:
            down = st.number_input("Down payment (%)", 0, 100, 5)
        with col3:
            rate = st.number_input("Interest rate (%)", 1.0, 15.0, 6.5, step=0.1)

        if st.button("Estimate monthly payment (demo)", key="mtg_btn"):
            loan_amount = home_price * (1 - down / 100)
            # extremely simplified demo calculation (not real amortization)
            monthly = loan_amount * (rate / 100) / 12 + 300
            st.success(f"Estimated monthly payment (demo): **${monthly:,.0f} / mo**")
            st.caption("Includes rough taxes/insurance placeholder. Real app would use lender APIs.")

    render_footer()


# ---------- RENTER TOOLS ----------


def page_renter():
    st.title("🏘 Renter Hub – Smarter Renting & Moving Tools")

    tabs = st.tabs(
        [
            "Rental Finder (demo)",
            "Section 8 & Assistance (info demo)",
            "Moving & Utilities (demo)",
            "Rent Budget Helper (demo)",
        ]
    )

    # RENTAL FINDER
    with tabs[0]:
        st.subheader("Rental Finder (demo)")
        col1, col2, col3 = st.columns(3)
        with col1:
            city = st.text_input("City or ZIP", "Detroit, MI", key="rent_city")
        with col2:
            max_rent = st.number_input("Max monthly rent", 300, 6000, 1800, step=50)
        with col3:
            beds = st.selectbox("Beds", ["Any", "Studio", "1+", "2+", "3+"])

        if st.button("Show sample rentals", key="rent_btn"):
            st.success(f"Showing mock rentals under **${max_rent}** in **{city}** with **{beds} beds**.")
            st.write(
                """
- 2 bd · Midtown loft – **$1,550/mo** – walkable to groceries & QLine  
- 3 bd · East side bungalow – **$1,350/mo** – fenced yard, pets allowed  
- 1 bd · Downtown high-rise – **$1,750/mo** – parking + gym
"""
            )

    # SECTION 8 INFO
    with tabs[1]:
        st.subheader("Section 8 & Rental Assistance (info demo)")
        st.write(
            """
**HomePathAI won’t approve or deny anyone**, but we can coach renters on:

- Where to find **local Housing Choice Voucher (Section 8)** offices  
- What documents landlords usually ask for  
- How to spot **scams** and protect your information  
- Questions to ask about inspections, timelines, and waitlists
"""
        )
        st.info(
            "In the real product, this tab would show a map of local housing authorities, "
            "intake checklists, and a safe way to organize documents."
        )

    # MOVING & UTILITIES
    with tabs[2]:
        st.subheader("Moving & Set-Up (demo)")
        city = st.text_input("Where are you moving to?", "Detroit, MI", key="move_city")
        if st.button("Show mock moving helpers", key="move_btn"):
            st.write(
                f"""
### Moving helpers for **{city}** (demo)

- 🚚 Shortlist of **moving companies** (with reviews & pricing ranges)  
- 🔌 Utilities checklist – power, gas, water, trash, internet providers  
- 🗓 Move-in timeline – reminders 60 / 30 / 7 days before your move
"""
            )

    # RENT BUDGET
    with tabs[3]:
        st.subheader("Rent Budget Helper (demo)")
        income = st.number_input("Monthly take-home income ($)", 500, 20000, 4000, step=100)
        percent = st.slider("Max % of income toward rent (rule of thumb)", 20, 40, 30)
        if st.button("Calculate target rent", key="rent_budget_btn"):
            target = income * percent / 100
            st.success(f"Suggested max rent (demo): **${target:,.0f} / mo**")
            st.caption("Real app could sync with your bank/credit data securely via partners.")

    render_footer()


# ---------- INVESTOR HUB ----------


def page_investor():
    st.title("💼 Investor Hub – Flips, BRRRR, and Rentals")

    tabs = st.tabs(
        [
            "Quick Deal Analyzer (demo)",
            "ARV & Rehab (demo)",
            "Lead Scoring & Skip Tracing (demo)",
            "Portfolio Snapshot (demo)",
        ]
    )

    # QUICK DEAL ANALYZER
    with tabs[0]:
        st.subheader("Quick Deal Analyzer (demo)")
        col1, col2, col3 = st.columns(3)
        with col1:
            arv = st.number_input("After-repair value (ARV)", 50000, 2000000, 260000, step=5000)
        with col2:
            purchase = st.number_input("Purchase price", 30000, 2000000, 140000, step=5000)
        with col3:
            rehab = st.number_input("Estimated rehab cost", 0, 1000000, 45000, step=5000)

        holding_months = st.slider("Holding period (months)", 1, 24, 6)
        if st.button("Analyze flip deal (demo)", key="deal_btn"):
            total_basis = purchase + rehab + holding_months * 1200  # toy holding cost model
            profit = arv - total_basis
            margin = profit / arv * 100
            st.write("### Deal snapshot (demo)")
            st.metric("Projected profit (demo)", f"${profit:,.0f}")
            st.metric("Margin on ARV (demo)", f"{margin:,.1f}%")
            st.caption("Real version would factor in closing costs, agent fees, & financing terms.")

    # ARV & REHAB
    with tabs[1]:
        st.subheader("ARV & Rehab Estimator (demo)")
        col1, col2 = st.columns(2)
        with col1:
            subject_sqft = st.number_input("Subject property sq ft", 400, 10000, 1600, step=100)
            comp_price = st.number_input("Average comp sale price", 50000, 2000000, 240000, step=5000)
        with col2:
            comp_sqft = st.number_input("Average comp sq ft", 400, 10000, 1700, step=100)
            rehab_level = st.selectbox(
                "Rehab level (demo)",
                ["Light", "Medium", "Heavy"],
            )
        if st.button("Estimate ARV & rehab", key="arv_btn"):
            arv_est = comp_price * (subject_sqft / comp_sqft)
            if rehab_level == "Light":
                rehab_est = 15000
            elif rehab_level == "Medium":
                rehab_est = 40000
            else:
                rehab_est = 75000
            st.success(
                f"Estimated ARV (demo): **${arv_est:,.0f}**  ·  "
                f"Estimated rehab (demo): **${rehab_est:,.0f}**"
            )
            st.caption("Real engine would use MLS, contractor pricing, and computer vision on photos.")

    # LEAD SCORING & SKIP TRACING (MOCK)
    with tabs[2]:
        st.subheader("Lead Scoring & Skip Tracing (demo)")
        st.write(
            """
Paste a list of addresses or upload CSV (in the full product).  
Here we just show how a **mock scoring** flow could look.
"""
        )
        sample_leads = st.text_area(
            "Sample leads (one per line, demo)",
            "123 Main St, Detroit, MI 48202\n"
            "456 Oak Ave, Warren, MI 48088\n"
            "789 Maple Dr, Grand Rapids, MI 49503",
            height=120,
        )

        if st.button("Score leads (demo only)", key="score_btn"):
            st.info("Scoring leads based on equity, distress signals, and time-in-ownership (mock).")
            lines = [l.strip() for l in sample_leads.splitlines() if l.strip()]
            for i, line in enumerate(lines, start=1):
                if i == 1:
                    score = "🔥 High – vacancy + equity signals"
                elif i == 2:
                    score = "🟡 Medium – some motivation, follow up"
                else:
                    score = "🟢 Low – nurture in long-term list"
                st.write(f"- **{line}** → {score}")

            st.caption("Real version would connect to skip-tracing & property data providers via API.")

    # PORTFOLIO SNAPSHOT
    with tabs[3]:
        st.subheader("Portfolio Snapshot (demo)")
        st.write(
            """
This is a placeholder for a simple portfolio dashboard:

- Total doors, average cash-on-cash return  
- Vacancy, delinquency, & upcoming lease renewals  
- Refi opportunities based on rates & equity
"""
        )
        st.metric("Sample doors (demo)", "7", "+2 acquired this year")
        st.metric("Est. portfolio value (demo)", "$1.9M", "+$160k vs last year")
        st.metric("Avg. cash-on-cash (demo)", "11.3%", "+1.2 pts YoY")

    render_footer()


# ================== SIDEBAR NAV ==================


def main():
    st.sidebar.title("HomePathAI")
    nav = st.sidebar.radio(
        "Navigate",
        ["Home", "Buyer Hub", "Renter Hub", "Investor Hub"],
        index=0,
    )

    # Later, when you upload your logo to the repo, you can add:
    # st.sidebar.image("homepathai_logo.png", width=160)

    if nav == "Home":
        page_home()
    elif nav == "Buyer Hub":
        page_buyer()
    elif nav == "Renter Hub":
        page_renter()
    elif nav == "Investor Hub":
        page_investor()


if __name__ == "__main__":
    main()



