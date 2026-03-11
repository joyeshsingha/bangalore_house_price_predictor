# src/predict.py

from pathlib import Path
import joblib
import pandas as pd

# =========================
# Load Model + Columns
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "house_price_model.pkl")
columns = joblib.load(BASE_DIR / "models" / "model_columns.pkl")


# =========================
# Prediction Function
# =========================

def predict_price(location, sqft, bath, bhk):

    # create empty dataframe with training columns
    input_df = pd.DataFrame(columns=columns)
    input_df.loc[0] = 0

    # numeric inputs
    input_df.at[0, "total_sqft"] = sqft
    input_df.at[0, "bath"] = bath
    input_df.at[0, "bhk"] = bhk

    # one-hot location
    loc_col = f"location_{location}"
    if loc_col in input_df.columns:
        input_df.at[0, loc_col] = 1

    prediction = model.predict(input_df)[0]

    return round(prediction, 2)


# =========================
# Locations for Dropdown
# =========================

def get_locations():
    locations = [
        col.replace("location_", "")
        for col in columns
        if col.startswith("location_")
    ]

    return sorted(locations)