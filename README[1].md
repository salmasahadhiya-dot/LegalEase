# LegalEase — AI-Powered Legal Document Generator

Includes a Streamlit frontend, FastAPI backend, Gemini AI integration, editable preview, and TXT/DOCX/PDF downloads.

## Files
- `app.py`: Streamlit frontend
- `backend/main.py`: FastAPI app and health checks
- `backend/routes.py`: request validation and `/generate`
- `ai_core/gemini_generator.py`: Gemini integration
- `requirements.txt`: dependencies
- `.env.example`: environment template
- `render.yaml`: Render two-service blueprint example

## Run locally on Windows
1. Install Python 3.12.
2. Extract the ZIP and open this folder in VS Code.
3. Terminal: `py -3.12 -m venv .venv`
4. Activate: `.venv\\Scripts\\Activate.ps1` (or Command Prompt: `.venv\\Scripts\\activate.bat`)
5. Install: `pip install -r requirements.txt`
6. Copy `.env.example` to `.env`; add your Gemini API key. Never upload `.env`.
7. Terminal 1: `uvicorn backend.main:app --reload --port 8000`
8. Terminal 2: activate `.venv`, then `streamlit run app.py`
9. Open the Streamlit URL shown. API docs: `http://127.0.0.1:8000/docs`.

## Upload to GitHub
1. Create a repository named `LegalEase`.
2. Choose Add file → Upload files.
3. Upload the contents of this project folder, not only the ZIP.
4. Commit changes. Ensure `.env` is not in GitHub.

## Deploy on Render
Create two Web Services from the same repository.

### Backend
Build: `pip install -r requirements.txt`
Start: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
Environment variables: `GEMINI_API_KEY` = your key; `GEMINI_MODEL` = `gemini-2.5-flash` (use a model available to your key if needed).

### Frontend
Build: `pip install -r requirements.txt`
Start: `streamlit run app.py --server.address 0.0.0.0 --server.port $PORT`
Environment variable: `BACKEND_URL` = the backend's full public URL, without `/docs`.

Check Render Logs for failures. Never share your API key. AI-generated legal drafts must be reviewed by a qualified lawyer.
