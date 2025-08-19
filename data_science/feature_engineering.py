"""
feature_engineering.py
---------------------
Comprehensive feature engineering techniques for data science and machine learning in Python.
Covers: feature creation, transformation, encoding, scaling, binning, interaction, and custom transformers (with scikit-learn pipelines).
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, LabelEncoder, KBinsDiscretizer, PolynomialFeatures
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

# 1. FEATURE CREATION

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create new features from existing columns."""
    df = df.copy()
    if 'height' in df and 'weight' in df:
        df['bmi'] = df['weight'] / (df['height']/100) ** 2
    if 'date' in df:
        df['year'] = pd.to_datetime(df['date']).dt.year
    return df

# 2. FEATURE TRANSFORMATION

def log_transform(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Apply log transform to a column (add 1 to avoid log(0))."""
    df = df.copy()
    df[col + '_log'] = np.log1p(df[col])
    return df

def scale_features(df: pd.DataFrame, cols: list, scaler=None) -> pd.DataFrame:
    """Scale columns using StandardScaler or MinMaxScaler."""
    df = df.copy()
    scaler = scaler or StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])
    return df

# 3. ENCODING

def one_hot_encode(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """One-hot encode categorical columns."""
    return pd.get_dummies(df, columns=cols)

def label_encode(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Label encode a single categorical column."""
    df = df.copy()
    le = LabelEncoder()
    df[col + '_le'] = le.fit_transform(df[col])
    return df

# 4. BINNING

def bin_numerical(df: pd.DataFrame, col: str, bins: int = 5) -> pd.DataFrame:
    """Discretize a numerical column into bins."""
    df = df.copy()
    df[col + '_bin'] = pd.cut(df[col], bins=bins, labels=False)
    return df

# 5. INTERACTION & POLYNOMIAL FEATURES

def add_interactions(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Add interaction and polynomial features for given columns."""
    pf = PolynomialFeatures(degree=2, include_bias=False, interaction_only=False)
    arr = pf.fit_transform(df[cols])
    new_cols = pf.get_feature_names_out(cols)
    df_poly = pd.DataFrame(arr, columns=new_cols, index=df.index)
    return pd.concat([df, df_poly], axis=1)

# 6. CUSTOM TRANSFORMER (for sklearn pipeline)

class ColumnSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.columns]

# Example pipeline

def example_pipeline():
    df = pd.DataFrame({
        'height': [170, 180, 160],
        'weight': [70, 80, 60],
        'gender': ['M', 'F', 'F']
    })
    pipe = Pipeline([
        ('select', ColumnSelector(['height', 'weight'])),
        ('scale', StandardScaler()),
        ('poly', PolynomialFeatures(degree=2))
    ])
    features = pipe.fit_transform(df)
    print('Pipeline features shape:', features.shape)

if __name__ == "__main__":
    print("--- Feature Engineering Examples ---")
    df = pd.DataFrame({
        'height': [170, 180, 160],
        'weight': [70, 80, 60],
        'gender': ['M', 'F', 'F'],
        'date': ['2020-01-01', '2021-06-15', '2019-12-31']
    })
    print(create_features(df))
    print(log_transform(df, 'weight'))
    print(scale_features(df, ['height', 'weight']))
    print(one_hot_encode(df, ['gender']))
    print(label_encode(df, 'gender'))
    print(bin_numerical(df, 'height', bins=3))
    print(add_interactions(df, ['height', 'weight']))
    example_pipeline()
