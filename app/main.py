from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
from app.api.model_api import router
from app.ml.ml_model import model

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "template" / "index.html"

app = FastAPI(
    title="Real-Time Sentiment Analysis Pipeline",
    description="Streamlines live user text directly into the trained ML model."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with your specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router, prefix="/api")

@app.get("/")
def home():
    return FileResponse(TEMPLATE_PATH, media_type="text/html")

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": model is not None}

