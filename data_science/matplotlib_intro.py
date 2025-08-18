"""
matplotlib_intro.py
-------------------
Step-by-step introduction to matplotlib for data science.
Covers: basic plots, customization, subplots, and saving figures.
"""

import matplotlib.pyplot as plt
import numpy as np

def basic_line_plot():
    """Create a simple line plot."""
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y, label='sin(x)')
    plt.title('Basic Line Plot')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.legend()
    plt.show()

def scatter_plot():
    """Create a scatter plot."""
    x = np.random.rand(50)
    y = np.random.rand(50)
    plt.scatter(x, y, color='red', alpha=0.6)
    plt.title('Scatter Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def subplot_example():
    """Create multiple subplots in one figure."""
    x = np.linspace(0, 2 * np.pi, 100)
    fig, axs = plt.subplots(2)
    axs[0].plot(x, np.sin(x))
    axs[0].set_title('Sine')
    axs[1].plot(x, np.cos(x), 'r')
    axs[1].set_title('Cosine')
    plt.tight_layout()
    plt.show()

def save_figure():
    """Save a plot to a file."""
    x = np.arange(5)
    y = x ** 2
    plt.plot(x, y)
    plt.title('Saved Plot')
    plt.savefig('saved_plot.png')
    plt.close()

if __name__ == "__main__":
    print("--- Matplotlib Intro Examples ---")
    # Uncomment to test
    basic_line_plot()
    scatter_plot()
    subplot_example()
    save_figure()
