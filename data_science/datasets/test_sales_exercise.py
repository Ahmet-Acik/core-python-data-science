import unittest
import pandas as pd

class TestSalesExercise(unittest.TestCase):
    def test_load(self):
        sales = pd.read_json('data_science/datasets/sales.json')
        self.assertIn('revenue', sales.columns)
        self.assertEqual(sales.shape[0], 3)

    def test_total_revenue(self):
        sales = pd.read_json('data_science/datasets/sales.json')
        self.assertEqual(sales['revenue'].sum(), 575.0)

if __name__ == '__main__':
    unittest.main()
