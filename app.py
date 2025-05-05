import streamlit as st
from streamlit_option_menu import option_menu
from routes import login, dashboard, visit

if "page" not in st.session_state:
    st.session_state.page = "Login"

if st.session_state.page == "Login":
    login.show()
else:
    with st.sidebar:
        options = ["Dashboard", "Visit", "Logout"]
        selected = option_menu("ASHA-Sathi", options, 
            icons=["list-task", "mic", "person"], menu_icon="hospital",
            default_index=options.index(st.session_state.page)
        )

    st.session_state.page = selected

    if st.session_state.page == "Dashboard":
        dashboard.show()
    elif st.session_state.page == "Visit":
        visit.show()
    elif st.session_state.page == "Logout":
        st.session_state.clear()
