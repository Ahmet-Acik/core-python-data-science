"""
MNIST Sample Exercise
---------------------
Practice loading and visualizing digit data.
"""
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
mnist = pd.read_csv('mnist_sample.csv')
print(mnist.head())

# 2. Visualize a digit
pixels = mnist.iloc[0, 1:].values.reshape(1, -1)
plt.imshow(pixels, cmap='gray')
plt.title(f'Label: {mnist.iloc[0, 0]}')
plt.show()
