"""
data_loading.py
---------------
Comprehensive examples for loading, inspecting, and saving data in Python for data science.
Covers: CSV, Excel, JSON, SQL, APIs, and basic data validation.
"""

import pandas as pd
import json
import sqlite3
import requests
from typing import Any, Optional

def load_csv(filepath: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(filepath)

from typing import Union, Dict

def load_excel(filepath: str, sheet: Optional[str] = None) -> Union[pd.DataFrame, Dict[str, pd.DataFrame]]:
    """Load an Excel file (optionally a specific sheet) into a DataFrame or dict of DataFrames."""
    return pd.read_excel(filepath, sheet_name=sheet)

def load_json(filepath: str) -> Any:
    """Load a JSON file as a Python object."""
    with open(filepath) as f:
        return json.load(f)

def load_sqlite(db_path: str, query: str) -> pd.DataFrame:
    """Query a SQLite database and return a DataFrame."""
    with sqlite3.connect(db_path) as conn:
        return pd.read_sql_query(query, conn)

def fetch_api(url: str) -> Any:
    """Fetch data from a REST API and return JSON."""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_csv(df: pd.DataFrame, filepath: str) -> None:
    """Save a DataFrame to a CSV file."""
    df.to_csv(filepath, index=False)

def save_json(data: Any, filepath: str) -> None:
    """Save a Python object as JSON."""
    with open(filepath, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    print("--- Data Loading Examples ---")
    # Example usage (uncomment and provide real file paths to test)
    # df = load_csv('datasets/sample.csv')
    # print(df.head())
    # data = load_json('datasets/sample.json')
    # print(data)
    # df_sql = load_sqlite('datasets/sample.db', 'SELECT * FROM users')
    # print(df_sql.head())
    # api_data = fetch_api('https://jsonplaceholder.typicode.com/posts/1')
    # print(api_data)
