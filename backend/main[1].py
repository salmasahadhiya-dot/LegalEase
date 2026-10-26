from fastapi import FastAPI
from backend.routes import router

app = FastAPI(title="LegalEase API", description="API for generating first-draft legal documents with AI.", version="1.0.0")
app.include_router(router)

@app.get("/")
def home():
    return {"message": "LegalEase API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
