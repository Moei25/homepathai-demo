import streamlit as st
import pandas as pd
import pydeck as pdk

# --------------- CONFIG --------------- #
st.set_page_config(
    page_title="HomePathAI Demo",
    page_icon="🏠",
    layout="wide",
)

# --------------- MOCK DATA --------------- #

PROPERTY_DATA = [
    {
        "id": 1,
        "city": "Detroit, MI",
        "neighborhood": "Downtown",
        "price": 285000,
        "beds": 3,
        "baths": 2,
        "sqft": 1650,
        "type": "Buyer",
        "score": 87,
        "cashflow": None,
        "lat": 42.3314,
        "lon": -83.0458,
        "tag": "First-time buyer friendly",
    },
    {
        "id": 2,
        "city": "Detroit, MI",
        "neighborhood": "Midtown",
        "price": 420000,
        "beds": 4,
        "baths": 3,
        "sqft": 2200,
        "type": "Investor",
        "score": 92,
        "cashflow": 750,
        "lat": 42.3487,
        "lon": -83.058,
        "tag": "Value-add duplex",
    },
    {
        "id": 3,
        "city": "Miami, FL",
        "neighborhood": "Little Havana",
        "price": 365000,
        "beds": 3,
        "baths": 2,
        "sqft": 1400,
        "type": "Investor",
        "score": 89,
        "cashflow": 640,
        "lat": 25.765,
        "lon": -80.219,
        "tag": "Rental hot zone",
    },
    {
        "id": 4,
        "city": "Grand Rapids, MI",
        "neighborhood": "Eastown",
        "price": 245000,
        "beds": 2,
        "baths": 1,
        "sqft": 1200,
        "type": "Buyer",
        "score": 84,
        "cashflow": None,
        "lat": 42.9634,
        "lon": -85.6681,
        "tag": "Walkable & family friendly",
    },
    {
        "id": 5,
        "city": "Chicago, IL",
        "neighborhood": "Logan Square",
        "price": 525000,
        "beds": 3,
        "baths": 2,
        "sqft": 1900,
        "type": "Investor",
        "score": 91,
        "cashflow": 820,
        "lat": 41.923,
        "lon": -87.712,
        "tag": "High appreciation corridor",
    },
]

RENTAL_DATA = [
    {
        "id": 101,
        "city": "Detroit, MI",
        "neighborhood": "Downtown",
        "rent": 1850,
        "beds": 2,
        "baths": 1,
        "sqft": 900,
        "type": "Apartment",
        "section8_friendly": True,
    },
    {
        "id": 102,
        "city": "Detroit, MI",
        "neighborhood": "Midtown",
        "rent": 1450,
        "beds": 1,
        "baths": 1,
        "sqft": 650,
        "type": "Studio",
        "section8_friendly": False,
    },
    {
        "id": 103,
        "city": "Grand Rapids, MI",
        "neighborhood": "Eastown",
        "rent": 1650,
        "beds": 2,
        "baths": 1,
        "sqft": 800,
        "type": "Duplex upper",
        "section8_friendly": True,
    },
]

LENDERS = [
    {
        "name": "Great Lakes Home Finance",
        "type": "First-time buyer focused",
        "min_credit": 620,
        "max_ltv": "97%",
        "states": "MI, OH, IN",
    },
    {
        "name": "Metro Investor Lending",
        "type": "DSCR & fix-and-flip",
        "min_credit": 660,
        "max_ltv": "80% (investment)",
        "states": "Nationwide",
    },
    {
        "name": "Sunrise Mortgage Co.",
        "type": "Conventional & FHA",
        "min_credit": 600,
        "max_ltv": "96.5%",
        "states": "FL, GA, TX",
    },
]

AGENTS = [
    {
        "name": "Jordan Lee",
        "market": "Detroit Metro",
        "focus": "First-time buyers & house hackers",
        "avg_response": "5 min",
        "deals_year": 42,
    },
    {
        "name": "Alicia Rivera",
        "market": "Miami–Dade",
        "focus": "Out-of-state investors",
        "avg_response": "9 min",
        "deals_year": 58,
    },
    {
        "name": "Marcus Green",
        "market": "Grand Rapids",
        "focus": "Families & move-up buyers",
        "avg_response": "7 min",
        "deals_year": 31,
    },
]

MOVERS = [
    {
        "name": "SmoothMove Detroit",
        "areas": "SE Michigan",
        "specialty": "Local + small long-distance moves",
        "estimate": "$$$",
    },
    {
        "name": "Interstate Relocation Group",
        "areas": "Nationwide",
        "specialty": "State-to-state relocation",
        "estimate": "$$$$",
    },
    {
        "name": "Neighborhood Haulers",
        "areas": "Regional",
        "specialty": "Budget-friendly moves",
        "estimate": "$$",
    },
]


# --------------- STYLES --------------- #

def inject_css():
    st.markdown(
        """
        <style>
        .main {
            background: #050816;
        }
        .home-hero {
            background: linear-gradient(135deg, #020617, #0f172a);
            border-radius: 18px;
            padding: 26px 26px 18px 26px;
            border: 1px solid rgba(148,163,184,0.4);
            box-shadow: 0 22px 50px rgba(15,23,42,0.7);
        }
        .hp-title {
            font-size: 32px;
            font-weight: 700;
            color: #e5f4ff;
            letter-spacing: 0.03em;
        }
        .hp-sub {
            font-size: 15px;
            color: #cbd5f5;
            margin-top: 4px;
        }
        .hp-pill-row {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 14px;
        }
        .hp-pill {
            font-size: 13px;
            padding: 6px 13px;
            border-radius: 999px;
            border: 1px solid rgba(148,163,184,0.6);
            color: #e5f4ff;
            background: radial-gradient(circle at top left, #1d4ed8 0, #020617 55%);
        }
        .hp-section-title {
            font-size: 20px;
            font-weight: 600;
            color: #e5f4ff;
            margin-bottom: 4px;
        }
        .hp-section-sub {
            font-size: 13px;
            color: #9ca3af;
        }
        .hp-card {
            background: radial-gradient(circle at top left, #0f172a 0, #020617 55%);
            border-radius: 16px;
            padding: 14px 16px;
            border: 1px solid rgba(148,163,184,0.4);
            box-shadow: 0 16px 30px rgba(15,23,42,0.9);
            height: 100%;
        }
        .hp-badge {
            display: inline-block;
            padding: 3px 9px;
            border-radius: 999px;
            font-size: 11px;
            font-weight: 500;
            background: rgba(45,212,191,0.1);
            color: #5eead4;
            border: 1px solid rgba(45,212,191,0.6);
        }
        .hp-tag {
            display: inline-block;
            padding: 3px 9px;
            border-radius: 999px;
            font-size: 11px;
            background: rgba(59,130,246,0.14);
            color: #bfdbfe;
        }
        .hp-price {
            font-size: 18px;
            font-weight: 600;
            color: #e5f4ff;
            margin-top: 6px;
        }
        .hp-metrics {
            font-size: 12px;
            color: #9ca3af;
            margin-top: 4px;
        }
        .hp-footer {
            font-size: 12px;
            color: #6b7280;
            margin-top: 24px;
            border-top: 1px solid rgba(55,65,81,0.8);
            padding-top: 10px;
            text-align: center;
        }
        .hp-logo {
            font-size: 15px;
            font-weight: 700;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            color: #38bdf8;
        }
        .stTabs [role="tablist"] {
            gap: 4px;
        }
        .stTabs [role="tab"] {
            padding-top: 6px;
            padding-bottom: 6px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# --------------- HELPERS --------------- #

def format_price(value: int) -> str:
    return "${:,.0f}".format(value)


def format_currency(value: float) -> str:
    return "${:,.0f}".format(value)


def property_dataframe(city_filter: str = None):
    df = pd.DataFrame(PROPERTY_DATA)
    if city_filter:
        mask = df["city"].str.contains(city_filter, case=False)
        df = df[mask]
    return df


def rental_dataframe(city_filter: str = None):
    df = pd.DataFrame(RENTAL_DATA)
    if city_filter:
        mask = df["city"].str.contains(city_filter, case=False)
        df = df[mask]
    return df


def render_property_card(p):
    st.markdown(
        f"""
        <div class="hp-card">
            <span class="hp-tag">{p['tag']}</span>
            <div class="hp-price">{format_price(p['price'])}</div>
            <div class="hp-metrics">
                {p['beds']} bd · {p['baths']} ba · {p['sqft']:,} sqft
            </div>
            <div class="hp-metrics">
                {p['neighborhood']} · {p['city']}
            </div>
            <div class="hp-metrics" style="margin-top:4px;">
                HomePath Score: <b>{p['score']}</b>
                {" · Est. monthly cashflow: <b>" + format_currency(p['cashflow']) + "</b>" if p['cashflow'] else ""}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def repair_estimate(sqft: int, level: str) -> int:
    base = 22  # $/sqft light
    if level == "Light (paint, fixtures, cosmetics)":
        cost_per_sqft = base
    elif level == "Medium (kitchens, baths, flooring)":
        cost_per_sqft = base + 12
    else:
        cost_per_sqft = base + 25
    return int(sqft * cost_per_sqft)


def investor_metrics(arv: int, purchase: int, rehab: int, rent: int):
    total_basis = purchase + rehab
    equity = max(arv - total_basis, 0)
    coc_return = None
    if purchase > 0:
        coc_return = (max((rent * 12) - (0.4 * rent * 12), 0) / purchase) * 100
    return total_basis, equity, coc_return


def smartsearch_response(query: str, persona: str):
    query_l = query.lower()
    bullets = []

    if "detroit" in query_l:
        bullets.append("✅ Prioritizing Detroit Metro with strong cash-flow and improving blocks.")
    if "miami" in query_l or "florida" in query_l:
        bullets.append("☀️ Highlighting Miami sub-markets with solid rent-to-price ratios.")
    if "family" in query_l or "schools" in query_l:
        bullets.append("🏫 Weighting school ratings, parks, and low traffic noise higher.")
    if "walk" in query_l or "walkable" in query_l:
        bullets.append("🚶 Focusing on walk scores, transit access, and nearby daily amenities.")
    if "cheap" in query_l or "budget" in query_l or "under" in query_l:
        bullets.append("💸 Filtering for best value vs area median price, not just lowest price.")

    persona_line = {
        "Buyer": "I’ll return a short list of 3–7 neighborhoods and homes that match your budget and lifestyle.",
        "Investor": "I’ll surface deals with margin, rental demand, and distress indicators.",
        "Renter": "I’ll focus on safe, convenient rentals that don’t wreck your monthly budget.",
    }[persona]

    if not bullets:
        bullets.append("✨ I’ll blend lifestyle, risk, and affordability into one ranked list of options.")

    return bullets, persona_line


# --------------- PAGE RENDERERS --------------- #

def render_home():
    inject_css()

    # Hero
    st.markdown(
        """
        <div class="home-hero">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:16px;flex-wrap:wrap;">
                <div style="flex:1;min-width:260px;">
                    <div class="hp-logo">HOMEPATHAI</div>
                    <div class="hp-title">Find your next home with AI that actually thinks like a local.</div>
                    <div class="hp-sub">
                        Smart search, investor-grade numbers, and renter tools — all in one experience built for
                        first-time buyers, flippers, house hackers, and renters.
                    </div>
                    <div class="hp-pill-row">
                        <div class="hp-pill">✨ First-time buyer friendly</div>
                        <div class="hp-pill">📊 Investor deal analysis</div>
                        <div class="hp-pill">🗺️ Neighborhood intelligence</div>
                        <div class="hp-pill">🛠️ Repair cost estimator</div>
                        <div class="hp-pill">📦 Rent & moving tools</div>
                    </div>
                </div>
                <div style="flex:0.9;min-width:260px;margin-top:10px;">
                    <div style="
                        background: radial-gradient(circle at top left, #1f2937 0, #020617 60%);
                        border-radius: 16px;
                        padding: 12px 14px;
                        border: 1px solid rgba(148,163,184,0.6);
                    ">
                        <div style="font-size:13px;color:#9ca3af;margin-bottom:6px;">SmartSearch – conversational search</div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.write("")

    # SmartSearch input row
    col_query, col_persona = st.columns([3, 1])
    with col_query:
        smart_query = st.text_input(
            "Describe what you're looking for (e.g. “3 bed under 350k in a safe Detroit suburb with good schools”):",
            key="home_smartsearch",
        )
    with col_persona:
        persona = st.selectbox("I'm searching as a:", ["Buyer", "Investor", "Renter"])

    if st.button("Run SmartSearch (demo)", type="primary"):
        if not smart_query.strip():
            st.info("Tell me what you're looking for and I'll guide you.")
        else:
            bullets, persona_line = smartsearch_response(smart_query, persona)
            st.markdown("#### HomePathAI SmartSearch Preview")
            st.write(persona_line)
            st.write("")
            for b in bullets:
                st.markdown(f"- {b}")
            st.write("")
            st.caption("This is a demo preview. In production, this will be powered by live MLS + rental feeds + your preferences over time.")

    st.write("---")

    # Trending homes & neighborhood insight
    c1, c2 = st.columns([1.4, 1])

    with c1:
        st.markdown('<div class="hp-section-title">Trending homes near you</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="hp-section-sub">Sample homes across Detroit, Grand Rapids, Chicago, and Miami with buyer- and investor-friendly options.</div>',
            unsafe_allow_html=True,
        )
        st.write("")
        df = pd.DataFrame(PROPERTY_DATA)
        for i, row in df.iterrows():
            with st.container():
                render_property_card(row)
                st.write("")

    with c2:
        st.markdown('<div class="hp-section-title">Neighborhood snapshot</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="hp-section-sub">Safety, price, and walkability at a glance — powered by a simple heat-style map in this demo.</div>',
            unsafe_allow_html=True,
        )

        df_map = pd.DataFrame(PROPERTY_DATA)
        if not df_map.empty:
            center_lat = df_map["lat"].mean()
            center_lon = df_map["lon"].mean()
            layer = pdk.Layer(
                "ScatterplotLayer",
                data=df_map,
                get_position='[lon, lat]',
                get_radius=400,
                get_fill_color='[56, 189, 248, 190]',
                pickable=True,
            )
            view_state = pdk.ViewState(
                latitude=center_lat,
                longitude=center_lon,
                zoom=4.2,
                bearing=0,
                pitch=35,
            )
            st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{city}\n{neighborhood}"}))
        st.write("")
        st.markdown(
            """
            <div class="hp-card">
                <div class="hp-badge">Demo insight</div>
                <div class="hp-metrics" style="margin-top:6px;">
                    • Detroit & Grand Rapids showing strong cash-flow and affordability.<br>
                    • Miami & Chicago showing higher appreciation but tighter cash-flow.<br>
                    • In production, this would be driven by crime, schools, income & rent trends.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="hp-footer">
            For you · Built to make your home buying simple. HomePathAI unifies buyers, investors, renters, and agents in one smart platform.
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_buyer_hub():
    st.header("Buyer Hub · First-time buyer friendly")
    st.caption("Guided path from 'curious' to 'confident pre-approval' — without the overwhelm.")

    tab1, tab2, tab3 = st.tabs(
        ["Buying roadmap", "Payment & affordability", "Explore lenders"]
    )

    with tab1:
        st.subheader("Step-by-step path")
        steps = [
            "1. Tell us your budget, income, and what 'home' looks like for you.",
            "2. HomePathAI maps neighborhoods that actually match your lifestyle.",
            "3. We estimate monthly payments & closing costs — in plain English.",
            "4. You connect with friendly lenders & agents that fit your profile.",
            "5. We help you compare 3–5 top options, not 300 random listings.",
        ]
        for s in steps:
            st.markdown(f"- {s}")

        st.info("In the real app, this becomes an interactive onboarding flow that saves your profile and syncs to SmartSearch and your lender.")

    with tab2:
        st.subheader("Estimate a monthly payment (demo only)")
        col1, col2 = st.columns(2)
        with col1:
            home_price = st.number_input("Home price", 80000, 1500000, 300000, step=5000)
            down_pct = st.slider("Down payment (%)", 0, 30, 5)
        with col2:
            rate = st.slider("Interest rate (%)", 2.5, 10.0, 6.75, 0.05)
            years = st.selectbox("Loan term", [15, 20, 30], index=2)

        loan_amount = int(home_price * (1 - down_pct / 100))
        n_payments = years * 12
        monthly_rate = rate / 100 / 12
        if monthly_rate > 0:
            monthly_pmt = loan_amount * (monthly_rate * (1 + monthly_rate) ** n_payments) / (
                (1 + monthly_rate) ** n_payments - 1
            )
        else:
            monthly_pmt = loan_amount / n_payments

        taxes_escrow = home_price * 0.015 / 12  # very rough
        insurance = 90
        total_monthly = monthly_pmt + taxes_escrow + insurance

        st.write("### Estimated monthly payment")
        st.metric("Total est. monthly payment", f"{format_currency(total_monthly)}")

        st.caption("This is a rough demo. The production app will use local taxes, insurance, and PMI rules per county & loan type.")

    with tab3:
        st.subheader("Featured sample lenders (demo)")
        df = pd.DataFrame(LENDERS)
        st.dataframe(df, hide_index=True)
        st.info("In production, this becomes a live marketplace where buyers compare rates & fees, then get pre-approved without leaving HomePathAI.")


def render_investor_hub():
    st.header("Investor Hub · Deals, repairs & skip tracing in one place")
    st.caption("High-level investor tools — all demo logic, no real data or skip tracing in this version.")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Deal analyzer", "Repair estimator", "Skip tracing (mock)", "Sample investor leads"]
    )

    with tab1:
        st.subheader("Quick flip / BRRRR deal analyzer (demo)")
        col1, col2 = st.columns(2)
        with col1:
            arv = st.number_input("After-repair value (ARV)", 50000, 1500000, 350000, step=5000)
            purchase = st.number_input("Purchase price", 30000, 1000000, 210000, step=5000)
        with col2:
            rehab = st.number_input("Estimated rehab budget", 0, 500000, 60000, step=5000)
            rent = st.number_input("Expected monthly rent (if held)", 0, 15000, 2400, step=100)

        basis, equity, coc = investor_metrics(arv, purchase, rehab, rent)
        st.write("### Deal snapshot")
        st.metric("Total project cost (basis)", format_currency(basis))
        st.metric("Instant equity at ARV", format_currency(equity))

        if coc is not None:
            st.metric("Est. cash-on-cash return (year 1)", f"{coc:,.1f}%")

        st.caption("Demo math only. Real version plugs into comps, rents, and financing options.")

    with tab2:
        st.subheader("Repair cost estimator (photo-free demo version)")
        level = st.selectbox(
            "Scope of work",
            [
                "Light (paint, fixtures, cosmetics)",
                "Medium (kitchens, baths, flooring)",
                "Heavy (systems, layout changes, major rehab)",
            ],
        )
        sqft = st.number_input("Approximate finished square footage", 400, 6000, 1500, step=50)
        if st.button("Estimate rehab cost", key="investor_repair_btn"):
            est = repair_estimate(sqft, level)
            st.success(f"Estimated rehab budget: {format_currency(est)}")
            st.caption("In production, this will be driven by before/after photo datasets, local labor & material costs by ZIP.")

    with tab3:
        st.subheader("Skip tracing & lead prioritization (mock)")
        st.write("This is UI-only — no real skip tracing is happening in this demo.")

        owner_name = st.text_input("Owner name or address")
        motivation = st.multiselect(
            "Potential motivation signals (demo tags)",
            ["Pre-foreclosure", "Out-of-state owner", "Vacant", "Inherited", "Code violations"],
        )
        if st.button("Run skip trace (demo)", key="skiptrace_btn"):
            st.info("In the real app, this would call a skip tracing provider and enrich the record.")

            st.markdown("##### Demo result")
            st.write(
                """
                • Owner: **Sample Owner LLC**  
                • Mailing address: **Somewhere in FL (out-of-state)**  
                • Phones: **3 possible numbers**, 1 marked as “likely mobile”  
                • Email: **Pull 1–2 if available**  
                • Motivation score: **High** (3 of your selected signals match)
                """
            )
            st.caption("This is purely illustrative UI. No real personal data is used or stored in this demo.")

    with tab4:
        st.subheader("Sample investor-style leads (demo data)")
        df = pd.DataFrame(
            [
                {
                    "Address": "123 Maple St, Detroit, MI",
                    "ARV": 310000,
                    "As-is": 185000,
                    "Est. Rehab": 55000,
                    "Motivation": "Vacant · Out-of-state owner",
                },
                {
                    "Address": "456 Oak Ave, Grand Rapids, MI",
                    "ARV": 275000,
                    "As-is": 160000,
                    "Est. Rehab": 35000,
                    "Motivation": "Long-term landlord · Deferred maintenance",
                },
                {
                    "Address": "789 Brick Rd, Chicago, IL",
                    "ARV": 520000,
                    "As-is": 330000,
                    "Est. Rehab": 90000,
                    "Motivation": "Estate sale · Needs full rehab",
                },
            ]
        )
        df["Spread"] = df["ARV"] - df["As-is"] - df["Est. Rehab"]
        st.dataframe(df, hide_index=True)
        st.caption("This is fake data. In production, this would come from your wholesaling / off-market data feeds and filters.")


def render_rent_moving():
    st.header("Rent & Moving · Make relocating less painful")
    st.caption("For renters, relocators, and anyone comparing cities without guessing.")

    tab1, tab2 = st.tabs(["Rentals & affordability", "Moving & Section 8 resources"])

    with tab1:
        st.subheader("Sample rentals by city (demo data)")
        city = st.selectbox("Choose a city", ["All", "Detroit, MI", "Grand Rapids, MI"])
        if city == "All":
            df = rental_dataframe()
        else:
            df = rental_dataframe(city)

        st.dataframe(df, hide_index=True)
        st.caption("This is demo data. The real app will plug into partner rental feeds and apply your affordability rules.")

    with tab2:
        st.subheader("Moving helpers")
        st.markdown("##### Featured demo moving partners")
        for m in MOVERS:
            st.markdown(
                f"**{m['name']}**  \nAreas: {m['areas']}  \nSpecialty: {m['specialty']}  \nCost tier: {m['estimate']}"
            )
            st.write("")

        st.subheader("Section 8 & voucher-friendly info (demo)")
        st.write(
            """
            • We’ll highlight rentals marked as voucher-friendly where possible.  
            • Explain how payment standards and inspections work in plain English.  
            • Help renters understand realistic timelines and documentation.
            """
        )
        st.caption("In production, this ties into local housing authority data and filters within the rental feed.")


def render_agent_hub():
    st.header("Agent Hub · Built for the agents who actually pick up the phone")
    st.caption("Demo view of how agents will plug into HomePathAI.")

    tab1, tab2 = st.tabs(["Agent marketplace", "Workflow automation (concept)"])

    with tab1:
        st.subheader("Sample featured agents (demo)")
        for a in AGENTS:
            st.markdown(
                f"""
                **{a['name']}** — {a['market']}  
                • Focus: {a['focus']}  
                • Avg. response time: {a['avg_response']}  
                • Transactions (last 12 months): {a['deals_year']}
                """
            )
            st.write("")

        st.info("In production, agents will have verified profiles, reviews, coverage maps, and routing from SmartSearch leads.")

    with tab2:
        st.subheader("AI assistant for agents (concept)")
        st.write(
            """
            Imagine an inbox where HomePathAI:

            • Drafts replies to buyer & investor leads  
            • Writes MLS-style descriptions from your notes or bullet points  
            • Suggests comps for pricing conversations  
            • Nudges you when high-intent leads don’t get a reply  
            • Syncs to your CRM (kvCORE, Follow Up Boss, etc.)

            This demo doesn’t automate a real inbox yet — it’s here to show how the UX will look and feel.
            """
        )


def render_help():
    st.header("About this demo")
    st.write(
        """
        This is a **Streamlit-based concept demo** of HomePathAI — not the full production application.

        What this demo shows:

        • A unified UI for buyers, investors, renters, and agents  
        • SmartSearch concept flow  
        • Investor deal analysis and repair estimator logic  
        • Rent & moving tools concept  
        • Agent marketplace & automation concept  
        • Maps and neighborhood snapshots using mock data  

        What this demo does **not** do yet:

        • Connect to real MLS, rental, or skip tracing data  
        • Store user profiles or login accounts  
        • Execute real pre-approvals, applications, or funding  
        • Replace real legal, lending, or tax advice  

        This is designed to help investors, partners, and dev teams **see the product vision clearly** and understand how all pieces fit together.
        """
    )


# --------------- MAIN --------------- #

def main():
    inject_css()

    with st.sidebar:
        st.markdown("### 🏠 HomePathAI")
        st.caption("All-in-one AI assistant for buyers, investors, renters & agents.")
        page = st.radio(
            "Navigate",
            ["Home", "Buyer Hub", "Investor Hub", "Rent & Moving", "Agent Hub", "Help / About"],
            index=0,
        )

    if page == "Home":
        render_home()
    elif page == "Buyer Hub":
        render_buyer_hub()
    elif page == "Investor Hub":
        render_investor_hub()
    elif page == "Rent & Moving":
        render_rent_moving()
    elif page == "Agent Hub":
        render_agent_hub()
    else:
        render_help()


if __name__ == "__main__":
    main()





