from fastapi import FastAPI, File, UploadFile
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from services.whisper_stt import get_transcript
from services.llama_med42 import get_suggestion
import tempfile
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/analyze")
async def analyze(file: Optional[UploadFile] = File(None)):
    if file:
        contents = await file.read()
        file_extension = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
            temp_file.write(contents)
            temp_file_path = temp_file.name
        # transcript = get_transcript(os.path.abspath(temp_file_path))
        transcript = get_transcript()
    else:
        transcript = get_transcript()
    result = get_suggestion(transcript)
    return result
