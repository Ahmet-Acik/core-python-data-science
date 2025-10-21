import unittest
import numpy as np
from data_science import numpy_intro

class TestNumpyIntro(unittest.TestCase):
    def test_array_basics(self):
        # Test array creation, shape, dtype, reshape, and astype
        arr = np.array([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(arr.shape, (2, 3))
        self.assertEqual(arr.dtype, np.int64 if hasattr(np, 'int64') else arr.dtype)
        arr2 = arr.reshape(3, 2)
        self.assertEqual(arr2.shape, (3, 2))
        arr_float = arr.astype(float)
        self.assertTrue(np.issubdtype(arr_float.dtype, np.floating))

    def test_math_operations(self):
        a = np.arange(5)
        b = np.ones(5)
        self.assertTrue(np.array_equal(a + b, np.array([1,2,3,4,5])))
        self.assertTrue(np.array_equal(a * 2, np.array([0,2,4,6,8])))
        self.assertTrue(np.allclose(np.exp(a), np.exp(np.arange(5))))
        self.assertEqual(np.sum(a), 10)
        self.assertEqual(np.mean(a), 2)
        self.assertAlmostEqual(np.std(a), np.std(np.arange(5)))

    def test_slicing_and_indexing(self):
        arr = np.arange(10)
        self.assertTrue(np.array_equal(arr[2:7], np.array([2,3,4,5,6])))
        self.assertTrue(np.array_equal(arr[arr % 2 == 0], np.array([0,2,4,6,8])))
        arr2 = arr.reshape(2, 5)
        arr3 = np.arange(10, 20).reshape(2, 5)
        vstack = np.vstack([arr2, arr3])
        hstack = np.hstack([arr2, arr3])
        self.assertEqual(vstack.shape, (4, 5))
        self.assertEqual(hstack.shape, (2, 10))

    def test_random_examples(self):
        np.random.seed(42)
        rand_ints = np.random.randint(0, 10, 5)
        self.assertEqual(len(rand_ints), 5)
        rand_norm = np.random.randn(3)
        self.assertEqual(rand_norm.shape, (3,))
        # Linear algebra
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[2, 0], [1, 2]])
        mat_prod = np.dot(A, B)
        self.assertTrue(np.array_equal(mat_prod, np.array([[4, 4], [10, 8]])))
        self.assertTrue(np.array_equal(A.T, np.array([[1, 3], [2, 4]])))
        inv_A = np.linalg.inv(A)
        self.assertTrue(np.allclose(np.dot(A, inv_A), np.eye(2)))
        eigvals = np.linalg.eigvals(A)
        self.assertEqual(len(eigvals), 2)

if __name__ == "__main__":
    unittest.main()
