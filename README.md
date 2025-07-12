# California-Housing-Analysis-App

Ce projet a été réalisé dans le cadre du cours 420-1AA-TT à l’Institut Teccart durant la session été 2025, sous la supervision du professeur Hichem Benfriha.

L’application développée avec Streamlit permet d’explorer visuellement les facteurs influençant les prix des logements en Californie à partir des données du recensement de 1990

## Objectif du projet

Développer une application interactive avec Streamlit ayant pour objectifs de :

Explorer les relations entre les caractéristiques des logements (superficie, ancienneté, localisation, etc.) et leur prix.

Identifier les facteurs ayant le plus d'influence sur la valeur des propriétés.

Fournir un outil d’aide à la décision pour les agences immobilières dans l’évaluation et la stratégie de vente.
## Structure du projet

- `data/housing.csv` : dataset d'origine
- `app.py` : interface Streamlit
- `analysis.py` : fonctions d'analyse
- `visualizations.py` : fonctions graphiques
- `requirements.txt` : dépendances(pandas-matplotlib-seaborn-streamlit)
- `README.md` : documentation

## Usage
Assurez-vous d'avoir installé les bibliothèques nécessaires : Puis lancez l'application : avec cette commande 
>>>streamlit run app.py

## Description des données

Le dataset provient de Kaggle : *California Housing Prices* (1990 census). Il comprend 10 colonnes :

1. longitude  
2. latitude  
3. housing_median_age  
4. total_rooms  
5. total_bedrooms  
6. population  
7. households  
8. median_income  
9. median_house_value  
10. ocean_proximity  

