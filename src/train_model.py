# src/train_model.py
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from data_cleaning import clean_data
from feature_engineering import prepare_features


DATA_PATH = "data/Bengaluru_House_Data.csv"


def train():

    # cleaning
    df = clean_data(DATA_PATH)

    # feature engineering
    X, y = prepare_features(df)

    # split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # model
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=None,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"Model R2 Score: {score:.3f}")


    # save model
    joblib.dump(model, "models/house_price_model.pkl")
    joblib.dump(X.columns, "models/model_columns.pkl")


if __name__ == "__main__":
    train()