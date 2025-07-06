def compute_urgency(polarity, subjectivity):
    if polarity is None or subjectivity is None:
        return None
    polarity_score = 1 - ((polarity + 1) / 2)
    urgency = 0.7 * polarity_score + 0.3 * subjectivity
    return round(urgency, 3)
import re

def clean_review(text):
    text = re.sub(r"http\S+|www\S+|@\w+|[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.lower().strip()
