import os
from google import genai

def generate_document(document_type: str, parties: str, terms: str, effective_date: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing. Set it in .env or Render environment variables.")
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    client = genai.Client(api_key=api_key)
    prompt = f"""
Create a structured first draft for this legal document. This is general drafting assistance, not legal advice.
Do not claim guaranteed enforceability. Do not invent missing facts; mark them [TO BE COMPLETED].
Use clear headings, numbered clauses, and signature sections where appropriate. If jurisdiction is not provided, say local legal review is required.
Document type: {document_type}
Parties: {parties}
Terms and conditions: {terms}
Effective date: {effective_date}
Finish with: Draft only — review by a qualified lawyer before signing.
"""
    response = client.models.generate_content(model=model_name, contents=prompt)
    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("The AI model returned an empty response. Please retry.")
    return text.strip()
