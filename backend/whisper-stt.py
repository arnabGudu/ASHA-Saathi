import os
from dotenv import load_dotenv
from e2enetworks.cloud import tir

load_dotenv()

team_id = os.getenv("E2E_TIR_TEAM_ID")
project_id = os.getenv("E2E_TIR_PROJECT_ID")
api_key = os.getenv("E2E_TIR_API_KEY")
access_token = os.getenv("E2E_TIR_ACCESS_TOKEN")

if not (team_id and project_id and api_key and access_token):
    raise ValueError("One or more environment variables are not set. "
                     "Please ensure E2E_TIR_TEAM_ID, E2E_TIR_PROJECT_ID, "
                     "E2E_TIR_API_KEY, and E2E_TIR_ACCESS_TOKEN are set.") 

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