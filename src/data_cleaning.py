# src/data_cleaning.py

import pandas as pd
import numpy as np


def load_data(path):
    return pd.read_csv(path)


def drop_unnecessary_columns(df):
    cols = ["area_type", "availability", "society", "balcony"]
    return df.drop(columns=cols, errors="ignore")


def clean_size(df):
    df["bhk"] = df["size"].str.split().str[0].astype(float)
    return df.drop(columns=["size"])


def convert_sqft(x):
    try:
        if "-" in str(x):
            a, b = x.split("-")
            return (float(a) + float(b)) / 2
        return float(x)
    except:
        return np.nan


def clean_total_sqft(df):
    df["total_sqft"] = df["total_sqft"].apply(convert_sqft)
    return df


def remove_nulls(df):
    return df.dropna()


def clean_data(path):
    df = load_data(path)
    df = drop_unnecessary_columns(df)
    df = clean_size(df)
    df = clean_total_sqft(df)
    df = remove_nulls(df)
    return df