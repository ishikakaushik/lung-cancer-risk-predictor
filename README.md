# Lung Cancer Risk Predictor

A full-stack machine learning web application that predicts lung cancer risk based on patient symptoms and lifestyle factors.

## 🔍 Features
- Predicts lung cancer risk using a Random Forest model
- Provides probability score
- Gives human-readable explanations for predictions
- Full-stack implementation (FastAPI + React)

## 🛠 Tech Stack
- Backend: FastAPI, Python, Scikit-learn
- Frontend: React (Vite)
- Data: CSV-based dataset

## ⚙️ How to Run

### Backend
cd backend  
uvicorn app.main:app --reload  

Runs on: http://127.0.0.1:8000  

### Frontend
cd frontend  
npm install  
npm run dev  

Runs on: http://localhost:5173  

## 📊 Example Output
- Label: High Risk  
- Probability: 0.87  
- Explanation:  
  - Smoking increases lung cancer risk  
  - Shortness of breath is a strong symptom  

## 📌 Future Improvements
- Add user input form  
- Deploy online  
- Improve UI/UX  
- Add model evaluation metrics  
