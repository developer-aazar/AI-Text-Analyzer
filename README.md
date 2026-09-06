# AI Text Analyzer

An AI-powered text correction application built with **FastAPI**, **Gemini**, and **Streamlit**.

The application analyzes user-provided text and identifies **grammar, spelling, and punctuation mistakes**, while also providing a corrected version of the original text.

## ✨ Features

- AI-powered text correction
- Grammar mistake detection
- Spelling mistake detection
- Punctuation mistake detection
- Shows the original and corrected text
- Structured API responses using Pydantic
- FastAPI backend with Swagger/OpenAPI documentation
- Streamlit-based user interface
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
│   └── app_gui.py
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md

🔄 How It Works
User
  │
  ▼
Streamlit Frontend
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

🛠️ Tech Stack
Backend
Python
FastAPI
Pydantic
Uvicorn
AI
Google Gemini API
Google GenAI SDK
Frontend
Streamlit
Development
Git
GitHub
uv

📋 API
POST /correct

Analyzes and corrects the submitted text.

Request
{
  "text": "This are a example sentence."
}
Response
{
  "original_text": "This are a example sentence.",
  "corrected_text": "This is an example sentence.",
  "grammar_mistakes": [
    {
      "mistake": "are",
      "correction": "is"
    }
  ],
  "spelling_mistakes": [],
  "punctuation_mistakes": []
}

The API also provides interactive Swagger documentation at:

/docs

🚀 Running Locally
1. Clone the repository
git clone <https://github.com/developer-aazar/AI-Text-Analyzer>
cd "AI project"
2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables

Create a .env file in the project root:

AI_API_KEY=your_gemini_api_key

5. Start the FastAPI backend

From the project root:

cd backend
uvicorn api.main:app --reload

The backend will be available at:

http://localhost:8000

Swagger documentation:

http://localhost:8000/docs

6. Start the Streamlit frontend

Open another terminal, activate the virtual environment, and run:

streamlit run frontend/app_gui.py

🔐 Environment Variables

The application requires the following environment variable:

AI_API_KEY = Google Gemini API key

🎯 Project Goal

This project was built to explore practical AI integration with Python backend development.

Rather than simply returning a corrected sentence, the API produces structured information about the detected mistakes, making the AI output easier for a frontend or another application to consume.

🔮 Future Improvements

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
