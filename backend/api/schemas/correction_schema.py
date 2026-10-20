from typing import Literal

from pydantic import BaseModel, Field

class CorrectionRequest(BaseModel):
    text: str = Field(min_length=1, max_length=10_000)

class Mistake(BaseModel):
    mistake: str
    correction: str
    explanation: str = ""


class AnalysisIssue(BaseModel):
    type: Literal["spelling", "grammar", "punctuation"]
    original: str
    suggestion: str
    explanation: str = ""


class AnalyzeResponse(BaseModel):
    corrected_text: str
    issues: list[AnalysisIssue]


class DocumentAnalysisResponse(AnalyzeResponse):
    filename: str
    original_text: str

class CorrectionResponse(BaseModel):
    original_text: str
    corrected_text: str
    grammar_mistakes: list[Mistake]
    spelling_mistakes: list[Mistake]
    punctuation_mistakes: list[Mistake]


class AIAnalysisResponse(BaseModel):
    corrected_text: str
    grammar_mistakes: list[Mistake] = Field(default_factory=list)
    spelling_mistakes: list[Mistake] = Field(default_factory=list)
    punctuation_mistakes: list[Mistake] = Field(default_factory=list)