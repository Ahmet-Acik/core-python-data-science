import unittest
import pandas as pd

class TestMNISTExercise(unittest.TestCase):
    def test_load(self):
        mnist = pd.read_csv('data_science/datasets/mnist_sample.csv')
        self.assertIn('label', mnist.columns)
        self.assertEqual(mnist.shape[1], 6)

    def test_labels(self):
        mnist = pd.read_csv('data_science/datasets/mnist_sample.csv')
        self.assertTrue(mnist['label'].isin([0,1,2,4,7]).all())

if __name__ == '__main__':
    unittest.main()
