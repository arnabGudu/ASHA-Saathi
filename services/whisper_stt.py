import os
from dotenv import load_dotenv
from e2enetworks.cloud import tir

def get_transcript(file: str = "data/conversation.wav"):
    load_dotenv()

    team_id = os.getenv("E2E_TIR_TEAM_ID")
    project_id = os.getenv("E2E_TIR_PROJECT_ID")
    api_key = os.getenv("E2E_TIR_API_KEY")
    access_token = os.getenv("E2E_TIR_ACCESS_TOKEN")

    if not (team_id and project_id and api_key and access_token):
        raise ValueError(
            "One or more environment variables are not set. "
            "Please ensure E2E_TIR_TEAM_ID, E2E_TIR_PROJECT_ID, "
            "E2E_TIR_API_KEY, and E2E_TIR_ACCESS_TOKEN are set."
        )

    tir.init()
    client = tir.ModelAPIClient()
    data = {
        "input": file,
        "language": "English",
        "task": "transcribe",
        "max_new_tokens": 400,
        "return_timestamps": "none"
    }

    response = client.infer(model_name="whisper-large-v3", data=data)
    
    if response[0]:
        outputs = response[1].outputs
        generated_text_data = outputs[0].data[0]
    
    return generated_text_data
