from fastapi import FastAPI
from pydantic import BaseModel
from model.db import insert_review
from model.classifier import classify_review
from model.keybert_extractor import extract_keyphrases
from model.utils import compute_urgency

app = FastAPI()

# Define input schema
class ReviewInput(BaseModel):
    text: str
    app_name: str
    polarity: float
    subjectivity: float

@app.post("/analyze")
def analyze_review(review_input: ReviewInput):
    # 1. Classify
    label, confidence = classify_review(review_input.text)

    # 2. Keyphrases
    keyphrases = extract_keyphrases(review_input.text)

    # 3. Urgency
    urgency = compute_urgency(review_input.polarity, review_input.subjectivity)

    # 4. Prepare and save
    data = {
        "app_name": review_input.app_name,
        "review": review_input.text,
        "cleaned_review": review_input.text,  # if not already cleaned
        "label": label,
        "confidence": confidence,
        "urgency": urgency,
        "keyphrases": keyphrases
    }

    insert_review(data)
    return data
