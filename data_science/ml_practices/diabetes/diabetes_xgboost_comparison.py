"""
diabetes_xgboost_comparison.py
------------------------------
Compares XGBoost with other regressors on the Diabetes dataset.
"""

import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor

from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor

X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = [
    ("XGBoost", XGBRegressor(n_estimators=100, random_state=42, verbosity=0)),
    ("GradientBoosting", GradientBoostingRegressor(n_estimators=100, random_state=42)),
    ("RandomForest", RandomForestRegressor(n_estimators=100, random_state=42))
]

for name, model in models:
    model.fit(X_train_scaled, y_train)
    preds = model.predict(X_test_scaled)
    print("{} MSE: {:.2f}, R2: {:.3f}".format(name, mean_squared_error(y_test, preds), r2_score(y_test, preds)))