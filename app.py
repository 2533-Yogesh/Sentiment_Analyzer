from flask import Flask, request, send_file, render_template_string
from transformers import pipeline

app = Flask(__name__)
classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = classifier(text)[0]
    return result['label'], round(result['score'] * 100, 2)

with open("index.html") as f:
    html_template = f.read()

@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    confidence = None
    if request.method == "POST":
        text = request.form["user_text"]
        sentiment, confidence = analyze_sentiment(text)
    return render_template_string(html_template, sentiment=sentiment, confidence=confidence)

@app.route("/download-readme")
def download_readme():
    return send_file("README.md", as_attachment=True)

@app.route("/style.css")
def serve_css():
    return send_file("style.css", mimetype='text/css')

if __name__ == "__main__":
    app.run(debug=True)
