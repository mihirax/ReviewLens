import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="ReviewLens", page_icon="🔍")
st.title("📱 ReviewLens - Real-time Review Classifier")

# Input fields
review = st.text_area("✏️ Paste your review:")
app_name = st.text_input("🏷️ App Name")

if st.button("🔎 Analyze"):
    payload = {
        "text": review,
        "app_name": app_name,
        "review": review,
        "polarity": 0.5,       # Placeholder; you can compute this too
        "subjectivity": 0.5    # Placeholder
    }

    response = requests.post("http://127.0.0.1:8000/analyze", json=payload)

    if response.ok:
        result = response.json()

        # Label display with emoji
        label_emojis = {
            "bug": "🐞 Bug",
            "feature": "✨ Feature Request",
            "praise": "🎉 Praise"
        }
        label = label_emojis.get(result['label'].lower(), result['label'])

        st.success(f"**Predicted Label:** {label}")

        # Confidence bar
        st.write("**Model Confidence:**")
        st.progress(result['confidence'])

        # Urgency bar
        st.write("**Urgency Score:**")
        st.progress(result['urgency'])

        # Keyphrases
        st.write("**🔑 Keyphrases Extracted:**")
        st.code(", ".join(result['keyphrases']))

        # Optionally save results locally
        log_data = {
            "App": app_name,
            "Review": review,
            "Label": result['label'],
            "Confidence": result['confidence'],
            "Urgency": result['urgency'],
            "Keyphrases": ", ".join(result['keyphrases'])
        }

        df = pd.DataFrame([log_data])
        try:
            df.to_csv("reviewlens_log.csv", mode="a", header=not pd.read_csv("reviewlens_log.csv").empty, index=False)
        except FileNotFoundError:
            df.to_csv("reviewlens_log.csv", index=False)

    else:
        st.error("❌ API request failed. Is FastAPI running?")
