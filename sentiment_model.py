from transformers import pipeline

# Use a specific model and revision
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    revision="714eb0f"
)

def analyze_sentiment(text):
    result = classifier(text)[0]
    return result['label'], result['score']
