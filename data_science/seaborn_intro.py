"""
seaborn_intro.py
----------------
Step-by-step introduction to seaborn for data science.
Covers: basic plots, categorical plots, regression plots, and style customization.
"""

import seaborn as sns
import matplotlib.pyplot as plt

def basic_scatter():
    """Scatter plot with seaborn."""
    data = sns.load_dataset('iris')
    sns.scatterplot(x='sepal_length', y='sepal_width', data=data, hue='species')
    plt.title('Iris Sepal Scatter')
    plt.show()

def categorical_plot():
    """Bar plot for categorical data."""
    data = sns.load_dataset('titanic')
    sns.countplot(x='class', data=data, hue='sex')
    plt.title('Passenger Class Count')
    plt.show()

def regression_plot():
    """Regression plot with seaborn."""
    data = sns.load_dataset('tips')
    sns.regplot(x='total_bill', y='tip', data=data)
    plt.title('Tip vs Total Bill')
    plt.show()

def style_customization():
    """Customize seaborn style."""
    sns.set_style('whitegrid')
    data = sns.load_dataset('iris')
    sns.boxplot(x='species', y='petal_length', data=data)
    plt.title('Petal Length by Species')
    plt.show()

if __name__ == "__main__":
    print("--- Seaborn Intro Examples ---")
    # Uncomment to test
    basic_scatter()
    categorical_plot()
    regression_plot()
    style_customization()
