# frontend/app.py
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="ASHA-Sathi", layout="wide")

# Check for query param override
query_params = st.experimental_get_query_params()
default_page = query_params.get("page", ["Login"])[0]

with st.sidebar:
    selected = option_menu("ASHA-Sathi", ["Login", "Dashboard", "Visit", "History"], 
        icons=["person", "list-task", "mic", "clock"], menu_icon="hospital", default_index=0)

# Use URL param override if present
selected = default_page if default_page in ["Login", "Dashboard", "Visit", "History"] else selected


if selected == "Login":
    from pages import login
    login.show()

elif selected == "Dashboard":
    from pages import dashboard
    dashboard.show()

elif selected == "Visit":
    from pages import visit
    visit.show()

elif selected == "History":
    from pages import history
    history.show()
