# AI Text Analyzer

An AI-powered text correction application built with **FastAPI**, **Gemini**, and a browser-based frontend.

The application analyzes user-provided text and identifies **grammar, spelling, and punctuation mistakes**, while also providing a corrected version of the original text.

## ✨ Features

- AI-powered text correction
- Grammar mistake detection
- Spelling mistake detection
- Punctuation mistake detection
- Shows the original and corrected text
- Structured API responses using Pydantic
- FastAPI backend with Swagger/OpenAPI documentation
- Browser-based text, document, and audio interface
- Environment-based API key configuration

## 🏗️ Project Structure

```text
AI Text Analyzer/
│
├── backend/
│   └── api/
│       ├── core/
│       │   └── config.py
│       │
│       ├── routers/
│       │   └── correction_router.py
│       │
│       ├── schemas/
│       │   └── correction_schema.py
│       │
│       ├── services/
│       │   └── ai_service.py
│       │
│       └── main.py
│
├── frontend/
│   ├── index.html
│   └── README.md
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```

## How It Works

```text
User
  │
  ▼
Browser Frontend
  │
  ▼
FastAPI API
  │
  ▼
AI Service
  │
  ▼
Gemini API
  │
  ▼
Structured Analysis
  │
  ├── Corrected Text
  ├── Grammar Mistakes
  ├── Spelling Mistakes
  └── Punctuation Mistakes
```

## Tech Stack

- Backend: Python, FastAPI, Pydantic, Uvicorn
- AI: Google Gemini API, Google GenAI SDK
- Frontend: HTML, CSS, and JavaScript
- Development: Git, uv

## API

- `POST /analyze` accepts `{"text": "..."}` and returns `corrected_text` plus an `issues` array.
- `POST /analyze-document` accepts `.txt`, `.md`, or `.pdf` files.
- `POST /analyze-audio` accepts supported audio files.
- `POST /CorrectText` provides the legacy correction response.

Interactive API documentation is available at `/docs`.

## Running Locally
1. Create and activate a virtual environment, then install dependencies:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Configure the Gemini API key in a `.env` file in the project root:

```env
AI_API_KEY=your_gemini_api_key
```

3. Start the FastAPI backend from the project root:

```sh
uvicorn api.main:app --app-dir backend --reload
```

The backend and interactive API docs are available at `http://localhost:8000` and `http://localhost:8000/docs`.

4. In another terminal, serve the frontend from the project root:

```sh
python -m http.server 5500 --directory frontend
```

Open `http://localhost:5500`. The frontend defaults to `http://localhost:8000`; use its settings to change the backend address if needed.

## Environment Variables

The application reads `AI_API_KEY` from the root `.env` file. A missing key does not prevent the backend from starting, but AI endpoints return HTTP 503 until it is configured.

## Project Goal

This project was built to explore practical AI integration with Python backend development.

Rather than simply returning a corrected sentence, the API produces structured information about the detected mistakes, making the AI output easier for a frontend or another application to consume.

## Future Improvements

Possible future improvements include:

Voice message feature
User authentication
Text history
Multiple language support
Improved AI error handling
Rate limiting
Database integration
API deployment
Production monitoring
