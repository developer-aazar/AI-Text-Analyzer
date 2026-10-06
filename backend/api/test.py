from schemas.correction_schema import AIAnalysisResponse

result = {
    "corrected_text": "I am going to school.",
    "grammar_mistakes": "No mistakes",
    "spelling_mistakes": [],
    "punctuation_mistakes": []
}

validated_result = AIAnalysisResponse(**result)

print(validated_result)