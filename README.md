#  AI Medical Symptom Assistant

An AI-powered web application that predicts possible diseases based on user-selected symptoms and provides detailed disease information along with AI-generated explanations and follow-up medical guidance.

> **Disclaimer:** This application is developed for educational purposes only and is **not a substitute for professional medical advice, diagnosis, or treatment.**

---

#  Demo

**Frontend:** https://ai-medical-symptom-assistant.vercel.app/

**Backend API:** https://ai-medical-symptom-assistant.onrender.com

---

#  Features

- Predicts diseases from user-selected symptoms using a Deep Learning model
- Displays Top-3 disease predictions with confidence scores
- Interactive confidence progress bars
- Detailed disease information including:
  - Description
  - Possible Causes
  - Precautions
  - Recommended Specialist
- AI-powered follow-up medical assistant using Groq LLM
- Symptom autocomplete search
- Responsive React frontend
- FastAPI REST API backend
- Swagger API documentation
- TensorFlow SavedModel deployment
- Fully deployed on Render & Vercel

---

#  Tech Stack

## Frontend

- React
- Vite
- Axios
- React Icons
- CSS3

## Backend

- FastAPI
- TensorFlow
- NumPy
- Scikit-learn
- Pandas
- Groq API

## Machine Learning

- TensorFlow / Keras Deep Neural Network
- Random Forest (Experimented)
- Logistic Regression (Experimented)
- XGBoost (Experimented)

---

#  Machine Learning Pipeline

1. Collect symptom dataset
2. Data preprocessing
3. Label Encoding
4. Feature Vector Generation
5. Model Training
6. Deep Learning Classification
7. Save TensorFlow Model
8. FastAPI Integration
9. Disease Prediction
10. AI Explanation Generation

---

#  Project Structure

```
AI-medical-symptom-assistant
│
├── backend
│   ├── main.py
│   ├── config.py
│   ├── requirements.txt
│   ├── models
│   │   ├── dnn_saved_model
│   │   ├── label_encoder.pkl
│   │   └── symptom_columns.pkl
│   ├── services
│   ├── utils
│   └── schemas
│
├── medical-ai-frontend
│   ├── src
│   ├── public
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

#  Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-medical-symptom-assistant.git
cd AI-medical-symptom-assistant
```

---

## Backend

```bash
cd backend

python -m venv venv

source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```
```

Run

```bash
uvicorn main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

---

## Frontend

```bash
cd medical-ai-frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /health | Health Check |
| GET | /symptoms | Get Symptoms |
| GET | /diseases | List Diseases |
| GET | /diseases/{disease_name} | Disease Information |
| POST | /predict | Disease Prediction |
| POST | /ask-ai | AI Medical Chat |

---

#  Model Performance

The project was trained and evaluated using multiple Machine Learning algorithms.

Algorithms experimented:

- Logistic Regression
- Random Forest
- XGBoost
- Deep Neural Network (Final Model)

The Deep Neural Network achieved the best overall performance and was selected as the production model.


# 🌐 Deployment

Frontend

- Vercel

Backend

- Render


---

#  Author

**Rituraj Singh Rathore**

GitHub:
https://github.com/rituraj2028

LinkedIn:
https://www.linkedin.com/in/rituraj-singh-rathore-97b77336b

---

