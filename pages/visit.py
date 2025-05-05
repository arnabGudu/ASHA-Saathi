import streamlit as st
from components.audio_recorder import record_audio
# from services.whisper_stt import get_transcript
# from services.llama_med42 import get_suggestion
import requests

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

    audio_path = record_audio()

    if st.button("🧠 Analyze Conversation"):
        st.info("Sending audio to backend and analyzing...")

        # transcript = get_transcript()
        # if transcript:
        #     suggestions = get_suggestion(transcript)
        #     st.success("✅ Analysis Complete")
        #     st.markdown(suggestions)
        # else:
        #     st.error("Analysis failed. Check backend logs.")
        
        # with open(audio_path, "rb") as f:
        #     files = {"file": f}
        
        response = requests.post("http://localhost:8000/analyze")#, files=files)

        if response.status_code == 200:
            data = response.json()
            st.success("✅ Analysis Complete")
            st.markdown(data)

        #     st.markdown("### 📊 Risk Analysis")
        #     st.json(data.get("structured_data", {}))

        #     st.markdown("### 🥗 Dietary Recommendations")
        #     st.write(data.get("diet_recommendations", "No recommendations"))

        #     st.markdown("### 🔊 Hindi Audio Advice")
        #     st.audio(data.get("audio_url"))  # Replace with actual audio output URL

        
