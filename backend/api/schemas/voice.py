from pydantic import BaseModel

from api.schemas.correction_schema import AnalysisIssue


class VoiceAnalysisResponse(BaseModel):
	transcript: str
	corrected_text: str
	issues: list[AnalysisIssue]
