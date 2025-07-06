Contract Clause Classification System
This project presents an end-to-end system for classifying legal contract clauses into well-defined categories. The pipeline leverages fine-tuned versions of LegalBERT for both single-label and multi-label classification. The system supports clause-level predictions from PDF/DOCX files, outputs interpretable results, and includes clause similarity detection.

Table of Contents
Project Overview
Directory Structure
Model Design
Training Data
Installation
Usage
Features
Evaluation
Acknowledgments
Project Overview
This repository contains two contract clause classifiers:

Single-label classifier: Each clause is assigned exactly one label.
Multi-label classifier: A clause may belong to multiple legal categories.
Both classifiers are accessible via Gradio applications. The system also includes:

Clause similarity comparison using sentence embeddings.
Prediction confidence explanation for each clause.
Batch processing and exportable CSV output.
Directory Structure
ContractClassifier/
├── app/                          # Gradio UI scripts
│   ├── multi_app.py
│   └── single_app.py
├── dataset/                      # Processed data
│   ├── clauses.csv
│   ├── clauses_multilabel_raw.csv
│   ├── clauses_top10_balanced.csv
│   └── CUADv1.json
├── models/                       # Trained model directories
│   ├── clause_classifier/
│   └── multi-clause-classifier/
├── notebook/                     # Training notebooks
│   ├── single_clause_training.ipynb
│   └── multi_clause_training.ipynb
├── outputs/                      # Model outputs
│   ├── single_outputs/
│   └── multi_outputs/
├── synthetic-contracts/         # Sample test documents
├── README.md
├── report.pdf                    # Final 2-page project report
└── requirements.txt             # Dependencies
Model Design
Backbone Model: nlpaueb/legal-bert-base-uncased

Single-Label Classifier
Type: Softmax
Architecture: BERT + linear classification head
Loss: CrossEntropyLoss
Output: Top-1 predicted label
Multi-Label Classifier
Type: Sigmoid
Architecture: BERT + linear classification head
Loss: BCEWithLogitsLoss
Output: Labels with score > 0.5 (threshold adjustable)
Similarity Module
Model: sentence-transformers/all-MiniLM-L6-v2
Technique: Cosine similarity across clause embeddings
Training Data
Base Dataset: CUAD (Contract Understanding Atticus Dataset)

Focus: Top 10 most frequent clause types

Format:

For single-label: one label per clause
For multi-label: multiple labels per clause (parsed from CUAD JSON)
Installation
git clone https://github.com/yourusername/ContractClassifier.git
cd ContractClassifier
pip install -r requirements.txt
Usage
Run the Single-Label Gradio App
python app/single_app.py
Run the Multi-Label Gradio App
python app/multi_app.py
Upload any .pdf or .docx contract.

The model classifies each clause.

Predictions are shown in a table with confidence scores.

Use buttons to:

Download output
View label-wise prediction probabilities (explainability)
Detect similar clauses
Features
Clause classification from contract files (PDF/DOCX)
Support for both single-label and multi-label scenarios
Clause similarity using embeddings
Confidence explanation for predictions
CSV export of results
Includes synthetic test contracts for validation
Evaluation
Single-Label Classifier (10 Classes)
Accuracy: 91%
Macro F1 Score: 0.91
Best performing classes: audit rights, cap on liability, governing law
Challenging class: exclusivity
Multi-Label Classifier (10 Classes)
Micro F1: 0.96
Macro F1: 0.96
Samples F1: 0.96
Good handling of overlapping labels and long-tail clauses
Acknowledgments
CUAD Dataset: The Atticus Project
LegalBERT: nlpaueb/legal-bert-base-uncased
Hugging Face Transformers and Datasets
Gradio for front-end deployment
Sentence Transformers for similarity analysis
