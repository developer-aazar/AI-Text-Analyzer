AI Text Analyzer 🤖📝

An AI-powered text analysis and correction application built with FastAPI, Google Gemini, and Streamlit.

The application analyzes user-provided text, identifies grammar, spelling, and punctuation mistakes, and returns both a fully corrected version and structured mistake details.

✨ Features
🤖 AI-powered text analysis and correction
📖 Grammar mistake detection
🔤 Spelling mistake detection
✍️ Punctuation mistake detection
🔄 Displays both the original and corrected text
📦 Structured API responses using Pydantic
⚡ FastAPI backend
📚 Interactive Swagger/OpenAPI documentation
🖥️ Streamlit-based user interface
🔐 Environment-based API key configuration
🧩 Separation of concerns using routers, schemas, services, and core configuration
🏗️ Project Structure

AI-Text-Analyzer/
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
Google Gemini API
 │
 ▼
Structured Analysis
 │
 ├── Corrected Text
 ├── Grammar Mistakes
 ├── Spelling Mistakes
 └── Punctuation Mistakes

The AI response is processed into a structured format before being returned by the API, making it easier for the frontend or other applications to consume.

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
Development Tools
Git
GitHub
uv

📋 API
POST /correct

Analyzes the submitted text, identifies mistakes, and returns a corrected version.

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

Each mistake category returns a list containing zero or more detected mistakes.

If no mistakes are found in a category, the API returns an empty list:

[]

📚 API Documentation

FastAPI automatically provides interactive API documentation.

After starting the backend, open:

http://localhost:8000/docs

From Swagger UI, you can test the /correct endpoint directly.

🚀 Running Locally
1. Clone the Repository
git clone https://github.com/developer-aazar/AI-Text-Analyzer.git
cd AI-Text-Analyzer

2. Create and Activate a Virtual Environment
python -m venv .venv
Linux
source .venv/bin/activate
Windows
.venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the project root:

AI_API_KEY=your_gemini_api_key_here


5. Start the FastAPI Backend

From the project root:

cd backend

Then run:

uvicorn api.main:app --reload

The backend will be available at:

http://localhost:8000

Swagger documentation:

http://localhost:8000/docs

6. Start the Streamlit Frontend

Open another terminal, activate the virtual environment, and from the project root run:

streamlit run frontend/app_gui.py

🔐 Environment Variables
Variable	Description
AI_API_KEY	Google Gemini API key used for AI text analysis

🎯 Project Goal

This project was built to explore practical AI integration with Python backend development.

Rather than simply sending text to an AI model and displaying its response, the application focuses on returning structured AI output through a backend API.

The project demonstrates concepts such as:

API architecture
Request validation
Response validation
Pydantic schemas
Service-layer separation
AI API integration
Structured JSON responses
Backend and frontend integration
Environment variable management
🔮 Future Improvements
🎤 Voice input and response
👤 User authentication
📜 Text analysis history
🌍 Multiple language support
⚠️ Improved AI and API error handling
🚦 Rate limiting
🗄️ Database integration
☁️ Production API deployment
📊 Production monitoring

👨‍💻 Author

Abdul Latif (Aazar)

Backend Developer | Python | FastAPI | AI Integration