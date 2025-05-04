# # frontend/app.py
# import streamlit as st
# from streamlit_option_menu import option_menu

# st.set_page_config(page_title="ASHA-Sathi", layout="wide")

# # Check for query param override
# query_params = st.get_query_params()
# default_page = query_params.get("page", ["Login"])[0]

# with st.sidebar:
#     selected = option_menu("ASHA-Sathi", ["Login", "Dashboard", "Visit", "History"], 
#         icons=["person", "list-task", "mic", "clock"], menu_icon="hospital", default_index=0)

# # Use URL param override if present
# selected = default_page if default_page in ["Login", "Dashboard", "Visit", "History"] else selected


# if selected == "Login":
#     from pages import login
#     login.show()

# elif selected == "Dashboard":
#     from pages import dashboard
#     dashboard.show()

# elif selected == "Visit":
#     from pages import visit
#     visit.show()

# elif selected == "History":
#     from pages import history
#     history.show()

import streamlit as st
from streamlit_option_menu import option_menu
from pages import login, dashboard, visit

st.set_page_config(page_title="ASHA-Sathi", layout="wide")

# Get query param for navigation
query_params = st.query_params
print(query_params)
default_page = query_params.get("page", ["Login"])[0]

with st.sidebar:
    selected = option_menu("ASHA-Sathi", ["Login", "Dashboard", "Visit", "History"], 
        icons=["person", "list-task", "mic", "clock"], menu_icon="hospital", default_index=0)

# Override sidebar nav with URL param if provided
if default_page in ["Login", "Dashboard", "Visit", "History"]:
    selected = default_page

# Route to page
if selected == "Login":
    login.show()
elif selected == "Dashboard":
    dashboard.show()
elif selected == "Visit":
    visit.show()
else:
    st.info("Page under construction.")
