
HomePathAI Demo (Streamlit) - Investor Upload ZIP

Files included:
- app.py (Streamlit app)
- integrations.py (API placeholders)
- api_config.py (placeholder keys)
- assets/logo.svg (simple logo)
- requirements.txt

How to deploy to Streamlit Cloud:
1. Create a new GitHub repo and push these files.
2. Go to https://share.streamlit.io/ and 'New app' -> pick the repo + app.py
3. Add any API keys in the app's Secrets (if using live mode)
4. Deploy and share the public link with investors.

Local run (devs only):
pip install -r requirements.txt
streamlit run app.py
