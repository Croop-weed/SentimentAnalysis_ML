from fastapi import APIRouter
from app.schemas.model import InputText, Response
from app.ml.ml_model import text_cleaning

router = APIRouter(prefix="/predict")

@router.post("/result", response_model=Response)
def res(data: InputText):
    return text_cleaning(data)
