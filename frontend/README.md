# AI Text Analyzer: front-end

A clean, responsive web page for your AI Text Analyzer. You write or speak text, press **Analyze**, and see spelling, grammar and punctuation problems marked in color, with fixes in a sidebar.

Built by Abdul Latif Jatoi (Aazar). The frontend is served as a static page and needs no build step.

## What it can do

- Three kinds of problems in three colors: **spelling** (red), **grammar** (blue), **punctuation** (orange)
- Click a card to find the problem in the text, or click a mark to find its card
- **Apply** one fix, **Ignore** one, or **Apply all fixes**, with **Undo**
- Filters, a writing score, and word and character counts
- **Review** tab (marked text) and **Corrected** tab (fixed text with changes shown in green)
- Copy or download the corrected text
- **Voice**: record your voice, see a live waveform and live transcript, then analyze the text
- **Voice insights**: speaking speed (words per minute) and filler words ("um", "you know", ...)
- Analyze an **audio file** (needs your backend)
- Open a `.txt` file or drag it onto the editor
- Light and dark theme, works on phones
- **Demo mode**: a small checker built into the page, so it works even with no backend

## Run it

From the repository root, serve the frontend directory:

```
python -m http.server 5500 --directory frontend
```

Open http://localhost:5500 in Chrome or Edge.

## Connect your FastAPI backend

1. Start the backend from the repository root: `uvicorn api.main:app --app-dir backend --reload`.
2. In the page settings, use `http://localhost:8000` as the backend address, then save.

The top-right badge changes from "Demo mode" to "Backend · 127.0.0.1:8000".

### What the page expects

```
POST /analyze          {"text": "..."}
POST /analyze-audio    multipart form with a "file" field
```

Response:

```json
{
  "corrected_text": "The fixed text",
  "transcript": "Only for audio",
  "issues": [
    {
      "type": "spelling",
      "original": "recieve",
      "suggestion": "receive",
      "explanation": "Common misspelling.",
      "start": 2,
      "end": 9
    }
  ]
}
```

- `type` is `spelling`, `grammar` or `punctuation`.
- `start` and `end` are optional. If they are missing, the page finds `original` in the text itself.
- The backend response uses `corrected_text`, `issues`, and optional `transcript` fields.

The backend reads `AI_API_KEY` from the repository-root `.env` file. Keep that key on the server.

## Files

| File | What it does |
|---|---|
| `index.html` | The complete bundled frontend application |

## Voice notes

- **Live transcript** uses your browser's speech recognition. It works in Chrome, Edge and Safari, not in Firefox. Chrome sends the audio to Google's servers for this.
- **Backend transcription** (tick the box in the Voice panel) sends the recording to `/analyze-audio`, so Gemini can transcribe it. This works in every browser that can record.
- The browser asks for microphone permission. It only works on `localhost` or `https`.

## Before you put it online

- Serve it over HTTPS and set your backend's CORS to your real site address only.
- Never put your Gemini API key in the front-end. Keep it on the server.
- Add rate limits and a size limit on `/analyze` and `/analyze-audio`.
- Tell users that audio and text are sent to an AI service.

## Ideas to extend it

- Save history per user (needs login and a database)
- Tone and style suggestions (formal, friendly, short)
- Rewrite a sentence in a different tone
- Export a PDF report
- Show a diff between the original and corrected text
