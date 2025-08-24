# """
# diabetes_ml_practice.py
# -----------------------
# Comprehensive ML workflow using the Diabetes dataset.
# Covers: data exploration, preprocessing, regression with multiple models, hyperparameter tuning, model persistence, and feature importance.
# """

# import pandas as pd
# import numpy as np
# from sklearn.datasets import load_diabetes
# from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
# from sklearn.linear_model import LinearRegression, Ridge, Lasso
# from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import Pipeline
# import joblib

# try:
#     from xgboost import XGBRegressor
#     xgb_installed = True
# except ImportError:
#     xgb_installed = False

# def get_diabetes():
#     data = load_diabetes(as_frame=True)
#     X = data.data
#     y = data.target
#     return X, y

# def evaluate_model(model, X_train, X_test, y_train, y_test, name="Model"):
#     model.fit(X_train, y_train)
#     preds = model.predict(X_test)
#     print('{} MSE:'.format(name), mean_squared_error(y_test, preds))
#     print('{} R2:'.format(name), r2_score(y_test, preds))
#     return model

# def diabetes_all_models():
#     X, y = get_diabetes()
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     scaler = StandardScaler()
#     X_train_scaled = scaler.fit_transform(X_train)
#     X_test_scaled = scaler.transform(X_test)

#     print("\n--- Linear Regression ---")
#     evaluate_model(LinearRegression(), X_train_scaled, X_test_scaled, y_train, y_test, "Linear Regression")

#     print("\n--- Ridge Regression ---")
#     evaluate_model(Ridge(alpha=1.0), X_train_scaled, X_test_scaled, y_train, y_test, "Ridge Regression")

#     print("\n--- Lasso Regression ---")
#     evaluate_model(Lasso(alpha=0.1), X_train_scaled, X_test_scaled, y_train, y_test, "Lasso Regression")

#     print("\n--- Random Forest Regressor ---")
#     evaluate_model(RandomForestRegressor(n_estimators=100, random_state=42), X_train, X_test, y_train, y_test, "Random Forest")

#     print("\n--- Gradient Boosting Regressor ---")
#     evaluate_model(GradientBoostingRegressor(n_estimators=100, random_state=42), X_train, X_test, y_train, y_test, "Gradient Boosting")

#     if xgb_installed:
#         print("\n--- XGBoost Regressor ---")
#         evaluate_model(XGBRegressor(n_estimators=100, random_state=42, verbosity=0), X_train, X_test, y_train, y_test, "XGBoost")
#     else:
#         print("\n--- XGBoost Regressor ---")
#         print("XGBoost is not installed. Skipping XGBoost evaluation.")

# def diabetes_grid_search():
#     X, y = get_diabetes()
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     pipe = Pipeline([
#         ('scaler', StandardScaler()),
#         ('ridge', Ridge())
#     ])
#     param_grid = {
#         'ridge__alpha': [0.01, 0.1, 1.0, 10.0]
#     }
#     grid = GridSearchCV(pipe, param_grid, cv=3)
#     grid.fit(X_train, y_train)
#     print('Best params:', grid.best_params_)
#     print('Best score:', grid.best_score_)

# def diabetes_save_and_load():
#     X, y = get_diabetes()
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     reg = GradientBoostingRegressor(n_estimators=100, random_state=42)
#     reg.fit(X_train, y_train)
#     joblib.dump(reg, 'diabetes_gb_model.joblib')
#     loaded = joblib.load('diabetes_gb_model.joblib')
#     print('Loaded GradientBoostingRegressor R2:', loaded.score(X_test, y_test))

# def diabetes_feature_importance():
#     X, y = get_diabetes()
#     reg = GradientBoostingRegressor(n_estimators=100, random_state=42)
#     reg.fit(X, y)
#     importances = reg.feature_importances_
#     feature_names = X.columns
#     print('Feature importances:', dict(zip(feature_names, importances)))

# if __name__ == "__main__":
#     print("--- Diabetes Dataset ML Practice ---")
#     diabetes_all_models()
#     diabetes_grid_search()
#     diabetes_save_and_load()
#     diabetes_feature_importance()

"""
diabetes_ml_practice.py
-----------------------
Comprehensive ML workflow using the Diabetes dataset.
Covers: data exploration, preprocessing, regression with multiple models, wide hyperparameter tuning, polynomial features, model persistence, and feature importance.
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
import joblib

try:
    from xgboost import XGBRegressor
    xgb_installed = True
except ImportError:
    xgb_installed = False

def get_diabetes():
    data = load_diabetes(as_frame=True)
    X = data.data
    y = data.target
    return X, y

def evaluate_model(model, X_train, X_test, y_train, y_test, name="Model"):
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print('{} MSE:'.format(name), mean_squared_error(y_test, preds))
    print('{} R2:'.format(name), r2_score(y_test, preds))
    return model

def diabetes_all_models():
    X, y = get_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("\n--- Linear Regression ---")
    evaluate_model(LinearRegression(), X_train_scaled, X_test_scaled, y_train, y_test, "Linear Regression")

    print("\n--- Ridge Regression ---")
    evaluate_model(Ridge(alpha=1.0), X_train_scaled, X_test_scaled, y_train, y_test, "Ridge Regression")

    print("\n--- Lasso Regression ---")
    evaluate_model(Lasso(alpha=0.1), X_train_scaled, X_test_scaled, y_train, y_test, "Lasso Regression")

    print("\n--- Random Forest Regressor ---")
    evaluate_model(RandomForestRegressor(n_estimators=100, random_state=42), X_train, X_test, y_train, y_test, "Random Forest")

    print("\n--- Gradient Boosting Regressor ---")
    evaluate_model(GradientBoostingRegressor(n_estimators=100, random_state=42), X_train, X_test, y_train, y_test, "Gradient Boosting")

    if xgb_installed:
        print("\n--- XGBoost Regressor ---")
        evaluate_model(XGBRegressor(n_estimators=100, random_state=42, verbosity=0), X_train, X_test, y_train, y_test, "XGBoost")
    else:
        print("\n--- XGBoost Regressor ---")
        print("XGBoost is not installed. Skipping XGBoost evaluation.")

def diabetes_grid_search():
    X, y = get_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('ridge', Ridge())
    ])
    param_grid = {
        'ridge__alpha': [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]
    }
    grid = GridSearchCV(pipe, param_grid, cv=5)
    grid.fit(X_train, y_train)
    print('Best params:', grid.best_params_)
    print('Best score:', grid.best_score_)

def diabetes_poly_features():
    X, y = get_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipe = Pipeline([
        ('poly', PolynomialFeatures(degree=2, include_bias=False)),
        ('scaler', StandardScaler()),
        ('ridge', Ridge(alpha=1.0))
    ])
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)
    print('\n--- Ridge Regression with Polynomial Features (degree=2) ---')
    print('Poly Ridge MSE:', mean_squared_error(y_test, preds))
    print('Poly Ridge R2:', r2_score(y_test, preds))

def diabetes_save_and_load():
    X, y = get_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    reg = GradientBoostingRegressor(n_estimators=100, random_state=42)
    reg.fit(X_train, y_train)
    joblib.dump(reg, 'diabetes_gb_model.joblib')
    loaded = joblib.load('diabetes_gb_model.joblib')
    print('Loaded GradientBoostingRegressor R2:', loaded.score(X_test, y_test))

def diabetes_feature_importance():
    X, y = get_diabetes()
    reg = GradientBoostingRegressor(n_estimators=100, random_state=42)
    reg.fit(X, y)
    importances = reg.feature_importances_
    feature_names = X.columns
    print('Feature importances:', dict(zip(feature_names, importances)))

if __name__ == "__main__":
    print("--- Diabetes Dataset ML Practice ---")
    diabetes_all_models()
    diabetes_grid_search()
    diabetes_poly_features()
    diabetes_save_and_load()
    diabetes_feature_importance()