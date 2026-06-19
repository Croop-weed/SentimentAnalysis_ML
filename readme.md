# 📊 Sentiment Pulse Detector

An aesthetic, high-performance, real-time Sentiment Analysis web application. This project features a machine learning pipeline powered by a **Random Forest Classifier** trained on text data vectorized via **TF-IDF (Term Frequency-Inverse Document Frequency)**. The entire system is packaged as a unified **FastAPI** service that serves both a modern Tailwind CSS glassmorphic frontend and a high-speed prediction engine from a single port.

---

## 🚀 Key Features
- **Machine Learning Powered:** Utilizes a Random Forest Classifier for reliable multiclass sentiment predictions.
- **Unified Microservice Architecture:** Both the frontend user interface and backend inference logic run concurrently from the same FastAPI instance (no CORS configuration required).
- **In-Memory Transformation:** Loads the baseline TF-IDF vocabulary matrix and trained model weights into RAM exactly once at system startup for sub-millisecond response times.
- **Real-Time Data Preparation:** Automatically applies case normalization, URL extraction, and punctuation stripping to live user inputs before running vector transforms.
- **Aesthetic UI:** Designed with a sleek, responsive dark-mode glassmorphism interface using Tailwind CSS and native JavaScript (Fetch API).

---

## 📸 Application Preview
*To render your application images here, create an `images` folder in your project root, save your screenshots as `app_screenshot.png` and `confidence_chart.png`, and push them to your repository.*

![Main Interface](images/app_screenshot.png)
*Figure 1: The Glassmorphic Sentiment Pulse Input Web Interface.*

![Analysis Result](images/confidence_chart.png)
*Figure 2: Real-time analysis output exhibiting dynamic class styling.*

---

## 🛠️ Tech Stack
- **Data Vectorization:** `Scikit-Learn` (TfidfVectorizer)
- **Core Model:** `Scikit-Learn` (RandomForestClassifier)
- **Backend Server Framework:** `FastAPI`
- **ASGI Server Engine:** `Uvicorn`
- **Frontend Layer:** HTML5, CSS3, Tailwind CSS, Vanilla JavaScript
- **Serialization & Storage:** `Joblib`

---

## 📊 Pipeline Data Flow
The system strictly isolates runtime data transformation from your historical training datasets to prevent production data drift failures, following this assembly line:

###[ Raw User Input String ]
│
▼
┌──────────────────────────┐
│  ###Real-Time Cleaning Loop │ ──> Strips URLs, normalizes casing & punctuation
└──────────────────────────┘
│
▼
┌──────────────────────────┐
│   ###tfidf_vectorizer.pkl   │ ──> Transforms text via trained baseline vocabulary
└──────────────────────────┘
│
▼
┌──────────────────────────┐
│ ###best_sentiment_model.pkl │ ──> Random Forest calculates decision paths
└──────────────────────────┘
│
▼
###[ Class Map Dictionary ]  ──> { 0: "NEGATIVE", 1: "NEUTRAL", 2: "POSITIVE" }

---

## ⚙️ Installation & Local Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/sentiment-pulse-detector.git](https://github.com/yourusername/sentiment-pulse-detector.git)
cd sentiment-pulse-detector

