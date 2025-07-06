
# ReviewLens — Review-to-Product Optimization Engine

**ReviewLens** is an end-to-end intelligent review analysis system that transforms unstructured app or product reviews into structured, actionable insights. It goes beyond sentiment analysis by automatically identifying user intent, extracting keyphrases, scoring urgency, and recommending team assignments. Designed for product managers, engineers, and QA teams.

---

## Table of Contents

* [Project Overview](#project-overview)
* [Directory Structure](#directory-structure)
* [Model Design](#model-design)
* [Data Pipeline](#data-pipeline)
* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)
* [Evaluation](#evaluation)
* [Dashboard Plan](#dashboard-plan)
* [Acknowledgments](#acknowledgments)

---

## Project Overview

ReviewLens takes app store or product reviews and:

* Classifies intent as bug report, feature request, or praise
* Extracts keyphrases from user feedback for clarity and grouping
* Scores urgency using sentiment polarity and subjectivity
* Stores results in PostgreSQL for long-term tracking
* Exposes functionality through a FastAPI backend
* Plans to offer a front-end dashboard via Streamlit

---

## Directory Structure

```
ReviewLens/
├── app/                        # Streamlit dashboard (planned)
│   └── dashboard.py
├── model/                      # Core ML and NLP modules
│   ├── classifier.py
│   ├── keybert_extractor.py
│   ├── utils.py
│   └── db.py
├── saved_model/                # Fine-tuned BERT model
│   └── reviewlens-bert-model/
├── data/                       # Review dataset and preprocessing
│   └── reviews.csv
├── main.py                     # FastAPI backend entrypoint
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## Model Design

### Review Classification (BERT)

* Model: Fine-tuned `bert-base-uncased`
* Classes: `bug`, `feature`, `praise`
* Output: Predicted label and confidence score

### Keyphrase Extraction

* Tool: [KeyBERT](https://github.com/MaartenGr/KeyBERT)
* Method: Embedding-based keyphrase ranking
* Output: Top-N extracted keyphrases

### Urgency Scoring

* Formula: `urgency = (1 - polarity) * subjectivity`
* Range: 0 (low urgency) to 1 (high urgency)

---

## Data Pipeline

* Clean and normalize user reviews
* Classify intent using the BERT-based classifier
* Extract keyphrases using KeyBERT
* Compute urgency score based on sentiment metrics
* Store structured results in a PostgreSQL database
* Access predictions through FastAPI endpoints

---

## Installation

```bash
git clone https://github.com/yourusername/ReviewLens.git
cd ReviewLens
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## Usage

### Run the FastAPI Backend

```bash
uvicorn main:app --reload
```

Then visit: `http://127.0.0.1:8000/docs` for the interactive API documentation.

### API Endpoints

* `POST /classify` – Returns intent label and confidence
* `POST /keyphrases` – Extracts keyphrases from text
* `POST /urgency` – Computes urgency score from polarity and subjectivity
* `POST /analyze` – Executes full pipeline and stores results in database

### Run the Streamlit Dashboard (Optional)

```bash
streamlit run app/dashboard.py
```

---

## Features

* Review classification using fine-tuned BERT
* Keyphrase extraction for summarization and tagging
* Urgency scoring to prioritize user issues
* Integration with PostgreSQL for persistent storage
* FastAPI backend for modular access
* Streamlit-based UI for real-time insights (in development)

---

## Evaluation

Performance on a labeled dataset (3-class classification):

| Class    | Precision | Recall | F1-Score | Support |
| -------- | --------- | ------ | -------- | ------- |
| Bug      | 0.99      | 0.98   | 0.99     | 1065    |
| Feature  | 0.99      | 0.98   | 0.99     | 695     |
| Praise   | 0.99      | 1.00   | 1.00     | 4179    |
| Accuracy |           |        | 0.99     | 5939    |

---

## Dashboard Plan

The upcoming dashboard will include:

* Issue frequency charts (bug vs feature vs praise)
* Urgency vs frequency bubble chart
* App-wise issue distribution
* Keyphrase clusters and filtering
* CSV export of auto-generated action items
* Team assignment indicators (Product / QA / Engineering)

---

## Acknowledgments

* HuggingFace Transformers
* KeyBERT for keyword extraction
* VADER Sentiment Analysis
* FastAPI
* PostgreSQL
* Streamlit

---

