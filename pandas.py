#pandas

print("Hello ,PRANAM")

import pandas as pd

mylist=["a","b","c","d","e","1"]
myseries=pd.Series(mylist)

print(myseries)
print(type(myseries))



#DataFrAME FRON Dict
dict={
    "name": ["john", "kennedy", "dube"],
    "age": [12, 14, 16],
    "city": ["Houston", "texas", "new york"]
}

df=pd.DataFrame(dict)
print(df)
print(type(df))

#load CSV
cancer=pd.read_csv("Cancer.csv")
print(cancer.head())
print(type(cancer))


heart = pd.read_csv("heart.csv")
print(heart.head())
print(type(heart))

# --- Explore Heart Dataset ---
print(heart.head(16))
print(heart.tail())
print(heart.tail(14))
print(heart.info())
print(heart.describe())
print(heart.columns)
print(cancer.columns)
print(heart.shape)
print(heart.dtypes)
print(heart.index)

# --- Column Selection ---
x = heart["chol"]
print(x)
y = heart[["age", "chol", "target"]]
print(y.head())

print(heart["oldpeak"].unique())

# --- Titanic Dataset ---
titanic = pd.read_csv("train.csv")
print(titanic.head())
print(titanic["Pclass"].unique())
print(titanic["Pclass"].value_counts())
print(titanic["Embarked"].value_counts())
print(titanic["Age"].median())

# --- Slicing Example ---
print(x[0:10:3])
print(titanic.loc[3:7])