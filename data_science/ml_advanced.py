"""
ml_advanced.py
--------------
Advanced machine learning workflows and techniques in Python.
Covers: ensemble methods, unsupervised learning, model evaluation, hyperparameter tuning, model persistence, and interpretability.
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

def random_forest_example():

# --- DRY HELPERS ---
def get_iris():
    iris = load_iris(as_frame=True)
    return iris.data, iris.target

def get_train_test(X=None, y=None, test_size=0.2, random_state=42):
    if X is None or y is None:
        X, y = get_iris()
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

# 1. ENSEMBLE METHODS
def random_forest_example():
    X, y = get_iris()
    X_train, X_test, y_train, y_test = get_train_test(X, y)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    print('Random Forest Classification Report:\n', classification_report(y_test, preds))
    print('Confusion Matrix:\n', confusion_matrix(y_test, preds))

# 2. UNSUPERVISED LEARNING

def pca_kmeans_example():
    X, _ = get_iris()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(X_pca)
    print('PCA shape:', X_pca.shape)
    print('KMeans cluster counts:', np.bincount(clusters))

# 3. MODEL EVALUATION

def cross_val_and_roc():
    X, y = get_iris()
    X_bin = (y == 0).astype(int)  # Binary for ROC
    X_train, X_test, y_train, y_test = get_train_test(X, X_bin)
    clf = GradientBoostingClassifier()
    scores = cross_val_score(clf, X_train, y_train, cv=5)
    print('CV scores:', scores)
    clf.fit(X_train, y_train)
    proba = clf.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, proba)
    print('ROC AUC:', auc)
    fpr, tpr, _ = roc_curve(y_test, proba)
    print('ROC curve FPR:', fpr)
    print('ROC curve TPR:', tpr)

# 4. HYPERPARAMETER TUNING

def grid_search_example():
    X, y = get_iris()
    X_train, X_test, y_train, y_test = get_train_test(X, y)
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

# 5. MODEL PERSISTENCE

def save_and_load_model():
    X, y = get_iris()
    X_train, X_test, y_train, y_test = get_train_test(X, y)
    clf = RandomForestClassifier(n_estimators=10, random_state=42)
    clf.fit(X_train, y_train)
    joblib.dump(clf, 'rf_model.joblib')
    loaded = joblib.load('rf_model.joblib')
    print('Loaded model accuracy:', loaded.score(X_test, y_test))

# 6. MODEL INTERPRETABILITY (Feature Importances)

def feature_importance_example():
    X, y = get_iris()
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    importances = clf.feature_importances_
    print('Feature importances:', dict(zip(X.columns, importances)))

if __name__ == "__main__":
    print("--- Advanced ML Examples ---")
    random_forest_example()
    pca_kmeans_example()
    cross_val_and_roc()
    grid_search_example()
    save_and_load_model()
    feature_importance_example()
