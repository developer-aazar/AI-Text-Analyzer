from fastapi import HTTPException
from google import genai
from google.genai import types

from api.core.config import settings


def transcribe_audio(audio: bytes, mime_type: str) -> str:
	if not settings.ai_api_key:
		raise HTTPException(status_code=503, detail="AI_API_KEY is not configured on the server.")

	client = genai.Client(api_key=settings.ai_api_key)
	try:
		response = client.models.generate_content(
			model=settings.ai_model,
			contents=[
				"Transcribe the spoken audio verbatim. Return only the transcript, without labels or commentary.",
				types.Part.from_bytes(data=audio, mime_type=mime_type),
			],
		)
	except Exception as exc:
		raise HTTPException(status_code=502, detail="The audio transcription service is unavailable.") from exc

	transcript = (response.text or "").strip()
	if not transcript:
		raise HTTPException(status_code=422, detail="No speech could be transcribed from this audio.")
	return transcript
