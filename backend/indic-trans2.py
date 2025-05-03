import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()

url = "https://infer.e2enetworks.net/project/p-5482/v1/indic_trans_2/infer"

payload = json.dumps({
  "inputs": [
    {
      "name": "prompt",
      "shape": [
        1,
        1
      ],
      "datatype": "BYTES",
      "data": [
        "The model will produce a response according to the parameters configured."
      ]
    },
    {
      "name": "INPUT_LANGUAGE_ID",
      "shape": [
        1,
        1
      ],
      "datatype": "BYTES",
      "data": [
        "en"
      ]
    },
    {
      "name": "OUTPUT_LANGUAGE_ID",
      "shape": [
        1,
        1
      ],
      "datatype": "BYTES",
      "data": [
        "hi"
      ]
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

print(response.text)