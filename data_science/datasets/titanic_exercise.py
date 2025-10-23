"""
Titanic Dataset Exercise
------------------------
Practice loading, cleaning, and modeling the Titanic dataset.
"""
import pandas as pd

# 1. Load the dataset
titanic = pd.read_csv('titanic.csv')
print(titanic.head())

# 2. Data cleaning
print(titanic.isnull().sum())
# Fill missing ages with median
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())

# 3. Feature engineering
# Encode 'Sex'
titanic['Sex'] = titanic['Sex'].map({'male': 0, 'female': 1})

# 4. Train/test split and simple model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
X = titanic[['Pclass', 'Sex', 'Age', 'Fare']]
y = titanic['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
print('Accuracy:', model.score(X_test, y_test))
