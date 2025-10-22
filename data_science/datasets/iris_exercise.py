"""
Iris Dataset Exercise
---------------------
Practice loading, exploring, and modeling the iris dataset.
"""
import pandas as pd

# 1. Load the dataset
iris = pd.read_csv('iris.csv')
print(iris.head())

# 2. Basic EDA
print(iris.describe())
print(iris['species'].value_counts())

# 3. Visualization (optional)
# import matplotlib.pyplot as plt
# iris.plot(kind='scatter', x='sepal_length', y='sepal_width', c=iris['species'].astype('category').cat.codes)
# plt.show()

# 4. Train/test split and simple model
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
X = iris.drop('species', axis=1)
y = iris['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
print('Accuracy:', model.score(X_test, y_test))
