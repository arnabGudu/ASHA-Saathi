import streamlit as st
from data.dummy_data import USERS

def show():
    with st.form('login_form'):
        st.title("🔐 ASHA-Sathi Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.form_submit_button("Login"):
            user = USERS.get(username)
            if user and user["password"] == password:
                st.session_state["user"] = user
                st.success(f"Welcome, {user['name']}!")
                st.session_state.page = "Dashboard"
                st.rerun()
            else:
                st.error("Invalid credentials")
