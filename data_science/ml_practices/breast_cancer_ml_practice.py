"""
breast_cancer_ml_practice.py
----------------------------
Comprehensive ML workflow using the Breast Cancer dataset.
Covers: data exploration, preprocessing, classification, hyperparameter tuning, model persistence, and feature importance.
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

def get_breast_cancer():
    data = load_breast_cancer(as_frame=True)
    X = data.data
    y = data.target
    return X, y

def cancer_gradient_boosting():
    X, y = get_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = GradientBoostingClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    print('Gradient Boosting Classification Report:\n', classification_report(y_test, preds))
    print('Confusion Matrix:\n', confusion_matrix(y_test, preds))

def cancer_grid_search():
    X, y = get_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('gb', GradientBoostingClassifier(random_state=42))
    ])
    param_grid = {
        'gb__n_estimators': [50, 100],
        'gb__max_depth': [2, 4, 6]
    }
    grid = GridSearchCV(pipe, param_grid, cv=3)
    grid.fit(X_train, y_train)
    print('Best params:', grid.best_params_)
    print('Best score:', grid.best_score_)

def cancer_save_and_load():
    X, y = get_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = GradientBoostingClassifier(n_estimators=10, random_state=42)
    clf.fit(X_train, y_train)
    joblib.dump(clf, 'cancer_gb_model.joblib')
    loaded = joblib.load('cancer_gb_model.joblib')
    print('Loaded model accuracy:', loaded.score(X_test, y_test))

def cancer_feature_importance():
    X, y = get_breast_cancer()
    clf = GradientBoostingClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    importances = clf.feature_importances_
    feature_names = X.columns
    print('Feature importances:', dict(zip(feature_names, importances)))

if __name__ == "__main__":
    print("--- Breast Cancer Dataset ML Practice ---")
    cancer_gradient_boosting()
    cancer_grid_search()
    cancer_save_and_load()
    cancer_feature_importance()