from flask import Flask, send_file, request
from sentiment_model import analyze_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    sentiment = None
    confidence = None

    if request.method == 'POST':
        user_text = request.form['user_text']
        sentiment, confidence = analyze_sentiment(user_text)
        confidence = round(confidence * 100, 2)

    return send_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
