import pandas as pd

def descriptive_statistics(df):
    return df.describe()

def influential_features(df):
    numeric_df = df.select_dtypes(include=["float64", "int64"])

    correlations = numeric_df.corr()["median_house_value"].sort_values(ascending=False)
    return correlations.drop("median_house_value")

