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
import os
from typing import Any, Optional, Union, Dict

def load_csv(filepath: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(filepath)

def load_excel(filepath: str, sheet: Optional[str] = None) -> Union[pd.DataFrame, Dict[str, pd.DataFrame]]:
    """Load an Excel file (optionally a specific sheet) into a DataFrame or dict of DataFrames."""
    return pd.read_excel(filepath, sheet_name=sheet)

def load_json(filepath: str) -> Any:
    """Load a JSON file as a Python object."""
    with open(filepath, 'r') as f:
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
        json.dump(data, f, indent=2)

def create_sample_data():
    """Create sample data files for demonstration."""
    # Create datasets directory if it doesn't exist
    os.makedirs('datasets', exist_ok=True)
    
    # Create sample CSV
    sample_df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'London', 'Tokyo']
    })
    sample_df.to_csv('datasets/sample.csv', index=False)
    
    # Create sample JSON
    sample_json = {
        'users': [
            {'id': 1, 'name': 'Alice', 'active': True},
            {'id': 2, 'name': 'Bob', 'active': False}
        ]
    }
    with open('datasets/sample.json', 'w') as f:
        json.dump(sample_json, f, indent=2)
    
    # Create sample SQLite database
    conn = sqlite3.connect('datasets/sample.db')
    sample_df.to_sql('users', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    print("--- Data Loading Examples ---")
    
    # Create sample data first
    create_sample_data()
    print("Sample data created!")
    
    # Load CSV example
    try:
        df = load_csv('datasets/sample.csv')
        print("\nCSV Data:")
        print(df.head())
    except FileNotFoundError:
        print("CSV file not found")
    
    # Load JSON example
    try:
        data = load_json('datasets/sample.json')
        print("\nJSON Data:")
        print(data)
    except FileNotFoundError:
        print("JSON file not found")
    
    # Load SQLite example
    try:
        df_sql = load_sqlite('datasets/sample.db', 'SELECT * FROM users')
        print("\nSQLite Data:")
        print(df_sql.head())
    except Exception as e:
        print(f"SQLite error: {e}")
    
    # API example (this should work without local files)
    try:
        api_data = fetch_api('https://jsonplaceholder.typicode.com/posts/1')
        print("\nAPI Data:")
        print(f"Title: {api_data['title']}")
        print(f"Body: {api_data['body'][:50]}...")
    except Exception as e:
        print(f"API error: {e}")