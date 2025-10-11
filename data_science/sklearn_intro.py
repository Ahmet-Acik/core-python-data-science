"""
sklearn_intro.py
----------------
Step-by-step introduction to scikit-learn for data science.
Covers: datasets, preprocessing, model training, evaluation, and pipelines.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd

def load_and_split():
    """Load iris dataset and split into train/test."""
    iris = load_iris(as_frame=True)  # Remove the unpacking with *, _
    X = iris.data
    y = iris.target
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
