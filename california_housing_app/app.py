import streamlit as st
import pandas as pd
from analysis import descriptive_statistics, influential_features
from visualizations import plot_histograms, plot_boxplots, plot_correlation_heatmap

st.title(" Analyse du marché immobilier en Californie")

@st.cache_data
def load_data():
    return pd.read_csv("data/housing.csv")

data = load_data()

st.subheader("Aperçu du jeu de données")
st.write(data.head())

st.subheader(" Statistiques descriptives")
st.write(descriptive_statistics(data))

st.subheader(" Visualisations")
plot_histograms(data)
plot_boxplots(data)
plot_correlation_heatmap(data)

st.subheader(" Caractéristiques influentes sur le prix")
st.write(influential_features(data))
