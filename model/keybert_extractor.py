from keybert import KeyBERT

kw_model = KeyBERT(model='all-MiniLM-L6-v2')

def extract_keyphrases(text, top_n=5):
    phrases = kw_model.extract_keywords(text, stop_words='english', top_n=top_n)
    return [kw for kw, _ in phrases]
