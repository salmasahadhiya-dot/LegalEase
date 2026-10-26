from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from ai_core.gemini_generator import generate_document

router = APIRouter()

class DocumentRequest(BaseModel):
    document_type: str = Field(min_length=2, max_length=100)
    parties: str = Field(min_length=2, max_length=2000)
    terms: str = Field(min_length=2, max_length=5000)
    effective_date: str = Field(min_length=4, max_length=50)

@router.post("/generate")
def generate(request: DocumentRequest):
    try:
        document = generate_document(request.document_type, request.parties, request.terms, request.effective_date)
        return {"document": document}
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=502, detail="AI generation failed. Check API key, model name, quota, and logs.") from exc
