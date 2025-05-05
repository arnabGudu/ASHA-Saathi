from openai import OpenAI
import os
from dotenv import load_dotenv

def get_suggestion(transcript: str):
    load_dotenv()

    access_token = os.getenv("E2E_TIR_ACCESS_TOKEN")
    if not access_token:
        raise ValueError("E2E_TIR_ACCESS_TOKEN environment variable is not set.")

    client = OpenAI(
        base_url = "https://infer.e2enetworks.net/project/p-5482/genai/llama3-med42-8b/v1",
        api_key = access_token
    )

    system_prompt = '''
You are a medical AI assistant trained in prenatal care and micronutrient analysis.
Your task to analyze a transcription of a conversation between an ASHA (community health worker) and a pregnant woman in rural India. Based on the symptoms mentioned by the patient, analyze and produce a table with the following columns:
| Symptom | Possible Deficiency / Complication | Recommended Diet |
|--------|-------------------------------------|------------------|

Reference for nutrient source -
| Nutrient   | RDA         | Food Sources |
|------------|-------------|--------------|
| **Iron**   | 38 mg       | Dark green leafy vegetables, red meat, whole pulses, legumes, beans, tofu/paneer, beets, eggs, citrus fruits, broccoli, Brussels sprouts, dried fruits, and nuts. |
| **Folate** | 600 mcg     | [Sources not listed in original; assume leafy greens, citrus fruits, beans] |
| **Calcium**| 1000 mg     | Milk & milk products, whole cereals, millets (Ragi), oilseeds (sesame seeds) |
| **Iodine** | 220 mcg     | Seafood, iodized salt |
| **Vitamin A** | 3300-5000 IU | Liver, fish oils, milk, egg yolk, leafy vegetables, yellow/orange fruits and vegetables |
| **Zinc**   | 11 mg       | Nuts, beans, and fortified cereals |

Transcription -
'''

    completion = client.chat.completions.create(
        model='llama3-med42-8b',
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcript}
        ],
        temperature=0,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=1,
        stream=False
    )

    data = completion.choices[0].message.content
    return data
