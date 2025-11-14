import streamlit as st

# ================== PAGE CONFIG ==================

st.set_page_config(
    page_title="HomePathAI – Smart Real Estate Assistant",
    layout="wide",
    page_icon="🏠",
)

# ================== GLOBAL STYLES (CSS) ==================

APP_BG_IMAGE = "https://images.unsplash.com/photo-1568605114967-8130f3a36994?auto=format&fit=crop&w=1600&q=80"

CUSTOM_CSS = f"""
<style>
.main .block-container {{
    padding-top: 1.2rem;
    padding-bottom: 3rem;
}}

h1, h2, h3, h4 {{
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}}

body {{
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}}

/* HERO */
.hero-section {{
    position: relative;
    border-radius: 16px;
    overflow: hidden;
    margin-bottom: 1.8rem;
    color: #ffffff;
    box-shadow: 0 10px 30px rgba(15,23,42,0.35);
}}

.hero-bg {{
    position: absolute;
    inset: 0;
    background-image: url('{APP_BG_IMAGE}');
    background-size: cover;
    background-position: center;
    filter: brightness(0.55);
}}

.hero-content {{
    position: relative;
    padding: 2.4rem 2.2rem 2.1rem 2.2rem;
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
    z-index: 1;
}}

.hero-title {{
    font-size: 2.4rem;
    font-weight: 750;
    line-height: 1.15;
    text-shadow: 0 2px 10px rgba(0,0,0,0.7);
}}

.hero-subtitle {{
    font-size: 0.98rem;
    opacity: 0.96;
    max-width: 640px;
}}

.hero-chip-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-top: 0.2rem;
}}

.hero-chip {{
    font-size: 0.78rem;
    padding: 0.25rem 0.7rem;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.5);
    background: rgba(15,23,42,0.55);
    backdrop-filter: blur(4px);
}}

.hero-search-wrapper {{
    margin-top: 0.8rem;
    max-width: 620px;
}}

.hero-footer-row {{
    margin-top: 0.9rem;
    font-size: 0.8rem;
    opacity: 0.9;
    display: flex;
    flex-wrap: wrap;
    gap: 0.7rem;
}}

/* PROPERTY CARDS */
.property-card {{
    border-radius: 14px;
    border: 1px solid #e2e8f0;
    background: #ffffff;
    box-shadow: 0 10px 30px rgba(15,23,42,0.04);
    overflow: hidden;
    margin-bottom: 0.9rem;
}}

.property-card img {{
    width: 100%;
    height: 180px;
    object-fit: cover;
}}

.property-body {{
    padding: 0.85rem 0.95rem 0.9rem 0.95rem;
    font-size: 0.86rem;
}}

.badge-pill {{
    display: inline-block;
    font-size: 0.7rem;
    padding: 0.16rem 0.55rem;
    border-radius: 999px;
    background: #0f766e1a;
    color: #0f766e;
    margin-bottom: 0.15rem;
}}

.property-price {{
    font-size: 1.02rem;
    font-weight: 700;
    margin-bottom: 0.05rem;
}}

.property-meta {{
    color: #64748b;
    font-size: 0.8rem;
}}

/* FOOTER */
.hp-footer {{
    margin-top: 2.5rem;
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

# ================== HELPERS ==================


def get_trending_properties(city=None):
    props = [
        {
            "title": "Modern Bungalow on the East Side",
            "city": "Detroit, MI",
            "price": "$289,000",
            "beds": "3",
            "baths": "2",
            "sqft": "1,540",
            "badge": "Trending",
            "image": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?auto=format&fit=crop&w=900&q=80",
        },
        {
            "title": "Renovated Craftsman Near Downtown",
            "city": "Grand Rapids, MI",
            "price": "$344,900",
            "beds": "4",
            "baths": "2",
            "sqft": "1,920",
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
        return props
    city_l = city.lower()
    filtered = [p for p in props if city_l in p["city"].lower()]
    return filtered or props


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

# ================== PAGES ==================

# ---------- HOME PAGE ----------


def page_home():
    # HERO
    st.markdown(
        """
        <div class="hero-section">
            <div class="hero-bg"></div>
            <div class="hero-content">

                <div class="hero-title">
                    Smarter home search. <br/>Powered by AI.
                </div>

                <div class="hero-subtitle">
                    HomePathAI helps you compare neighborhoods, estimate repairs,
                    and navigate buying or renting — with tools built for first-time buyers,
                    investors, and renters.
                </div>

                <div class="hero-chip-row">
                    <div class="hero-chip">🏡 First-time buyer friendly</div>
                    <div class="hero-chip">📊 Investor deal analysis</div>
                    <div class="hero-chip">📍 Neighborhood insights</div>
                    <div class="hero-chip">🔧 Repair estimator</div>
                    <div class="hero-chip">🚚 Rent & moving tools</div>
                </div>

            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Search bar (real Streamlit input)
    search_query = st.text_input(
        "Search city, neighborhood, or ZIP",
        placeholder="Try “Detroit, MI” or a ZIP code",
    )
    if search_query:
        st.caption(f"Showing demo content based on: **{search_query}**")

    # Trending homes
    st.markdown("### 🔥 Trending homes near you (demo)")
    st.caption("Most-viewed homes in your area over the last 24 hours (mock data).")

    props = get_trending_properties(search_query)
    c1, c2, c3 = st.columns(3)
    for col, p in zip([c1, c2, c3], props):
        with col:
            st.markdown(
                f"""
                <div class="property-card">
                    <img src="{p['image']}" alt="Home photo"/>
                    <div class="property-body">
                        <div class="badge-pill">{p['badge']}</div>
                        <div class="property-price">{p['price']}</div>
                        <div class="property-meta">{p['beds']} bd · {p['baths']} ba · {p['sqft']} sq ft</div>
                        <div style="margin-top:0.08rem; font-weight:600;">{p['title']}</div>
                        <div style="color:#64748b; font-size:0.8rem;">{p['city']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Neighborhood snapshot
    st.markdown("### 🧭 Neighborhood snapshot (demo)")
    nc1, nc2, nc3 = st.columns(3)
    with nc1:
        st.metric("Safety score (demo)", "7.8 / 10", "+0.3 vs city avg")
    with nc2:
        st.metric("School rating (demo)", "B+ tier", "3 nearby schools")
    with nc3:
        st.metric("Affordability (demo)", "Moderate", "Est. 31% income → housing")

    # For you feed
    st.markdown("### 🎯 For you today (demo feed)")
    st.write(
        """
- 🧑‍💼 **First-time buyer coach** – See what lenders look at before you apply.  
- 🛠 **Repair estimator** – Upload photos and get a ballpark rehab range (future feature).  
- 📈 **Investor plays** – Quick filters for BRRRR, flips, and long-term rentals.  
- 🌎 **Relocation ideas** – Compare “Detroit vs Grand Rapids for families” and more.  
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

    # TAB 1 – SMART SEARCH
    with tabs[0]:
        st.subheader("🔍 Smart Search (demo)")
        city = st.text_input("City, neighborhood, or ZIP", "Detroit, MI", key="buyer_city")
        price_range = st.selectbox(
            "Price range (demo)",
            ["Any", "< $200k", "$200k – $400k", "$400k – $700k", "$700k+"],
        )
        beds = st.selectbox("Beds (demo)", ["Any", "1+", "2+", "3+", "4+"])
        if st.button("Search sample listings", key="buyer_search_btn"):
            st.success(
                f"Showing **mock** listings for **{city}** with **{price_range}**, **{beds} beds**."
            )
            demo = get_trending_properties(city)
            for p in demo:
                with st.expander(f"{p['price']} · {p['title']} · {p['city']}"):
                    st.write(f"- Beds/Baths: **{p['beds']} / {p['baths']}**")
                    st.write(f"- Sq ft: **{p['sqft']}**")
                    st.write("- Est. payment (demo): **$1,650 / mo**")

    # TAB 2 – FIRST-TIME BUYER COACH
    with tabs[1]:
        st.subheader("🧭 First-Time Buyer Coach (demo)")
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
        if stage.startswith("Just"):
            st.write(
                """
1. Pull a **soft credit check** (no hard hit) to get your ballpark score.  
2. List your **monthly debts** – cards, car, loans – lenders care about your DTI.  
3. Start saving for **inspection, appraisal, and closing costs**, not just down payment.  
"""
            )
        elif "budget" in stage:
            st.write(
                """
- Aim for housing costs under **33%** of your gross monthly income (rule of thumb).  
- Pay down **high-interest cards first** – often fastest way to bump your score.  
- Avoid new loans 3–6 months before applying (car, furniture, etc.).  
"""
            )
        elif "looking" in stage:
            st.write(
                """
- Get a **pre-approval letter** so sellers take you seriously.  
- Visit the neighborhood at **different times of day**.  
- Use a repair estimate to avoid budget-killer surprises later.  
"""
            )
        else:
            st.write(
                """
- Don’t feel pressured to offer at the **maximum** your lender approves.  
- Ask for a **buyer net sheet** showing estimated cash to close.  
- Keep a small **emergency buffer** after closing.  
"""
            )

    # TAB 3 – REPAIR ESTIMATOR
    with tabs[2]:
        st.subheader("🛠 Repair Estimator (demo)")
        img = st.file_uploader("Upload a property photo (front, kitchen, or bath)", type=["png", "jpg", "jpeg"])
        condition = st.selectbox(
            "Condition (your best guess, demo)",
            ["Light cosmetic", "Average", "Heavy rehab", "Full gut / major"],
        )
        if img:
            st.image(img, use_column_width=True, caption="Uploaded image (demo only)")
        if st.button("Run mock repair estimate", key="repair_btn"):
            if condition == "Light cosmetic":
                est = "$8,000 – $18,000"
            elif condition == "Average":
                est = "$18,000 – $35,000"
            elif condition == "Heavy rehab":
                est = "$35,000 – $70,000"
            else:
                est = "$70,000+"
            st.success(f"Estimated repairs (demo): **{est}**")
            st.caption("Real version will use computer vision + regional cost data.")

    # TAB 4 – NEIGHBORHOOD INSIGHTS
    with tabs[3]:
        st.subheader("📍 Neighborhood Insights (demo)")
        city = st.text_input("City or neighborhood", "Detroit, MI", key="nb_city")
        if st.button("Generate mock snapshot", key="nb_btn"):
            st.write(f"### Snapshot for **{city}** (demo only)")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Safety trend", "Improving", "+4% vs last year (demo)")
            with c2:
                st.metric("Family-friendliness", "High", "Parks & schools nearby")
            with c3:
                st.metric("Walkability", "Car dependent", "Some errands require a car")
            st.write(
                """
Real product will include:  
- Crime heatmaps and trend lines  
- School ratings and enrollment data  
- Commute times to work or key places  
- Internet speeds & local amenities  
"""
            )

    # TAB 5 – MORTGAGE & AFFORDABILITY
    with tabs[4]:
        st.subheader("💰 Mortgage & Affordability (demo)")
        c1, c2, c3 = st.columns(3)
        with c1:
            price = st.number_input("Home price ($)", 50000, 2000000, 300000, step=5000)
        with c2:
            down_pct = st.number_input("Down payment (%)", 0, 100, 5)
        with c3:
            rate = st.number_input("Interest rate (%)", 1.0, 15.0, 6.5)
        years = st.selectbox("Loan term (years)", [15, 20, 30], index=2)

        if st.button("Estimate monthly payment (demo)", key="mtg_btn"):
            loan = price * (1 - down_pct / 100)
            m_rate = rate / 100 / 12
            n = years * 12
            if m_rate > 0:
                payment = loan * (m_rate * (1 + m_rate) ** n) / ((1 + m_rate) ** n - 1)
            else:
                payment = loan / n
            st.success(f"Estimated principal & interest (demo): **${payment:,.0f} / mo**")
            st.caption("Real app will also estimate taxes, insurance, and HOA.")

    render_footer()

# ---------- RENTER HUB ----------


def page_renter():
    st.title("🏘 Renter Hub – Smarter Renting & Moving")

    tabs = st.tabs(
        [
            "Rental Finder (demo)",
            "Section 8 & Assistance (info demo)",
            "Moving & Setup (demo)",
            "Rent Budget Helper (demo)",
        ]
    )

    # TAB 1 – RENTAL FINDER
    with tabs[0]:
        st.subheader("🔎 Rental Finder (demo)")
        city = st.text_input("City or ZIP", "Detroit, MI", key="rent_city")
        max_rent = st.number_input("Max monthly rent ($)", 300, 6000, 1800, step=50)
        beds = st.selectbox("Beds", ["Any", "Studio", "1+", "2+", "3+"])
        if st.button("Show sample rentals", key="rent_btn"):
            st.success(f"Showing mock rentals under **${max_rent}** in **{city}** with **{beds} beds**.")
            st.write(
                """
- 2 bd • Midtown loft – **$1,550/mo** – walkable to groceries & transit  
- 3 bd • East side bungalow – **$1,350/mo** – fenced yard, pets allowed  
- 1 bd • Downtown high-rise – **$1,750/mo** – parking + gym  
"""
            )

    # TAB 2 – SECTION 8 & ASSISTANCE
    with tabs[1]:
        st.subheader("🏛 Section 8 & Rental Assistance (demo)")
        st.write(
            """
HomePathAI does **not** approve or deny assistance.  
But it can coach renters on:

- Where to find local **Housing Choice Voucher (Section 8)** offices  
- What documents landlords usually ask for  
- How inspections, vouchers, and move-in timing work  
- How to spot **scams** and protect your info  

Real version will show local housing authorities, links, and checklists.
"""
        )

    # TAB 3 – MOVING & SETUP
    with tabs[2]:
        st.subheader("🚚 Moving & Setup (demo)")
        city = st.text_input("Where are you moving to?", "Detroit, MI", key="move_city")
        if st.button("Show mock helpers", key="move_btn"):
            st.write(
                f"""
### Moving helpers for **{city}** (demo)

- Shortlist of movers with sample price ranges  
- Utility checklist – power, gas, water, internet providers  
- Suggested move-in timeline (60 / 30 / 7 days)  
"""
            )

    # TAB 4 – RENT BUDGET HELPER
    with tabs[3]:
        st.subheader("💸 Rent Budget Helper (demo)")
        income = st.number_input("Monthly take-home income ($)", 500, 20000, 4000, step=100)
        pct = st.slider("Max % of income toward rent", 20, 45, 30)
        if st.button("Calculate target rent", key="rent_budget_btn"):
            target = income * pct / 100
            st.success(f"Suggested max rent (demo): **${target:,.0f} / mo**")
            st.caption("Real app could sync with bank/credit data via partners (Plaid, etc.).")

    render_footer()

# ---------- INVESTOR HUB ----------


def page_investor():
    st.title("📈 Investor Hub – Flips, BRRRR, Rentals")

    tabs = st.tabs(
        [
            "Quick Deal Analyzer (demo)",
            "ARV & Rehab (demo)",
            "Lead Scoring & Skip (demo)",
            "Portfolio Snapshot (demo)",
        ]
    )

    # TAB 1 – QUICK DEAL ANALYZER
    with tabs[0]:
        st.subheader("🧮 Quick Deal Analyzer (demo)")
        c1, c2, c3 = st.columns(3)
        with c1:
            arv = st.number_input("ARV (After-repair value)", 50000, 2000000, 260000, step=5000)
        with c2:
            purchase = st.number_input("Purchase price", 30000, 2000000, 140000, step=5000)
        with c3:
            rehab = st.number_input("Estimated rehab cost", 0, 1000000, 45000, step=5000)
        hold_months = st.slider("Holding period (months)", 1, 24, 6)
        if st.button("Analyze deal (demo)", key="deal_btn"):
            holding_costs = hold_months * 1200  # toy model
            total = purchase + rehab + holding_costs
            profit = arv - total
            margin = (profit / arv * 100) if arv > 0 else 0
            st.metric("Projected profit (demo)", f"${profit:,.0f}")
            st.metric("Margin on ARV (demo)", f"{margin:,.1f}%")
            st.caption("Real version will include closing costs, fees, and financing structure.")

    # TAB 2 – ARV & REHAB
    with tabs[1]:
        st.subheader("📐 ARV & Rehab Estimator (demo)")
        c1, c2 = st.columns(2)
        with c1:
            subj_sqft = st.number_input("Subject property sq ft", 400, 10000, 1600, step=100)
            comp_price = st.number_input("Average comp sale price", 50000, 2000000, 240000, step=5000)
        with c2:
            comp_sqft = st.number_input("Average comp sq ft", 400, 10000, 1700, step=100)
            rehab_level = st.selectbox("Rehab level (demo)", ["Light", "Medium", "Heavy"])
        if st.button("Estimate ARV & rehab (demo)", key="arv_btn"):
            arv_est = comp_price * (subj_sqft / comp_sqft)
            if rehab_level == "Light":
                rehab_est = 15000
            elif rehab_level == "Medium":
                rehab_est = 40000
            else:
                rehab_est = 75000
            st.success(
                f"Estimated ARV (demo): **${arv_est:,.0f}** · "
                f"Estimated rehab (demo): **${rehab_est:,.0f}**"
            )
            st.caption("Real engine would use MLS comps, CV, and contractor pricing.")

    # TAB 3 – LEAD SCORING & SKIP (MOCK)
    with tabs[2]:
        st.subheader("📊 Lead Scoring & Skip Tracing (demo)")
        leads_text = st.text_area(
            "Sample lead list (one per line, demo)",
            "123 Main St, Detroit, MI 48202\n"
            "456 Oak Ave, Warren, MI 48088\n"
            "789 Maple Dr, Grand Rapids, MI 49503",
            height=120,
        )
        if st.button("Score leads (demo)", key="score_leads_btn"):
            lines = [l.strip() for l in leads_text.splitlines() if l.strip()]
            st.info("Demo scoring – real version will pull ownership, equity, distress flags, etc.")
            for i, line in enumerate(lines, start=1):
                if i == 1:
                    label = "🔥 High – vacancy + equity signals (demo)"
                elif i == 2:
                    label = "🟡 Medium – some motivation (demo)"
                else:
                    label = "🔵 Low – nurture lead (demo)"
                st.write(f"- **{line}** → {label}")
            st.caption("Skip tracing APIs would plug in here in the production build.")

    # TAB 4 – PORTFOLIO SNAPSHOT
    with tabs[3]:
        st.subheader("📚 Portfolio Snapshot (demo)")
        st.write(
            """
Mock view of your rental / BRRRR portfolio:

- Doors: **7**  
- Est. portfolio value: **$1.9M**  
- Avg. cash-on-cash return: **11.3%**  
- Vacancies: **1** (demo)  
"""
        )
        st.metric("Doors (demo)", "7", "+2 this year")
        st.metric("Portfolio value (demo)", "$1.9M", "+$160k vs last year")
        st.metric("Avg cash-on-cash (demo)", "11.3%", "+1.2 pts YoY")

    render_footer()

# ================== MAIN NAVIGATION ==================


def main():
    st.sidebar.title("HomePathAI")
    nav = st.sidebar.radio(
        "Navigate",
        ["Home", "Buyer Hub", "Renter Hub", "Investor Hub"],
        index=0,
    )

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




