"""
sklearn_intro.py
----------------
Step-by-step introduction to scikit-learn for data science.
Covers: datasets, preprocessing, model training, evaluation, and pipelines.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
import joblib
from sklearn.pipeline import Pipeline
import pandas as pd

def load_and_split():
    """Load iris dataset and split into train/test."""
    X, y = load_iris(return_X_y=True, as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print('Train shape:', X_train.shape)
    print('Test shape:', X_test.shape)
    return X_train, X_test, y_train, y_test

def train_and_evaluate():
    """Train a logistic regression and evaluate."""
    X_train, X_test, y_train, y_test = load_and_split()
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print('Accuracy:', accuracy_score(y_test, preds))
    print('Classification report:\n', classification_report(y_test, preds))

def cross_validation_example():
    """Cross-validation with logistic regression."""
    X, y = load_iris(return_X_y=True, as_frame=False)
    model = LogisticRegression(max_iter=200)
    scores = cross_val_score(model, X, y, cv=5)
    print('CV scores:', scores)
    print('Mean CV score:', scores.mean())

def grid_search_example():
    """Grid search for hyperparameter tuning."""
    X_train, X_test, y_train, y_test = load_and_split()
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', LogisticRegression(max_iter=200))
    ])
    param_grid = {
        'clf__C': [0.1, 1, 10],
        'clf__solver': ['lbfgs', 'liblinear']
    }
    grid = GridSearchCV(pipe, param_grid, cv=3)
    grid.fit(X_train, y_train)
    print('Best params:', grid.best_params_)
    print('Best score:', grid.best_score_)

def feature_selection_example():
    """Feature selection with SelectKBest."""
    X_train, X_test, y_train, y_test = load_and_split()
    selector = SelectKBest(score_func=f_classif, k=2)
    selector.fit(X_train, y_train)
    X_train_selected = selector.transform(X_train)
    print('Selected features shape:', X_train_selected.shape)

def model_persistence_example():
    """Save and load a trained model."""
    X_train, X_test, y_train, y_test = load_and_split()
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    joblib.dump(model, 'sklearn_intro_model.joblib')
    loaded = joblib.load('sklearn_intro_model.joblib')
    print('Loaded model accuracy:', loaded.score(X_test, y_test))

def multiclass_roc_example():
    """Compute multiclass ROC AUC."""
    X_train, X_test, y_train, y_test = load_and_split()
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    proba = model.predict_proba(X_test)
    auc = roc_auc_score(y_test, proba, multi_class='ovr')
    print('Multiclass ROC AUC:', auc)

def pipeline_example():
    """Build a pipeline with scaling and logistic regression."""
    X_train, X_test, y_train, y_test = load_and_split()
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', LogisticRegression(max_iter=200))
    ])
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)
    print('Pipeline accuracy:', accuracy_score(y_test, preds))

if __name__ == "__main__":
    print("--- scikit-learn Intro Examples ---")
    train_and_evaluate()
    pipeline_example()
    cross_validation_example()
    grid_search_example()
    feature_selection_example()
    model_persistence_example()
    multiclass_roc_example()
