import streamlit as st
import pandas as pd
import numpy as np

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="HomePathAI Demo",
    layout="wide"
)

# =========================================================
# SIMPLE STATE FOR TOP NAV
# =========================================================
if "active_page" not in st.session_state:
    st.session_state["active_page"] = "Home"


def set_page(page_name: str):
    st.session_state["active_page"] = page_name


# =========================================================
# TOP BAR: LOGO + NAV PILLS (LIKE YOUR SCREENSHOT)
# =========================================================
with st.container():
    left, right = st.columns([1, 3])

    # Logo + title
    with left:
        st.markdown(
            """
            <div style="
                display:flex;
                align-items:center;
                gap:10px;
                margin-bottom:4px;
            ">
                <div style="
                    width:40px;
                    height:40px;
                    border-radius:12px;
                    background:#015f73;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    color:white;
                    font-weight:700;
                    font-size:20px;
                ">
                    AI
                </div>
                <div style="font-size:26px;font-weight:700;color:#014451;">
                    HomePathAI
                </div>
            </div>
            <div style="color:#6b7b88;font-size:13px;">
                AI that thinks like a local.
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Top nav pills
    with right:
        labels = [
            "First time buyer friendly",
            "Investor deal analysis",
            "Neighbor insights",
            "Repair estimator",
            "Rent & moving tools",
        ]
        pages = ["Buyer", "Investor", "Neighbor", "Repair", "Rent"]

        cols = st.columns(len(labels))
        for col, label, page in zip(cols, labels, pages):
            with col:
                is_selected = st.session_state["active_page"] == page
                style = """
                    border:none;
                    padding:8px 14px;
                    border-radius:999px;
                    font-size:13px;
                    cursor:pointer;
                """
                if is_selected:
                    bg = "#006d77"
                    color = "white"
                else:
                    bg = "#e0f4f7"
                    color = "#035057"

                button_html = f"""
                <form action="" method="post">
                    <button name="nav-{page}" style="
                        {style}
                        background:{bg};
                        color:{color};
                    ">{label}</button>
                </form>
                """
                # HTML button (visual) + real Streamlit button on top of it
                clicked = st.button(label, key=f"nav_btn_{page}")
                st.markdown(button_html, unsafe_allow_html=True)
                if clicked:
                    set_page(page)

# =========================================================
# HERO HEADER (TEAL GRADIENT) + SEARCH BAR
# =========================================================
hero_html = """
<div style="
    margin-top:24px;
    padding:32px 40px 28px 40px;
    border-radius:18px;
    background:linear-gradient(135deg,#0f92ce,#00a3b4,#14c5d9);
    color:white;
    box-shadow:0 10px 25px rgba(0,0,0,0.15);
">
    <h1 style="
        margin:0 0 10px 0;
        font-size:30px;
        font-weight:700;
    ">
        Smart search for your next home — powered by AI.
    </h1>
    <p style="
        margin:0 0 18px 0;
        opacity:0.96;
        font-size:16px;
        max-width:720px;
    ">
        Neighborhood insights, investor-grade numbers, repair tools, moving resources,
        and first-time buyer help — all in one experience built for real people.
    </p>

    <!-- Tag pills row -->
    <div style="margin-top:10px;">
        <span style="
            padding:8px 14px;
            background:#15d2e9;
            border-radius:999px;
            margin-right:8px;
            font-size:12px;
            font-weight:500;
        ">
            First-time buyer friendly
        </span>
        <span style="
            padding:8px 14px;
            background:#15d2e9;
            border-radius:999px;
            margin-right:8px;
            font-size:12px;
            font-weight:500;
        ">
            Investor deal analysis
        </span>
        <span style="
            padding:8px 14px;
            background:#15d2e9;
            border-radius:999px;
            margin-right:8px;
            font-size:12px;
            font-weight:500;
        ">
            Neighborhood insights
        </span>
        <span style="
            padding:8px 14px;
            background:#15d2e9;
            border-radius:999px;
            margin-right:8px;
            font-size:12px;
            font-weight:500;
        ">
            Repair estimator
        </span>
        <span style="
            padding:8px 14px;
            background:#15d2e9;
            border-radius:999px;
            font-size:12px;
            font-weight:500;
        ">
            Rent &amp; moving tools
        </span>
    </div>

    <!-- Search bar row -->
    <div style="
        background:white;
        border-radius:999px;
        padding:10px 10px 10px 20px;
        margin-top:22px;
        display:flex;
        align-items:center;
        gap:10px;
    ">
        <input
            placeholder="Search city, neighborhood, or ZIP"
            style="
                border:none;
                outline:none;
                flex:1;
                font-size:14px;
            "
        />
        <button style="
            background:#006d77;
            color:white;
            border:none;
            border-radius:999px;
            padding:8px 26px;
            font-weight:600;
            font-size:14px;
            cursor:pointer;
        ">
            Search
        </button>
    </div>

    <div style="margin-top:6px;font-size:12px;opacity:0.9;">
        Your AI-powered home search companion for smarter buying.
    </div>
</div>
"""

st.markdown(hero_html, unsafe_allow_html=True)

# =========================================================
# HOME PAGE CONTENT (TRENDING + MAP)
# =========================================================
def render_home():
    st.markdown(
        '<h3 style="margin-top:28px;margin-bottom:16px;">Trending homes near you</h3>',
        unsafe_allow_html=True,
    )

    # Fake listing data just for demo
    listing = {
        "price": "$579,900",
        "beds": "4 bd",
        "baths": "3 ba",
        "sqft": "2,580 sq ft",
        "location": "Downtown, Detroit, MI",
        "score": 88,
        "est_value": "$340,000",
        "growth": "+5.2%",
    }

    col_map, col_card = st.columns([1.2, 1])

    # Left: interactive map (scatter points around Detroit)
    with col_map:
        st.markdown(
            """
            <div style="font-size:15px;font-weight:600;margin-bottom:4px;">
                Neighborhood snapshot
            </div>
            <div style="font-size:12px;color:#6b7b88;margin-bottom:6px;">
                Safety, price, and walkability at a glance — demo map.
            </div>
            """,
            unsafe_allow_html=True,
        )

        center_lat, center_lon = 42.3314, -83.0458  # Detroit
        np.random.seed(7)
        map_df = pd.DataFrame(
            {
                "lat": center_lat + 0.12 * np.random.randn(200),
                "lon": center_lon + 0.18 * np.random.randn(200),
            }
        )
        st.map(map_df, use_container_width=True)

    # Right: featured listing card
    with col_card:
        st.markdown(
            """
            <div style="
                background:white;
                border-radius:16px;
                box-shadow:0 10px 24px rgba(0,0,0,0.10);
                overflow:hidden;
            ">
                <div style="height:210px;background:#dfe7ef;
                    background-image:url('https://placehold.co/800x500?text=HomePathAI+Listing');
                    background-size:cover;
                    background-position:center;">
                </div>
                <div style="padding:16px 18px 14px 18px;">
                    <div style="font-size:22px;font-weight:700;margin-bottom:4px;">
                        $579,900
                    </div>
                    <div style="font-size:13px;color:#4b5563;margin-bottom:2px;">
                        4 bd | 3 ba | 2,580 sq ft
                    </div>
                    <div style="font-size:12px;color:#6b7280;margin-bottom:10px;">
                        Downtown, Detroit, MI
                    </div>

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        font-size:12px;
                        margin-bottom:12px;
                    ">
                        <div>
                            <div style="text-transform:uppercase;font-size:10px;color:#9ca3af;">
                                HomePathAI score
                            </div>
                            <div style="font-weight:600;">88</div>
                        </div>
                        <div>
                            <div style="text-transform:uppercase;font-size:10px;color:#9ca3af;">
                                Est. value
                            </div>
                            <div style="font-weight:600;">$340,000</div>
                        </div>
                        <div>
                            <div style="text-transform:uppercase;font-size:10px;color:#9ca3af;">
                                5-yr growth
                            </div>
                            <div style="font-weight:600;color:#059669;">+5.2%</div>
                        </div>
                    </div>

                    <button style="
                        background:#006d77;
                        color:white;
                        border:none;
                        border-radius:999px;
                        padding:7px 20px;
                        font-size:13px;
                        font-weight:600;
                        cursor:pointer;
                    ">
                        Constrain this deal
                    </button>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        "<div style='height:40px;'></div>",
        unsafe_allow_html=True,
    )


# =========================================================
# OTHER PAGES (SIMPLE PLACEHOLDERS BUT CLICKABLE)
# =========================================================
def render_buyer():
    st.subheader("First-time buyer guide (demo)")
    st.write(
        "This section will walk buyers through pre-approval, budget, "
        "trade-offs, and closing steps. In the real version, we’ll plug in "
        "your lender tools and education content."
    )


def render_investor():
    st.subheader("Investor deal analysis (demo)")
    st.write(
        "Quick cap rate, cash-on-cash, and flip / BRRRR calculations. "
        "Here we’ll connect to your real deal analyzer later."
    )


def render_neighbor():
    st.subheader("Neighbor insights (demo)")
    st.write(
        "Compare neighborhoods on safety, schools, price trends, and amenities. "
        "For now this is just a placeholder view."
    )


def render_repair():
    st.subheader("Repair estimator (demo)")
    st.write(
        "This will show your repair cost breakdown screen (like the screenshot "
        "you have) once we wire in the estimator model."
    )


def render_rent():
    st.subheader("Rent & moving tools (demo)")
    st.write(
        "Estimate rent ranges, moving costs, and compare renting vs buying."
    )


# =========================================================
# ROUTER: WHICH PAGE TO SHOW
# =========================================================
page = st.session_state["active_page"]

if page == "Home":
    render_home()
elif page == "Buyer":
    render_buyer()
elif page == "Investor":
    render_investor()
elif page == "Neighbor":
    render_neighbor()
elif page == "Repair":
    render_repair()
elif page == "Rent":
    render_rent()
else:
    # Fallback
    render_home()







