
# 🧠 Sentiment Analyzer (NLP + Transformers + Flask)

A simple web application that performs sentiment analysis using Hugging Face Transformers. Built with Python, Flask, and an interactive front-end UI.

---

## 🚀 Features

- Real-time sentiment prediction (Positive / Negative / Neutral)
- Built using Hugging Face's `distilbert-base-uncased-finetuned-sst-2-english`
- Flask backend with HTML/CSS frontend (no Jinja templates required)
- Responsive and interactive UI (with animations and media queries)

---

## 🗂 Project Structure

```
Sentiment_Analyzer/
│
├── app.py                # Flask web app
├── index.html            # Frontend HTML (standalone)
├── style.css             # Custom responsive styling
├── sentiment_model.py    # Hugging Face sentiment analysis logic
└── README.md             # Documentation
```

> ✅  `templates/` or `static/` folders needed.

---

## 🔧 Requirements

Install these dependencies before running the app:

```bash
pip install flask transformers torch
```

### 📦 Python Libraries Used
- `Flask` — for the web server
- `transformers` — for loading the BERT model
- `torch` — backend for model inference

---

## 🧠 Model Info

We use:

```python
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
```

By default, this loads:

- `distilbert-base-uncased-finetuned-sst-2-english`

This model will **download automatically from Hugging Face** when first used.

📡 **Internet Connection is required** on first run.

---

## 💻 Running the App

Run your app locally:

```bash
python app.py
```

Then visit:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 Deployment Notes

If deploying online (e.g. Heroku, Render, etc):

1. Add a `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```

2. Optionally add:
   - `Procfile`
   - `runtime.txt` (e.g., `python-3.10.11`)

3. Make sure the first model load doesn't timeout (can cache locally if needed).

