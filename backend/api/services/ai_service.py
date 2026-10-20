import logging
import re

from fastapi import HTTPException
from google import genai
from google.genai import types

from api.core.config import settings
from api.schemas.correction_schema import (
    AIAnalysisResponse,
    AnalysisIssue,
    AnalyzeResponse,
    CorrectionResponse,
)

logger = logging.getLogger(__name__)


def call_ai(prompt):
    if not settings.ai_api_key:
        raise HTTPException(status_code=503, detail="AI_API_KEY is not configured on the server.")
    try:
        with genai.Client(api_key=settings.ai_api_key) as client:
            response = client.models.generate_content(
                model=settings.ai_model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=AIAnalysisResponse,
                ),
            )
        if response.parsed is not None:
            return AIAnalysisResponse.model_validate(response.parsed)

        raw_output = (response.text or "").strip()
        raw_output = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw_output, flags=re.IGNORECASE)
        return AIAnalysisResponse.model_validate_json(raw_output)
    except HTTPException:
        raise
    except ValueError as exc:
        raise HTTPException(status_code=502, detail="The AI service returned an invalid analysis.") from exc
    except Exception as exc:
        logger.exception("Gemini analysis request failed")
        raise HTTPException(status_code=502, detail="The AI analysis service is unavailable.") from exc


def analyze_text(text: str) -> AnalyzeResponse:
    prompt = f"""
    Analyze the text for spelling, grammar, and punctuation mistakes, then provide
    a fully corrected version. For each issue include the exact original text,
    its replacement, and a short explanation. Do not report stylistic preferences
    as errors. Return only JSON matching this structure:
    {{
        "corrected_text": "corrected version here",
        "grammar_mistakes": [
            {{
                "mistake": "original mistake",
                "correction": "correct version",
                "explanation": "brief reason"
            }}
        ],
        "spelling_mistakes": [
            {{
                "mistake": "original mistake",
                "correction": "correct version",
                "explanation": "brief reason"
            }}
        ],
        "punctuation_mistakes": [
            {{
                "mistake": "original mistake",
                "correction": "correct version",
                "explanation": "brief reason"
            }}
        ]
    }}
    Return an empty list for categories with no mistakes. Keep every original snippet
    exactly as it appears in the input. If there are no mistakes, corrected_text must
    equal the input text.
    Text:
    {text}
    """

    analysis = call_ai(prompt)
    issues = []
    for issue_type, mistakes in (
        ("grammar", analysis.grammar_mistakes),
        ("spelling", analysis.spelling_mistakes),
        ("punctuation", analysis.punctuation_mistakes),
    ):
        issues.extend(
            AnalysisIssue(
                type=issue_type,
                original=mistake.mistake,
                suggestion=mistake.correction,
                explanation=mistake.explanation,
            )
            for mistake in mistakes
        )
    return AnalyzeResponse(corrected_text=analysis.corrected_text, issues=issues)


def correct_text(text: str) -> CorrectionResponse:
    prompt = f"""
    Correct spelling, grammar, and punctuation in the text. Preserve its meaning
    and style. Return only valid JSON with corrected_text and grammar_mistakes,
    spelling_mistakes, and punctuation_mistakes arrays. Each mistake must contain
    mistake, correction, and explanation. Use empty arrays when there are no issues.
    Text:
    {text}
    """
    analysis = call_ai(prompt)

    return CorrectionResponse(
        original_text=text,
        corrected_text=analysis.corrected_text,
        grammar_mistakes=analysis.grammar_mistakes,
        spelling_mistakes=analysis.spelling_mistakes,
        punctuation_mistakes=analysis.punctuation_mistakes
    )




