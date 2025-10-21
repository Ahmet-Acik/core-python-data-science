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
    # Pairplot
    sns.pairplot(data, hue='species')
    plt.suptitle('Iris Pairplot', y=1.02)
    plt.show()

def categorical_plot():
    """Bar plot for categorical data."""
    data = sns.load_dataset('titanic')
    sns.countplot(x='class', data=data, hue='sex')
    plt.title('Passenger Class Count')
    plt.show()
    # FacetGrid
    g = sns.FacetGrid(data, col='sex')
    g.map(sns.histplot, 'age')
    plt.suptitle('Age Distribution by Sex', y=1.02)
    plt.show()

def regression_plot():
    """Regression plot with seaborn."""
    data = sns.load_dataset('tips')
    sns.regplot(x='total_bill', y='tip', data=data)
    plt.title('Tip vs Total Bill')
    plt.show()
    # Heatmap
    corr = data.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

def style_customization():
    """Customize seaborn style."""
    sns.set_style('whitegrid')
    sns.set_palette('Set2')
    data = sns.load_dataset('iris')
    sns.boxplot(x='species', y='petal_length', data=data)
    plt.title('Petal Length by Species')
    plt.savefig('seaborn_intro_boxplot.png')
    print('Boxplot saved as seaborn_intro_boxplot.png')
    plt.show()

if __name__ == "__main__":
    print("--- Seaborn Intro Examples ---")
    # Uncomment to test
    basic_scatter()
    categorical_plot()
    regression_plot()
    style_customization()
