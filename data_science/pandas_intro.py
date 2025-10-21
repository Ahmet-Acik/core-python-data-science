"""
pandas_intro.py
---------------
Step-by-step introduction to pandas for data science.
Covers: Series, DataFrame creation, indexing, selection, aggregation, and basic plotting.
"""

import pandas as pd
import numpy as np

def series_basics():
    """Create and inspect a pandas Series."""
    s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    print('Series:\n', s)
    print('Index:', s.index)
    print('Values:', s.values)
    print('Element b:', s['b'])
    # Handling missing data
    s2 = pd.Series([1, np.nan, 3])
    print('Missing values:', s2.isnull().sum())
    print('Fillna:', s2.fillna(0))

def dataframe_basics():
    """Create and inspect a DataFrame."""
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    print('DataFrame:\n', df)
    print('Columns:', df.columns)
    print('First row:', df.iloc[0])
    # Sorting
    df2 = pd.DataFrame({'A': [2, 1], 'B': [4, 3]})
    print('Sorted by A:', df2.sort_values('A'))
    # Reshaping
    df3 = pd.DataFrame({'A': ['foo', 'foo', 'bar'], 'B': [1, 2, 3]})
    print('Pivot table:', df3.pivot_table(index='A', values='B', aggfunc='sum'))

def selection_and_filtering():
    """Select/filter rows and columns."""
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print('A > 1:\n', df[df['A'] > 1])
    print('Select column B:', df['B'])
    # Merging
    df_left = pd.DataFrame({'key': ['a', 'b', 'c'], 'val1': [1, 2, 3]})
    df_right = pd.DataFrame({'key': ['a', 'b', 'd'], 'val2': [4, 5, 6]})
    merged = pd.merge(df_left, df_right, on='key', how='outer')
    print('Merged DataFrame:\n', merged)

def aggregation_and_plot():
    """Aggregate and plot data."""
    df = pd.DataFrame({'group': ['x', 'x', 'y'], 'value': [1, 2, 3]})
    print('Group mean:\n', df.groupby('group')['value'].mean())
    df['value'].plot(kind='bar', title='Bar Plot')
    import matplotlib.pyplot as plt
    plt.show()
    # Exporting
    df.to_csv('pandas_intro_export.csv', index=False)
    print('Exported to pandas_intro_export.csv')

if __name__ == "__main__":
    print("--- Pandas Intro Examples ---")
    series_basics()
    dataframe_basics()
    selection_and_filtering()
    aggregation_and_plot()
