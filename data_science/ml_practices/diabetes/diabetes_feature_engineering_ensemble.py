"""
diabetes_feature_engineering_ensemble.py
---------------------------------------
Demonstrates advanced feature engineering and ensembling on the Diabetes dataset.
"""

import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor

X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature engineering: polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

scaler = StandardScaler()
X_train_poly_scaled = scaler.fit_transform(X_train_poly)
X_test_poly_scaled = scaler.transform(X_test_poly)

rf = RandomForestRegressor(n_estimators=100, random_state=42)
gb = GradientBoostingRegressor(n_estimators=100, random_state=42)

ensemble = VotingRegressor([('rf', rf), ('gb', gb)])
ensemble.fit(X_train_poly_scaled, y_train)
preds = ensemble.predict(X_test_poly_scaled)
print("VotingRegressor with Poly Features R2: {:.3f}".format(r2_score(y_test, preds)))