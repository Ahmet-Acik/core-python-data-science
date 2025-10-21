"""
numpy_intro.py
--------------
Step-by-step introduction to NumPy for data science.
Covers: array creation, indexing, math operations, broadcasting, and random numbers.
"""

import numpy as np

def array_basics():
    """Create and inspect NumPy arrays."""
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print('Shape:', arr.shape)
    print('Data type:', arr.dtype)
    print('First row:', arr[0])
    print('Element [1,2]:', arr[1,2])
    # Reshape
    arr2 = arr.reshape(3, 2)
    print('Reshaped (3,2):', arr2)
    # Change dtype
    arr_float = arr.astype(float)
    print('As float:', arr_float)

def math_operations():
    """Elementwise math and broadcasting."""
    a = np.arange(5)
    b = np.ones(5)
    print('a + b:', a + b)
    print('a * 2:', a * 2)
    print('exp(a):', np.exp(a))
    # Aggregation
    print('Sum:', np.sum(a))
    print('Mean:', np.mean(a))
    print('Std:', np.std(a))

def slicing_and_indexing():
    """Slicing and boolean indexing."""
    arr = np.arange(10)
    print('Slice 2:7:', arr[2:7])
    print('Even numbers:', arr[arr % 2 == 0])
    # Stacking
    arr2 = arr.reshape(2, 5)
    arr3 = np.arange(10, 20).reshape(2, 5)
    print('Vertical stack:', np.vstack([arr2, arr3]))
    print('Horizontal stack:', np.hstack([arr2, arr3]))

def random_examples():
    """Random numbers and reproducibility."""
    np.random.seed(42)
    print('Random ints:', np.random.randint(0, 10, 5))
    print('Random normal:', np.random.randn(3))
    # Linear algebra
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[2, 0], [1, 2]])
    print('Matrix product:', np.dot(A, B))
    print('Transpose:', A.T)
    print('Inverse:', np.linalg.inv(A))
    print('Eigenvalues:', np.linalg.eigvals(A))

if __name__ == "__main__":
    print("--- NumPy Intro Examples ---")
    array_basics()
    math_operations()
    slicing_and_indexing()
    random_examples()
