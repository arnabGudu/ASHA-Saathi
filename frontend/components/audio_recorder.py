import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
import av
import numpy as np
import wave
import io
import tempfile
import os
from uuid import uuid4

# Global buffer to hold audio chunks
_audio_buffer = []

class AudioProcessor(AudioProcessorBase):
    def recv_queued(self, frame: av.AudioFrame) -> av.AudioFrame:
        pcm = frame.to_ndarray()
        _audio_buffer.append(pcm)
        return frame

def record_audio():
    st.subheader("🎤 Record Patient Conversation")

    webrtc_ctx = webrtc_streamer(
        key="mobile-audio-recorder",
        mode=WebRtcMode.SENDONLY,
        audio_receiver_size=1024,
        audio_processor_factory=AudioProcessor,
        media_stream_constraints = {"audio": True, "video": False},
    )

    audio_file_path = None

    if st.button("🛑 Stop & Save Audio"):
        if _audio_buffer:
            # Convert audio buffer to WAV
            wav_buffer = io.BytesIO()
            with wave.open(wav_buffer, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(48000)
                audio_data = np.concatenate(_audio_buffer).astype(np.int16).tobytes()
                wf.writeframes(audio_data)
            wav_buffer.seek(0)

            # Save to a temp file
            temp_dir = tempfile.gettempdir()
            filename = f"{uuid4().hex}.wav"
            audio_file_path = os.path.join(temp_dir, filename)
            with open(audio_file_path, "wb") as f:
                f.write(wav_buffer.read())

            st.audio(audio_file_path, format="audio/wav")
            st.success("Audio saved successfully.")

            # Clear buffer for next recording
            _audio_buffer.clear()
        else:
            st.warning("No audio recorded.")

    return audio_file_path
