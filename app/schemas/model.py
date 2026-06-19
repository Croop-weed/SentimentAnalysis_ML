from pydantic import BaseModel

class InputText(BaseModel):
    text: str

class Response(BaseModel):
    raw_text: str
    result: str
    cleaned_text: str
    confidence_scores: dict
