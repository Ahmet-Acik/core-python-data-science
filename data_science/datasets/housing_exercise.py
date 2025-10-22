"""
Housing Dataset Exercise
------------------------
Practice regression and feature engineering with housing data.
"""
import pandas as pd

# 1. Load the dataset
housing = pd.read_csv('housing.csv')
print(housing.head())

# 2. Basic EDA
print(housing.describe())

# 3. Feature engineering
housing['income_per_lat'] = housing['median_income'] / housing['latitude']

# 4. Train/test split and regression model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X = housing[['longitude', 'latitude', 'median_income', 'income_per_lat']]
y = housing['median_house_value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
print('R^2:', model.score(X_test, y_test))
