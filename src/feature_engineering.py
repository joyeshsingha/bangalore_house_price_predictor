# src/feature_engineering.py

import pandas as pd


def reduce_locations(df, threshold=10):

    df["location"] = df["location"].apply(lambda x: x.strip())

    location_stats = df["location"].value_counts()

    locations_less_than_threshold = location_stats[
        location_stats <= threshold
    ].index

    df["location"] = df["location"].apply(
        lambda x: "other" if x in locations_less_than_threshold else x
    )

    return df


def remove_outliers(df):

    # sqft per bhk filter
    df = df[df["total_sqft"] / df["bhk"] >= 300]

    # price per sqft
    df["price_per_sqft"] = df["price"] * 100000 / df["total_sqft"]

    def remove_pps_outliers(data):
        df_out = pd.DataFrame()
        for key, subdf in data.groupby("location"):
            m = subdf.price_per_sqft.mean()
            st = subdf.price_per_sqft.std()
            reduced = subdf[(subdf.price_per_sqft > (m - st)) &
                            (subdf.price_per_sqft <= (m + st))]
            df_out = pd.concat([df_out, reduced], ignore_index=True)
        return df_out

    df = remove_pps_outliers(df)

    return df.drop(columns=["price_per_sqft"])


def encode_location(df):
    df = pd.get_dummies(df, columns=["location"], drop_first=True)
    return df


def prepare_features(df):

    df = reduce_locations(df)
    df = remove_outliers(df)
    df = encode_location(df)

    X = df.drop("price", axis=1)
    y = df["price"]

    return X, y