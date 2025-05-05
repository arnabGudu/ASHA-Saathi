# # frontend/pages/dashboard.py
# import streamlit as st
# from frontend.data.dummy_data import PREGNANT_WOMEN

# def show():
#     st.title("📋 Dashboard - Pregnant Women Assigned")

#     user = st.session_state.get("user")
#     if not user:
#         st.warning("Please login first.")
#         return

#     st.subheader(f"Welcome, {user['name']} 👩‍⚕️")
#     women_list = PREGNANT_WOMEN.get(user["id"], [])

#     if not women_list:
#         st.info("No patients assigned.")
#         return

#     for woman in women_list:
#         col1, col2 = st.columns([4, 1])
#         with col1:
#             st.markdown(f"""
#             **{woman['name']}** ({woman['age']} yrs)  
#             🏡 *{woman['village']}*  
#             🤰 *Pregnancy Month: {woman['month']}*
#             """)
#         with col2:
#             if st.button("Visit", key=woman["id"]):
#                 st.session_state["selected_patient"] = woman
#                 st.set_query_params(page="Visit")
#                 st.rerun()

import streamlit as st
from data.dummy_data import PREGNANT_WOMEN

def show():
    st.title("📋 Dashboard - Pregnant Women Assigned")

    user = st.session_state.get("user")
    if not user:
        st.warning("Please login first.")
        return

    st.subheader(f"Welcome, {user['name']} 👩‍⚕️")
    women_list = PREGNANT_WOMEN.get(user["id"], [])

    if not women_list:
        st.info("No patients assigned.")
        return

    for woman in women_list:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""
            **{woman['name']}** ({woman['age']} yrs)  
            🏡 *{woman['village']}*  
            🤰 *Pregnancy Month: {woman['month']}*
            """)
        with col2:
            if st.button("Visit", key=woman["id"]):
                st.session_state["selected_patient"] = woman
                st.query_params["page"]="Visit"
                st.rerun()
