# frontend/pages/visit.py
import streamlit as st

def show():
    st.title("🩺 Patient Visit")

    patient = st.session_state.get("selected_patient")
    if not patient:
        st.warning("No patient selected. Go back to the dashboard.")
        return

    st.subheader(f"Visiting: {patient['name']}")
    st.write(f"""
    - Age: {patient['age']}
    - Village: {patient['village']}
    - Pregnancy Month: {patient['month']}
    """)
    
    # Placeholder: Add audio recorder + analysis here
