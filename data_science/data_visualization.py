"""
data_visualization.py
---------------------
Comprehensive data visualization examples for data science in Python.
Covers: matplotlib, seaborn, pandas plotting, and plotly basics.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Matplotlib example
def plot_line():
    """Plot a simple line chart with matplotlib."""
    x = [1, 2, 3, 4]
    y = [10, 20, 25, 30]
    plt.plot(x, y, marker='o')
    plt.title('Line Chart')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

# Seaborn example
def plot_histogram():
    """Plot a histogram with seaborn."""
    data = sns.load_dataset('iris')
    sns.histplot(data=data, x='sepal_length', kde=True)
    plt.title('Sepal Length Distribution')
    plt.show()

# Pandas plotting example
def plot_pandas():
    """Plot a DataFrame column using pandas built-in plot."""
    df = pd.DataFrame({'values': [1, 3, 2, 4]})
    df['values'].plot(kind='bar')
    plt.title('Bar Plot')
    plt.show()

# Plotly example
def plot_plotly():
    """Plot an interactive scatter plot with plotly."""
    df = px.data.iris()
    fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', title='Iris Sepal Dimensions')
    fig.show()

if __name__ == "__main__":
    print("--- Data Visualization Examples ---")
    # Uncomment to test each plot
    plot_line()
    plot_histogram()
    plot_pandas()
    plot_plotly()
