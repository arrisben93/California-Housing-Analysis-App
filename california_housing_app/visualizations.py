import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def plot_histograms(df):
    st.write("Distribution des variables")
    for col in ["median_income", "housing_median_age", "total_rooms", "median_house_value"]:
        fig, ax = plt.subplots()
        sns.histplot(df[col], bins=30, kde=True, ax=ax)
        st.pyplot(fig)

def plot_boxplots(df):
    st.write("Boxplots")
    for col in ["median_income", "total_rooms"]:
        fig, ax = plt.subplots()
        sns.boxplot(x=df[col], ax=ax)
        st.pyplot(fig)

def plot_correlation_heatmap(df):
    st.write("Heatmap des corrélations")

    numeric_df = df.select_dtypes(include=["float64", "int64"])

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig)

