"""
Sales JSON Exercise
-------------------
Practice loading and analyzing sales data from JSON.
"""
import pandas as pd

# 1. Load the dataset
sales = pd.read_json('sales.json')
print(sales.head())

# 2. Total revenue
print('Total revenue:', sales['revenue'].sum())

# 3. Revenue by item
print(sales.groupby('item')['revenue'].sum())
