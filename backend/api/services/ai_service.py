from google import genai
from api.core.config import settings
import json

def call_ai(prompt):

    client = genai.Client(api_key=settings.ai_api_key)

    response = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    raw_output = response.output_text.strip()

    if raw_output.startswith("```json"):
        raw_output = raw_output[7:]

    if raw_output.endswith("```"):
            raw_output = raw_output[:-3]

    result = json.loads(raw_output)

    return result

def correct_text(text: str):
    prompt = f"""
    Act as a senior text analyzer you task is to analyze the following text and identify:
    1. Grammatical mistakes
    2. Spelling mistakes
    3. Punctuation mistakes

    Also provide the fully corrected version of the text.

    For every mistake, provide:
    1. the original mistake
    2. the correction

    Return the result only as valid JSON using exactly this structure:
    {{
        "corrected_text": "corrected version here",
        "grammar_mistakes": [
            {{
                "mistake": "original mistake",
                "correction": "correct version"
            }}
        ],
        "spelling_mistakes": [
            {{
                "mistake": "original mistake",
                "correction": "correct version"
            }}
        ],
        "punctuation_mistakes": [
            {{
                "mistake": "original mistake",
                "correction": "correct version"
            }}
        ]
    }}
    If there are no mistakes in any category, always return an empty list [] never return "no mistakes found", "none", or any other string.
    Text:
    {text}
    """
    corrected_text = call_ai(prompt)
    return corrected_text
    



