import streamlit as st
import pandas as pd
from math import ceil

# ---------------------------
# Demo Data
# ---------------------------

SAMPLE_PROPERTIES = [
    {
        "city": "Detroit, MI",
        "neighborhood": "Downtown",
        "price": 265000,
        "beds": 3,
        "baths": 2,
        "sqft": 1450,
        "type": "Single Family",
        "first_time_friendly": True,
        "investor_friendly": True,
        "section8_friendly": False,
        "rent_estimate": 2100,
        "arv": 310000,
    },
    {
        "city": "Detroit, MI",
        "neighborhood": "Midtown",
        "price": 195000,
        "beds": 2,
        "baths": 1,
        "sqft": 980,
        "type": "Condo",
        "first_time_friendly": True,
        "investor_friendly": False,
        "section8_friendly": True,
        "rent_estimate": 1650,
        "arv": 220000,
    },
    {
        "city": "Detroit, MI",
        "neighborhood": "Corktown",
        "price": 345000,
        "beds": 4,
        "baths": 2,
        "sqft": 1850,
        "type": "Single Family",
        "first_time_friendly": False,
        "investor_friendly": True,
        "section8_friendly": False,
        "rent_estimate": 2600,
        "arv": 390000,
    },
    {
        "city": "Grand Rapids, MI",
        "neighborhood": "Heritage Hill",
        "price": 285000,
        "beds": 3,
        "baths": 2,
        "sqft": 1600,
        "type": "Single Family",
        "first_time_friendly": True,
        "investor_friendly": True,
        "section8_friendly": True,
        "rent_estimate": 2200,
        "arv": 330000,
    },
]

SAMPLE_LEADS = [
    {
        "owner": "Taylor Johnson",
        "property": "1243 Elm St, Detroit, MI",
        "motivation": 88,
        "equity_est": 37,
        "status": "New",
        "source": "Pre-foreclosure",
    },
    {
        "owner": "Jordan Smith",
        "property": "89 Maple Ave, Detroit, MI",
        "motivation": 74,
        "equity_est": 41,
        "status": "Follow-up",
        "source": "Tired landlord",
    },
    {
        "owner": "Chris Lee",
        "property": "501 State St, Grand Rapids, MI",
        "motivation": 62,
        "equity_est": 29,
        "status": "New",
        "source": "Vacant",
    },
]

SAMPLE_AGENTS = [
    {
        "name": "Alex Rivera",
        "market": "Detroit",
        "specialty": "First-time buyers",
        "experience": "7 years",
        "rating": 4.8,
    },
    {
        "name": "Morgan Patel",
        "market": "Grand Rapids",
        "specialty": "Investors + multifamily",
        "experience": "9 years",
        "rating": 4.9,
    },
    {
        "name": "Jordan Brooks",
        "market": "Statewide",
        "specialty": "VA & FHA buyers",
        "experience": "5 years",
        "rating": 4.7,
    },
]

SAMPLE_LENDERS = [
    {
        "name": "Motor City Home Lending",
        "niche": "First-time buyers, FHA",
        "min_credit": 580,
        "max_ltv": 96.5,
        "turn_time": "24–48 hours",
    },
    {
        "name": "Great Lakes Investor Finance",
        "niche": "Investors, DSCR loans",
        "min_credit": 640,
        "max_ltv": 80,
        "turn_time": "2–4 days",
    },
    {
        "name": "Midwest Prime Mortgage",
        "niche": "Conventional + Jumbo",
        "min_credit": 620,
        "max_ltv": 95,
        "turn_time": "48–72 hours",
    },
]


# ---------------------------
# Helpers
# ---------------------------

def format_currency(x: float) -> str:
    return f"${x:,.0f}"


def render_app_header():
    st.markdown(
        """
        <div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.5rem;">
            <div style="
                width:34px;height:34px;border-radius:9px;
                background:linear-gradient(135deg,#0f6fff,#22c1c3);
                display:flex;align-items:center;justify-content:center;
                color:white;font-weight:800;font-size:18px;">
                H
            </div>
            <div>
                <div style="font-size:22px;font-weight:800;letter-spacing:0.03em;">
                    HomePathAI
                </div>
                <div style="font-size:12px;color:#5c6f82;">
                    For you • Built to make home buying simple
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")


def smartsearch_results(query: str, persona: str):
    if not query.strip():
        st.info("Type something like: `3 bed in Detroit under 300k with good schools`.")
        return

    st.subheader("SmartSearch interpretation")
    st.write(f"**You asked as a {persona.lower()}**: `{query}`")

    # Very light fake "extraction"
    query_low = query.lower()
    budget = None
    if "300k" in query_low or "300,000" in query_low:
        budget = 300000
    elif "200k" in query_low:
        budget = 200000

    st.markdown("**What HomePathAI understood:**")
    bullets = []
    if "detroit" in query_low:
        bullets.append("- City focus: Detroit, MI")
    if "grand rapids" in query_low:
        bullets.append("- City focus: Grand Rapids, MI")
    if "good schools" in query_low:
        bullets.append("- Preference for stronger school ratings")
    if "walk" in query_low or "walkable" in query_low:
        bullets.append("- Preference for walkable neighborhoods")
    if budget:
        bullets.append(f"- Target budget up to about {format_currency(budget)}")
    if "flip" in query_low or "br" in query_low or "brrrr" in query_low:
        bullets.append("- You’re likely targeting a flip / BRRRR-style deal")
    if not bullets:
        bullets.append("- General home search with personalized filters")

    st.markdown("\n".join(bullets))

    st.markdown("### Matching sample homes")
    df = pd.DataFrame(SAMPLE_PROPERTIES)
    # very basic filtering
    if "detroit" in query_low:
        df = df[df["city"].str.contains("Detroit")]
    if "grand rapids" in query_low:
        df = df[df["city"].str.contains("Grand Rapids")]

    if budget:
        df = df[df["price"] <= budget]

    if df.empty:
        st.warning("No sample homes match this exact search, but this is just demo data.")
    else:
        for _, row in df.iterrows():
            with st.container(border=True):
                st.markdown(
                    f"**{row['neighborhood']} • {row['city']}**  \n"
                    f"{row['beds']} bed • {row['baths']} bath • {row['sqft']} sqft"
                )
                st.write(
                    f"Price: {format_currency(row['price'])}  "
                    f"• Est. rent: {format_currency(row['rent_estimate'])}"
                )
                tags = []
                if row["first_time_friendly"]:
                    tags.append("First-time buyer friendly")
                if row["investor_friendly"]:
                    tags.append("Investor potential")
                if row["section8_friendly"]:
                    tags.append("Section 8 friendly")
                if tags:
                    st.caption(" · ".join(tags))


# ---------------------------
# Hubs
# ---------------------------

def buyer_hub():
    st.subheader("Buyer Hub – First-time buyer friendly")

    tabs = st.tabs(
        ["🏡 Home search", "📊 Neighborhood insights", "🧠 AI HomeBuyer Assistant"]
    )

    # --- Home search tab ---
    with tabs[0]:
        col1, col2 = st.columns([1.5, 1])
        with col1:
            city = st.selectbox(
                "Where are you looking?",
                ["Detroit, MI", "Grand Rapids, MI", "Other (demo limited to MI)"],
            )
            min_price, max_price = st.slider(
                "Price range",
                50000,
                600000,
                (150000, 350000),
                step=5000,
            )
            beds = st.select_slider("Bedrooms (min)", options=[1, 2, 3, 4, 5], value=3)
            first_time_only = st.checkbox("Show only first-time buyer friendly homes", True)

        with col2:
            st.write("### Filters")
            st.checkbox("Good school ratings", True)
            st.checkbox("Walkable area", False)
            st.checkbox("Low property taxes", False)
            st.checkbox("Near transit / downtown", True)

        st.markdown("#### Results")
        df = pd.DataFrame(SAMPLE_PROPERTIES)
        if "Detroit" in city:
            df = df[df["city"].str.contains("Detroit")]
        elif "Grand Rapids" in city:
            df = df[df["city"].str.contains("Grand Rapids")]

        df = df[(df["price"] >= min_price) & (df["price"] <= max_price)]
        df = df[df["beds"] >= beds]
        if first_time_only:
            df = df[df["first_time_friendly"]]

        if df.empty:
            st.warning("No sample matches – remember this is demo data only.")
        else:
            for _, row in df.iterrows():
                with st.container(border=True):
                    st.markdown(
                        f"**{row['neighborhood']} • {row['city']}**  \n"
                        f"{row['beds']} bed • {row['baths']} bath • {row['sqft']} sqft"
                    )
                    st.write(f"Price: {format_currency(row['price'])}")
                    st.caption("Designed to be simple and friendly for first-time buyers.")

    # --- Neighborhood insights tab ---
    with tabs[1]:
        st.markdown("#### Compare neighborhoods")

        col1, col2 = st.columns(2)
        with col1:
            city_a = st.selectbox("City A", ["Detroit, MI", "Grand Rapids, MI"], key="city_a")
        with col2:
            city_b = st.selectbox("City B", ["Grand Rapids, MI", "Detroit, MI"], key="city_b")

        st.write("This demo uses fake example scores just to show the UX.")

        metrics = ["Affordability", "Schools", "Safety", "Walkability", "Job growth"]
        scores_a = [7.5, 6.8, 5.9, 7.2, 7.0] if "Detroit" in city_a else [6.9, 7.4, 7.1, 6.8, 7.3]
        scores_b = [7.5, 6.8, 5.9, 7.2, 7.0] if "Detroit" in city_b else [6.9, 7.4, 7.1, 6.8, 7.3]

        table_data = []
        for m, a, b in zip(metrics, scores_a, scores_b):
            table_data.append(
                {
                    "Metric": m,
                    f"{city_a}": f"{a}/10",
                    f"{city_b}": f"{b}/10",
                }
            )
        st.table(pd.DataFrame(table_data))

        st.caption(
            "In production, these scores would be powered by real data: crime, schools, price trends, "
            "internet speeds, amenities, etc."
        )

    # --- AI assistant tab ---
    with tabs[2]:
        st.write("Describe your situation and let HomePathAI simplify it for you.")
        income = st.number_input("Household income (yearly, before tax)", 20000, 500000, 80000, step=5000)
        debts = st.number_input("Total monthly debts (loans, cards, etc.)", 0, 20000, 800, step=50)
        st.caption("We’ll use a simple estimate – not real underwriting.")

        if st.button("Estimate comfortable home budget"):
            dti = debts * 12 / income if income > 0 else 0
            # very rough demo calc
            safe_multiplier = 3.5
            budget = income * safe_multiplier
            if dti > 0.4:
                budget *= 0.8
            st.success(f"Demo estimate: You might comfortably shop around **{format_currency(budget)}**.")
            st.caption(
                "In the real app, this would use lender-grade calculators and live rate data."
            )


def investor_hub():
    st.subheader("Investor Hub – Deals, repair, skip tracing")

    tabs = st.tabs(
        ["📈 Deal analyzer", "🛠 Repair estimator", "📇 Lead scoring & skip trace"]
    )

    # --- Deal analyzer ---
    with tabs[0]:
        st.markdown("##### Quick BRRRR / flip-style deal analyzer")

        col1, col2 = st.columns(2)
        with col1:
            purchase_price = st.number_input("Purchase price", 20000, 2000000, 180000, step=5000)
            rehab_budget = st.number_input("Rehab budget", 0, 1000000, 45000, step=5000)
            arv = st.number_input("After-repair value (ARV)", 50000, 3000000, 310000, step=5000)
        with col2:
            holding_costs = st.number_input("Holding + closing costs", 0, 500000, 15000, step=2500)
            desired_roi = st.slider("Target ROI on cash invested", 5, 40, 18, step=1)

        total_costs = purchase_price + rehab_budget + holding_costs
        gross_profit = arv - total_costs
        roi_pct = (gross_profit / total_costs * 100) if total_costs else 0
        score = min(max(ceil(roi_pct / 4), 1), 10)

        st.markdown("#### Deal summary (demo)")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total in", format_currency(total_costs))
        col2.metric("Gross profit", format_currency(gross_profit))
        col3.metric("ROI (demo)", f"{roi_pct:.1f}%")

        st.write(f"**HomePathAI score (demo)**: {score}/10")
        if roi_pct >= desired_roi:
            st.success("This looks like it **meets or beats** your target ROI in this demo.")
        else:
            st.warning("This demo deal is **below** your target ROI – you may want to renegotiate or pass.")

        st.caption(
            "In production, this analyzer would pull real comps, taxes, insurance, rent, and exit strategies."
        )

    # --- Repair estimator ---
    with tabs[1]:
        st.markdown("##### AI-style repair estimator (demo numbers only)")
        col1, col2 = st.columns(2)
        with col1:
            beds = st.select_slider("Bedrooms", [1, 2, 3, 4, 5], value=3)
            baths = st.select_slider("Bathrooms", [1, 2, 3], value=2)
            sqft = st.number_input("Square footage", 600, 6000, 1500, step=50)
        with col2:
            condition = st.select_slider(
                "Current condition",
                ["Heavy distress", "Needs work", "Light cosmetic", "Rent-ready"],
                value="Needs work",
            )
            region_cost = st.selectbox(
                "Cost profile (demo only)", ["Lower cost", "Average", "Higher cost"],
                index=1,
            )

        base_per_sqft = 18
        if condition == "Heavy distress":
            base_per_sqft = 40
        elif condition == "Needs work":
            base_per_sqft = 28
        elif condition == "Light cosmetic":
            base_per_sqft = 15
        elif condition == "Rent-ready":
            base_per_sqft = 8

        multiplier = 1.0
        if region_cost == "Lower cost":
            multiplier = 0.85
        elif region_cost == "Higher cost":
            multiplier = 1.25

        est_repair = sqft * base_per_sqft * multiplier

        st.markdown("#### Demo repair breakdown")
        st.write(f"Estimated total repairs (demo): **{format_currency(est_repair)}**")

        line_items = pd.DataFrame(
            [
                {"Category": "Interior / finishes", "Estimate": est_repair * 0.32},
                {"Category": "Kitchens / baths", "Estimate": est_repair * 0.24},
                {"Category": "Systems (HVAC, electrical, plumbing)", "Estimate": est_repair * 0.22},
                {"Category": "Exterior / roof", "Estimate": est_repair * 0.14},
                {"Category": "Contingency", "Estimate": est_repair * 0.08},
            ]
        )
        line_items["Estimate"] = line_items["Estimate"].apply(format_currency)
        st.table(line_items)

        st.caption(
            "In the real app, this would use computer vision on photos + local contractor cost data."
        )

    # --- Lead scoring & skip trace ---
    with tabs[2]:
        st.markdown("##### Lead scoring & skip-trace style view (demo)")
        df = pd.DataFrame(SAMPLE_LEADS)
        df_display = df.copy()
        df_display["Motivation score"] = df_display["motivation"].astype(str) + "/100"
        df_display["Equity (est)"] = df_display["equity_est"].astype(str) + "%"

        df_display = df_display[
            ["owner", "property", "source", "Motivation score", "Equity (est)", "status"]
        ].rename(
            columns={
                "owner": "Owner",
                "property": "Property",
                "source": "Source",
                "status": "Status",
            }
        )
        st.table(df_display)

        st.info(
            "In production, this screen would plug into real skip-trace + list providers "
            "and let you launch calls, SMS, and mailers directly."
        )


def rent_and_moving_hub():
    st.subheader("Rent & Moving Hub")

    tabs = st.tabs(["🏠 Rentals", "📦 Moving & utilities", "📑 Section 8 info (demo)"])

    with tabs[0]:
        city = st.selectbox(
            "Where do you want to rent?",
            ["Detroit, MI", "Grand Rapids, MI"],
        )
        section8 = st.checkbox("Show Section 8-friendly examples", True)

        df = pd.DataFrame(SAMPLE_PROPERTIES)
        df = df[(df["rent_estimate"] > 0)]
        if "Detroit" in city:
            df = df[df["city"].str.contains("Detroit")]
        else:
            df = df[df["city"].str.contains("Grand Rapids")]

        if section8:
            df = df[df["section8_friendly"]]

        if df.empty:
            st.warning("No sample rentals match these filters – demo data only.")
        else:
            for _, row in df.iterrows():
                with st.container(border=True):
                    st.markdown(
                        f"**{row['neighborhood']} • {row['city']}**  \n"
                        f"{row['beds']} bed • {row['baths']} bath • {row['sqft']} sqft"
                    )
                    st.write(f"Est. rent: {format_currency(row['rent_estimate'])}")
                    st.caption("Demo rental. Real app would show live listings & application links.")

    with tabs[1]:
        st.markdown("##### Moving checklist (demo)")
        st.write(
            "- Research movers and get 2–3 quotes  \n"
            "- Change your address (USPS, banks, ID)  \n"
            "- Schedule utilities (electric, gas, internet)  \n"
            "- Pack non-essentials early  \n"
            "- Take photos of old place for records"
        )
        st.caption("In the real app, this would connect to actual movers & utility providers.")

    with tabs[2]:
        st.markdown("##### Section 8 (demo educational content)")
        st.write(
            "HomePathAI could help renters understand Section 8 basics: waiting lists, inspections, "
            "rent limits, landlord requirements, and connect them with Section 8-friendly listings."
        )


def agents_and_lenders_hub():
    st.subheader("Agents & Lenders Hub")

    tabs = st.tabs(["👥 Agent hub", "🏦 Get pre-approved"])

    # --- Agent hub ---
    with tabs[0]:
        market = st.selectbox(
            "Filter by market",
            ["All", "Detroit", "Grand Rapids", "Statewide"],
        )
        specialty = st.selectbox(
            "Filter by specialty",
            ["All", "First-time buyers", "Investors + multifamily", "VA & FHA buyers"],
        )

        agents = SAMPLE_AGENTS
        filtered = []
        for a in agents:
            if market != "All" and market not in a["market"]:
                continue
            if specialty != "All" and specialty not in a["specialty"]:
                continue
            filtered.append(a)

        if not filtered:
            st.warning("No sample agents match those filters in this demo.")
        else:
            for a in filtered:
                with st.container(border=True):
                    st.markdown(f"**{a['name']}**  \n{a['market']} • {a['specialty']}")
                    st.caption(
                        f"{a['experience']} experience • Rating: {a['rating']}/5.0 (demo data)"
                    )
                    st.button(f"Request intro to {a['name']} (demo)", key=f"agent_{a['name']}")

        st.caption("In the real platform, agent routing would respect MLS / brokerage rules.")

    # --- Lender / pre-approval flow ---
    with tabs[1]:
        st.markdown("##### 3-step demo pre-approval flow")

        step = st.radio(
            "Step",
            [1, 2, 3],
            format_func=lambda x: f"Step {x}",
            horizontal=True,
        )

        if step == 1:
            st.write("**Step 1 – Basics**")
            loan_type = st.selectbox(
                "Loan type (demo)",
                ["FHA (low down payment)", "Conventional", "Investor (DSCR)", "VA"],
            )
            price_target = st.number_input(
                "Target purchase price",
                50000,
                2500000,
                300000,
                step=10000,
            )
            down_payment = st.slider("Down payment % (demo)", 3, 30, 5, step=1)
            st.info(
                "In production, this step would feed into a lender's actual underwriting engine."
            )

        elif step == 2:
            st.write("**Step 2 – Snapshot (demo)**")
            income = st.number_input("Household income (yearly)", 20000, 500000, 90000, step=5000)
            credit = st.slider("Credit score (demo)", 520, 850, 700, step=10)
            debts = st.number_input("Total monthly debts", 0, 20000, 900, step=50)
            st.caption("Not live underwriting – just demo logic.")

        else:
            st.write("**Step 3 – Matching demo lenders**")
            credit = st.session_state.get("demo_credit_for_match", 700)
            # We'll just show all sample lenders for demo
            for lender in SAMPLE_LENDERS:
                with st.container(border=True):
                    st.markdown(f"**{lender['name']}**")
                    st.write(lender["niche"])
                    st.write(
                        f"Min credit (demo): {lender['min_credit']} • Max LTV: {lender['max_ltv']}%"
                    )
                    st.caption(f"Typical response: {lender['turn_time']} (demo only)")
                    st.button(f"Start with {lender['name']} (demo)", key=f"lend_{lender['name']}")


def help_and_about():
    st.subheader("Help & About HomePathAI (Demo)")

    with st.expander("What is HomePathAI?"):
        st.write(
            "HomePathAI is an AI-first real estate platform demo that combines:\n"
            "- First-time home buyer tools\n"
            "- Investor deal analysis & repair estimates\n"
            "- Agent & lender matching\n"
            "- Rent + moving tools\n"
            "This demo runs on fake data, but the flows are designed for a real startup product."
        )

    with st.expander("Is this using real MLS or lender data?"):
        st.write(
            "No. This is a **demo only**. Real integrations would require licensed MLS feeds, "
            "lender partners, and compliance work."
        )

    with st.expander("What happens next for the real build?"):
        st.write(
            "- Connect this front-end to a production backend (AWS / similar)\n"
            "- Integrate real data providers (MLS, property, maps, lenders)\n"
            "- Add auth, security, and real user accounts\n"
            "- Deploy to web + mobile\n"
            "- Scale with monitoring and analytics\n"
        )

    st.info(
        "This demo is meant to show **product vision and UX** for investors, partners, and developers."
    )


# ---------------------------
# Main app
# ---------------------------

def main():
    st.set_page_config(
        page_title="HomePathAI Demo",
        page_icon="🏠",
        layout="wide",
    )

    render_app_header()

    st.sidebar.title("HomePathAI Demo")
    section = st.sidebar.radio(
        "Navigate",
        [
            "🏠 Home / SmartSearch",
            "🟢 Buyer Hub",
            "🟠 Investor Hub",
            "🔵 Rent & Moving",
            "🟣 Agents & Lenders",
            "❓ Help & About",
        ],
    )

    if section == "🏠 Home / SmartSearch":
        st.subheader("SmartSearch – conversational search (demo)")
        persona = st.radio("I’m searching as a…", ["Buyer", "Investor", "Renter"], horizontal=True)
        query = st.text_input(
            "Describe what you're looking for",
            placeholder="Example: 3 bed in Detroit under 300k, good schools, walkable",
        )
        if st.button("Run SmartSearch (demo)"):
            smartsearch_results(query, persona)
        st.caption(
            "In the real app, this would use an AI model fine-tuned on real estate to route you to "
            "the right homes, neighborhoods, and tools."
        )

    elif section == "🟢 Buyer Hub":
        buyer_hub()

    elif section == "🟠 Investor Hub":
        investor_hub()

    elif section == "🔵 Rent & Moving":
        rent_and_moving_hub()

    elif section == "🟣 Agents & Lenders":
        agents_and_lenders_hub()

    else:
        help_and_about()


if __name__ == "__main__":
    main()




