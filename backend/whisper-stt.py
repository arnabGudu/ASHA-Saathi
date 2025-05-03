import os
from dotenv import load_dotenv
from e2enetworks.cloud import tir

load_dotenv()

access_token = os.getenv("E2E_TIR_ACCESS_TOKEN")
if not access_token:
    raise ValueError("E2E_TIR_ACCESS_TOKEN environment variable is not set.")
api_key = os.getenv("E2E_TIR_API_KEY")
if not api_key:
    raise ValueError("E2E_TIR_API_KEY environment variable is not set.")

os.environ["E2E_TIR_ACCESS_TOKEN"] = access_token
os.environ["E2E_TIR_API_KEY"] = api_key
os.environ["E2E_TIR_PROJECT_ID"] = "5482"
os.environ["E2E_TIR_TEAM_ID"] = "4459"

tir.init()
client = tir.ModelAPIClient()
data = {"input": "/mnt/data/5482-1746313233-recording.wav",
        "language": "English",
        "task": "transcribe",
        "max_new_tokens": 400,
        "return_timestamps": "none"
}

output = client.infer(model_name="whisper-large-v3", data=data)
print(output)