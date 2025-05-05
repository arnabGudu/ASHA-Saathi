import streamlit as st
from streamlit_option_menu import option_menu
from routes import login, dashboard, visit

st.session_state.setdefault("page", "Login")
st.session_state.setdefault("user", None)

def page_router():
    page = st.session_state["page"]
    if page == "Login":
        login.show()
    elif page == "Dashboard":
        dashboard.show()
    elif page == "Visit":
        visit.show()
    elif page == "Logout":
        st.session_state.clear()
        st.session_state.page = "Login"
        st.rerun()
    else:
        st.warning("Unknown page")

def on_change(key):
    st.session_state.page = st.session_state[key]

def sidebar_menu():
    options = ["Dashboard", "Visit", "Logout"]
    icons = ["list-task", "mic", "person"]

    with st.sidebar:
        selected = option_menu(
            "ASHA-Sathi",
            options,
            icons=icons,
            menu_icon="hospital",
            key="menu_selector",
            default_index=0,
            manual_select=options.index(st.session_state.page),
            on_change=on_change,
        )

if st.session_state.page != "Login":
    sidebar_menu()

page_router()
