"""
data_cleaning.py
----------------
Comprehensive data cleaning and preprocessing examples for data science in Python.
Covers: missing values, duplicates, type conversion, outlier handling, string cleaning, and feature engineering.
"""

import pandas as pd
import numpy as np
import re
from typing import Any

def drop_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows with any missing values."""
    return df.dropna()

def fill_missing(df: pd.DataFrame, value: Any = 0) -> pd.DataFrame:
    """Fill missing values with a specified value (default=0)."""
    return df.fillna(value)

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows."""
    return df.drop_duplicates()

def convert_types(df: pd.DataFrame, col_types: dict) -> pd.DataFrame:
    """Convert columns to specified types."""
    return df.astype(col_types)

from typing import Optional

def handle_outliers(df: pd.DataFrame, col: str, method: str = 'clip', lower: Optional[float] = None, upper: Optional[float] = None) -> pd.DataFrame:
    """Handle outliers in a column by clipping or removing."""
    if method == 'clip':
        return df.assign(**{col: df[col].clip(lower, upper)})
    elif method == 'remove':
        return df[(df[col] >= lower) & (df[col] <= upper)]
    else:
        raise ValueError("method must be 'clip' or 'remove'")

def clean_strings(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Trim whitespace and lowercase a string column."""
    df[col] = df[col].str.strip().str.lower()
    return df

def extract_numbers(df: pd.DataFrame, col: str) -> pd.Series:
    """Extract numbers from a string column using regex."""
    return df[col].str.extract(r'(\d+)')[0]

if __name__ == "__main__":
    print("--- Data Cleaning Examples ---")
    # Example usage (uncomment and provide a real DataFrame to test)
    df = pd.DataFrame({'A': [1, None, 3], 'B': [' x ', 'Y', 'z ']})
    print(drop_missing(df))
    print(fill_missing(df, 99))
    print(remove_duplicates(df))
    print(convert_types(df, {'A': 'float64'}))
    print(handle_outliers(df, 'A', 'clip', 1, 2))
    print(clean_strings(df, 'B'))
    print(extract_numbers(pd.DataFrame({'C': ['abc123', 'def456']}), 'C'))
