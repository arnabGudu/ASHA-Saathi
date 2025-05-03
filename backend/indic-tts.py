import io
import json
import requests
import os

import numpy as np
from scipy.io.wavfile import write as scipy_wav_write

from dotenv import load_dotenv


load_dotenv()

url = "https://infer.e2enetworks.net/project/p-5482/v1/indic_tts/infer"

payload = json.dumps({
    "inputs": [
        {
            "name": "INPUT_TEXT",
            "shape": [1],
            "datatype": "BYTES",
            "data": [
                "The model will produce a response according to the parameters configured."
            ]
        },
        {
            "name": "INPUT_SPEAKER_ID",
            "shape": [1],
            "datatype": "BYTES",
            "data": ["female"]
        },
        {
            "name": "INPUT_LANGUAGE_ID",
            "shape": [1],
            "datatype": "BYTES",
            "data": ["en+hi"]
        }
    ]
})

# Read the token from environment variables
access_token = os.getenv("E2E_TIR_ACCESS_TOKEN")
if not access_token:
    raise ValueError("E2E_TIR_ACCESS_TOKEN environment variable is not set.")

headers = {
    'authorization': f'Bearer {access_token}',
    'content-type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

if response.status_code == 200:
    DEFAULT_SAMPLING_RATE = 22050
    audio_arr = json.loads(response.text)["outputs"][0]["data"]
    raw_audio = np.array(audio_arr, dtype=np.float32)
    byte_io = io.BytesIO()
    scipy_wav_write(byte_io, DEFAULT_SAMPLING_RATE, raw_audio)
    with open("audio.wav", "wb") as f:
        f.write(byte_io.read())
else:
    print(f"Error: {response.status_code}, {response.text}")