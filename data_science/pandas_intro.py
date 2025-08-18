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

def dataframe_basics():
    """Create and inspect a DataFrame."""
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    print('DataFrame:\n', df)
    print('Columns:', df.columns)
    print('First row:', df.iloc[0])

def selection_and_filtering():
    """Select/filter rows and columns."""
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print('A > 1:\n', df[df['A'] > 1])
    print('Select column B:', df['B'])

def aggregation_and_plot():
    """Aggregate and plot data."""
    df = pd.DataFrame({'group': ['x', 'x', 'y'], 'value': [1, 2, 3]})
    print('Group mean:\n', df.groupby('group')['value'].mean())
    df['value'].plot(kind='bar', title='Bar Plot')
    import matplotlib.pyplot as plt
    plt.show()

if __name__ == "__main__":
    print("--- Pandas Intro Examples ---")
    series_basics()
    dataframe_basics()
    selection_and_filtering()
    aggregation_and_plot()
