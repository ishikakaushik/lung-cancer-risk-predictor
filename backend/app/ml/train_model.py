import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from preprocess import load_and_clean_data


def train():
    df = load_and_clean_data()

    # separate features and target
    X = df.drop("LUNG_CANCER", axis=1)
    y = df["LUNG_CANCER"]

    # split into train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # create model
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # train model
    model.fit(X_train, y_train)

    # predictions
    y_pred = model.predict(X_test)

    # evaluate
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")


if __name__ == "__main__":
    train()