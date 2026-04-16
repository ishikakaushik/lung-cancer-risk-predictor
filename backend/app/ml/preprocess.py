import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

def load_and_clean_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "../../../data/raw/survey lung cancer.csv")
    
    df = pd.read_csv(data_path)
    df.columns = df.columns.str.strip().str.upper().str.replace(" ", "_")
    
    df["GENDER"] = df["GENDER"].map({"M": 1, "F": 0})
    df["LUNG_CANCER"] = df["LUNG_CANCER"].map({"YES": 1, "NO": 0})
    
    df = df.dropna()
    
    return df

if __name__ == "__main__":
    df = load_and_clean_data()
    print(df.head())
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())