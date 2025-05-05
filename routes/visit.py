import streamlit as st
from services.audio_recorder import record_audio
from services.whisper_stt import get_transcript
from services.llama_med42 import get_suggestion

def show():
    if "audio_path" not in st.session_state:
        st.session_state.audio_path = None

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

    if audio_path:
        st.session_state.audio_path = audio_path

    if st.session_state.audio_path and st.button("🧠 Analyze Conversation"):
        st.info("Sending audio to backend and analyzing...")

        transcript = get_transcript()
        if transcript:
            suggestions = get_suggestion(transcript)
            st.success("✅ Analysis Complete")
            st.markdown(suggestions)

            # st.markdown("### 📊 Risk Analysis")
            # st.json(data.get("structured_data", {}))

            # st.markdown("### 🥗 Dietary Recommendations")
            # st.write(data.get("diet_recommendations", "No recommendations"))

            # st.markdown("### 🔊 Hindi Audio Advice")
            # st.audio(data.get("audio_url"))  # Replace with actual audio output URL
        else:
            st.error("Analysis failed. Check backend logs.")

