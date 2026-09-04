from pydantic import BaseModel, Field

class CorrectionRequest(BaseModel):
    text: str = Field(min_length=5, max_length=200)

class Mistake(BaseModel):
    mistake: str
    correction: str

class CorrectionResponse(BaseModel):
    original_text: str
    corrected_text: str
    grammar_mistakes: list[Mistake]
    spelling_mistakes: list[Mistake]
    punctuation_mistakes: list[Mistake]


