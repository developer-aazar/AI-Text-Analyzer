from io import BytesIO
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile
from pypdf import PdfReader

from api.schemas.correction_schema import (
    AnalyzeResponse,
    CorrectionRequest,
    CorrectionResponse,
    DocumentAnalysisResponse,
)
from api.schemas.voice import VoiceAnalysisResponse
from api.services.ai_service import analyze_text, correct_text
from api.services.voice import transcribe_audio

router = APIRouter()
MAX_AUDIO_BYTES = 20 * 1024 * 1024
MAX_DOCUMENT_BYTES = 400_000
MAX_TEXT_LENGTH = 10_000


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: CorrectionRequest):
    return analyze_text(request.text)


@router.post("/analyze-audio", response_model=VoiceAnalysisResponse)
async def analyze_audio(file: UploadFile = File(...)):
    filename = file.filename or "audio"
    extension = Path(filename).suffix.lower()
    allowed_extensions = {".aac", ".flac", ".m4a", ".mp3", ".mp4", ".oga", ".ogg", ".wav", ".webm"}
    content_type = file.content_type or ""
    if not content_type.startswith("audio/") and extension not in allowed_extensions:
        raise HTTPException(status_code=415, detail="Upload a supported audio file.")

    audio = await file.read(MAX_AUDIO_BYTES + 1)
    if not audio:
        raise HTTPException(status_code=400, detail="The audio file is empty.")
    if len(audio) > MAX_AUDIO_BYTES:
        raise HTTPException(status_code=413, detail="Audio files must be 20 MB or smaller.")

    mime_types = {
        ".aac": "audio/aac",
        ".flac": "audio/flac",
        ".m4a": "audio/mp4",
        ".mp3": "audio/mpeg",
        ".mp4": "audio/mp4",
        ".oga": "audio/ogg",
        ".ogg": "audio/ogg",
        ".wav": "audio/wav",
        ".webm": "audio/webm",
    }
    mime_type = content_type if content_type.startswith("audio/") else mime_types[extension]
    transcript = transcribe_audio(audio, mime_type)
    analysis = analyze_text(transcript)
    return VoiceAnalysisResponse(
        transcript=transcript,
        corrected_text=analysis.corrected_text,
        issues=analysis.issues,
    )


@router.post("/analyze-document", response_model=DocumentAnalysisResponse)
async def analyze_document(file: UploadFile = File(...)):
    filename = file.filename or "document.txt"
    extension = Path(filename).suffix.lower()
    if extension not in {".txt", ".md", ".pdf"}:
        raise HTTPException(status_code=415, detail="Upload a .txt, .md, or .pdf document.")

    content = await file.read(MAX_DOCUMENT_BYTES + 1)
    if len(content) > MAX_DOCUMENT_BYTES:
        raise HTTPException(status_code=413, detail="Documents must be 400 KB or smaller.")
    if not content:
        raise HTTPException(status_code=400, detail="The document is empty.")

    try:
        if extension == ".pdf":
            text = "\n".join(page.extract_text() or "" for page in PdfReader(BytesIO(content)).pages)
        else:
            text = content.decode("utf-8-sig")
    except Exception as exc:
        raise HTTPException(status_code=422, detail="The document could not be read as UTF-8 text or a valid PDF.") from exc

    text = text.strip()
    if not text:
        raise HTTPException(status_code=422, detail="No readable text was found in the document.")
    if len(text) > MAX_TEXT_LENGTH:
        raise HTTPException(status_code=413, detail="Documents must contain 10,000 characters or fewer.")

    analysis = analyze_text(text)
    return DocumentAnalysisResponse(
        filename=filename,
        original_text=text,
        corrected_text=analysis.corrected_text,
        issues=analysis.issues,
    )

@router.post("/CorrectText" , response_model=CorrectionResponse)
def correct(request: CorrectionRequest):
    return correct_text(request.text)

