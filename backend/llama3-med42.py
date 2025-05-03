from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Read the token from environment variables
access_token = os.getenv("E2E_TIR_ACCESS_TOKEN")
if not access_token:
    raise ValueError("E2E_TIR_ACCESS_TOKEN environment variable is not set.")


client = OpenAI(
  base_url = "https://infer.e2enetworks.net/project/p-5482/genai/llama3-med42-8b/v1",
  api_key = access_token
)

completion = client.chat.completions.create(
    model='llama3-med42-8b',
    messages=[{"role":"user","content":"Can you write a poem about open source machine learning?"}],
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=1,
    stream=True
  )

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

