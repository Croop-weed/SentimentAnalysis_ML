import joblib
import re
import string
from pathlib import Path
from app.schemas.model import InputText, Response
from fastapi import HTTPException

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "Random Forest"
VECTORIZER_PATH = BASE_DIR / "tfidf_vectorizer.pkl"

model = joblib.load(MODEL_PATH)
tfidf = joblib.load(VECTORIZER_PATH)


def text_cleaning(data: InputText):
    raw_input = data.text

    try:
        cleaned_text = raw_input.lower().strip()
        cleaned_text = re.sub(r'https?://\S+|www\.\S+', '', cleaned_text)
        cleaned_text = cleaned_text.translate(
            str.maketrans('', '', string.punctuation))

        vectorized_text = tfidf.transform([cleaned_text])

        prediction = int(model.predict(vectorized_text)[0])
        prediction_label = {0: "NEGATIVE", 1: "NEUTRAL", 2: "POSITIVE"}.get(prediction, "NEUTRAL")

        probabilities = model.predict_proba(vectorized_text)[0]
        confidence_dict = {f"Class_{i}": round(
            float(prob), 4) for i, prob in enumerate(probabilities)}

        return Response(
            raw_text=raw_input,
            cleaned_text=cleaned_text,
            result=prediction_label,
            confidence_scores=confidence_dict
        )

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Pipeline processing failed: {str(e)}")
