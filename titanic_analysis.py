# titanic_analysis.py

import pandas as pd

# --- Load Titanic dataset ---
titanic = pd.read_csv("PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Pa.txt")

# --- Basic info ---
print("Shape:", titanic.shape)
print("Columns:", titanic.columns)
print("Data types:\n", titanic.dtypes)
print("\nFirst 5 rows:\n", titanic.head())

# --- Summary statistics ---
print("\nDataset Info:")
print(titanic.info())

print("\nSummary Stats:")
print(titanic.describe(include="all"))

# --- Column exploration ---
print("\nUnique Pclass values:", titanic["Pclass"].unique())
print("\nPclass counts:\n", titanic["Pclass"].value_counts())

print("\nEmbarked counts:\n", titanic["Embarked"].value_counts())

print("\nMedian Age:", titanic["Age"].median())

# --- Filtering examples ---
print("\nPassengers older than 50:\n", titanic[titanic["Age"] > 50].head())

# --- GroupBy example ---
print("\nAverage Age per Pclass:\n", titanic.groupby("Pclass")["Age"].mean())

# --- Missing values check ---
print("\nMissing values per column:\n", titanic.isnull().sum())

# --- Survival rate by class ---
print("\nSurvival rate by Pclass:\n", titanic.groupby("Pclass")["Survived"].mean())

# --- Survival rate by Sex ---
print("\nSurvival rate by Sex:\n", titanic.groupby("Sex")["Survived"].mean())
