import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from app.ml.preprocess import load_and_clean_data


# load and prepare training data
df = load_and_clean_data()
X = df.drop("LUNG_CANCER", axis=1)
y = df["LUNG_CANCER"]

# train model once when this file loads
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)


def predict(input_data: dict):
    df_input = pd.DataFrame([input_data])

    prediction = int(model.predict(df_input)[0])
    probability = float(model.predict_proba(df_input)[0][1])

    label = "High Risk" if prediction == 1 else "Low Risk"

    explanation = []

    if input_data.get("SMOKING", 0) == 1:
        explanation.append("Smoking increases lung cancer risk")

    if input_data.get("SHORTNESS_OF_BREATH", 0) == 2:
        explanation.append("Shortness of breath is a strong symptom")

    if input_data.get("CHEST_PAIN", 0) == 2:
        explanation.append("Chest pain is associated with lung issues")

    return {
        "prediction": prediction,
        "label": label,
        "probability": round(probability, 3),
        "explanation": explanation
    }