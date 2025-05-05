import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import av
import numpy as np
import wave
import os
from uuid import uuid4

audio_frames = []

class AudioProcessor:
    def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
        audio = frame.to_ndarray()
        audio_frames.append(audio)
        return frame

def record_audio():
    st.title("🎙️ Record Audio and Save on Stop")

    webrtc_ctx = webrtc_streamer(
        key="audio-recorder",
        mode=WebRtcMode.SENDONLY,
        audio_receiver_size=1024,
        audio_processor_factory=AudioProcessor,
        media_stream_constraints={"audio": True, "video": False},
    )

    if not webrtc_ctx.state.playing and audio_frames:
        audio_data = np.concatenate(audio_frames, axis=1)[0].astype(np.int16)

        file_path = os.path.join('data/recordings/', f"{uuid4().hex}.wav")

        with wave.open(file_path, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(48000)
            wf.writeframes(audio_data.tobytes())

        audio_frames.clear()
        return file_path
