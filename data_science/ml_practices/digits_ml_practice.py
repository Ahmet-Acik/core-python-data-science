"""
digits_ml_practice.py
---------------------
Comprehensive ML workflow using the Digits dataset.
Covers: data exploration, preprocessing, classification, hyperparameter tuning, model persistence, and feature importance.
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

def get_digits():
    data = load_digits(as_frame=True)
    X = data.data
    y = data.target
    return X, y

def digits_random_forest():
    X, y = get_digits()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    print('Random Forest Classification Report:\n', classification_report(y_test, preds))
    print('Confusion Matrix:\n', confusion_matrix(y_test, preds))

def digits_grid_search():
    X, y = get_digits()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('rf', RandomForestClassifier(random_state=42))
    ])
    param_grid = {
        'rf__n_estimators': [50, 100],
        'rf__max_depth': [2, 4, 6]
    }
    grid = GridSearchCV(pipe, param_grid, cv=3)
    grid.fit(X_train, y_train)
    print('Best params:', grid.best_params_)
    print('Best score:', grid.best_score_)

def digits_save_and_load():
    X, y = get_digits()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=10, random_state=42)
    clf.fit(X_train, y_train)
    joblib.dump(clf, 'digits_rf_model.joblib')
    loaded = joblib.load('digits_rf_model.joblib')
    print('Loaded model accuracy:', loaded.score(X_test, y_test))

def digits_feature_importance():
    X, y = get_digits()
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    importances = clf.feature_importances_
    feature_names = X.columns
    print('Feature importances:', dict(zip(feature_names, importances)))

if __name__ == "__main__":
    print("--- Digits Dataset ML Practice ---")
    digits_random_forest()
    digits_grid_search()
    digits_save_and_load()
    digits_feature_importance()