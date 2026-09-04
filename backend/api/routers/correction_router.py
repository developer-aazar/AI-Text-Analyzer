from fastapi import APIRouter
from api.schemas.correction_schema import CorrectionRequest , CorrectionResponse
from api.services.ai_service import correct_text

router = APIRouter()

@router.post("/correct" , response_model=CorrectionResponse)
def correct(request: CorrectionRequest):

    result = correct_text(request.text)

    return CorrectionResponse(
        original_text=request.text,
        corrected_text=result["corrected_text"],
        grammar_mistakes=result["grammar_mistakes"],
        spelling_mistakes=result["spelling_mistakes"],
        punctuation_mistakes=result["punctuation_mistakes"]
    )

