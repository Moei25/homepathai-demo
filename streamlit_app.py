def page_home():

    # HERO SECTION (corrected, safe HTML)
    st.markdown("""
    <div class="hp-hero">

        <h2 style="margin-bottom:6px;">Smart search for your next home — powered by AI.</h2>
        <p>Neighborhood insights, investor-grade numbers, repair tools,
           and first-time buyer help — all in one place.</p>

        <div style="display:flex; gap:12px; margin-top:18px;">
            <input class="hp-hero-input" type="text" placeholder="Search city, neighborhood, or ZIP" />
            <button class="hp-hero-btn">Search</button>
        </div>

    </div>
    """, unsafe_allow_html=True)

    # SECTION TITLE
    st.markdown("### 🔥 Trending homes near you")
    st.caption("Sample homes across Detroit — demo data only.")

    # MAP + LISTING
    left, right = st.columns([1.3, 1])

    with left:

        st.markdown("#### Neighborhood snapshot")
        df = pd.DataFrame({
            "lat": np.random.uniform(42.28, 42.42, 200),
            "lon": np.random.uniform(-83.5, -83.0, 200),
            "value": np.random.uniform(0, 1, 200)
        })

        layer = pdk.Layer(
            "HeatmapLayer",
            df,
            get_position='[lon, lat]',
            threshold=0.2,
            opacity=0.8
        )

        deck = pdk.Deck(
            layers=[layer],
            initial_view_state=pdk.ViewState(
                latitude=42.33,
                longitude=-83.1,
                zoom=9,
                pitch=40,
            )
        )
        st.pydeck_chart(deck)

    # LISTING CARD (fixed HTML)
    with right:
        st.markdown("""
        <div class="hp-card">

            <img src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg"
                 style="width:100%; border-radius:12px; margin-bottom:12px;" />

            <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
                <div>
                    <div style="font-size:22px; font-weight:700;">$579,900</div>
                    <div>4 bd | 3 ba | 2,580 sq ft</div>
                    <div>Downtown, Detroit, MI</div>
                </div>
                <button class="hp-hero-btn" style="padding:10px 18px;">Constrain</button>
            </div>

            <div style="display:flex; justify-content:space-between; margin-top:12px;">
                <div>
                    <div class="hp-label">HomePath score</div>
                    <div class="hp-value">88</div>
                </div>
                <div>
                    <div class="hp-label">Est. value</div>
                    <div class="hp-value">$340,000</div>
                </div>
                <div>
                    <div class="hp-label">5-yr growth</div>
                    <div class="hp-value" style="color:#0B9D4A;">+5.2%</div>
                </div>
            </div>

        </div>
        """, unsafe_allow_html=True)















