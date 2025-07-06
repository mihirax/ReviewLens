import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

# Load model and tokenizer (only once)
model_name = "saved_model/reviewlens-bert-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

# Get label mapping from config
label_map = {
    0: "bug",
    1: "feature",
    2: "praise"
}

def classify_review(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = F.softmax(logits, dim=1)
        top_prob, top_idx = torch.max(probs, dim=1)
        label = label_map[top_idx.item()]
        confidence = top_prob.item()
    return label, confidence
