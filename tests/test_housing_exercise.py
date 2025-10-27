import unittest
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class TestHousingExercise(unittest.TestCase):
    def test_load(self):
        housing = pd.read_csv('data_science/datasets/housing.csv')
        self.assertIn('median_house_value', housing.columns)

    def test_model(self):
        housing = pd.read_csv('data_science/datasets/housing.csv')
        housing['income_per_lat'] = housing['median_income'] / housing['latitude']
        X = housing[['longitude', 'latitude', 'median_income', 'income_per_lat']]
        y = housing['median_house_value']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        r2 = model.score(X_test, y_test)
        self.assertFalse(pd.isna(r2), "R² score is NaN")
        self.assertGreaterEqual(r2, 0)

    def test_expected_columns(self):
        housing = pd.read_csv('data_science/datasets/housing.csv')
        expected = {'longitude', 'latitude', 'median_income', 'median_house_value'}
        self.assertEqual(set(housing.columns), expected)

    def test_value_ranges(self):
        housing = pd.read_csv('data_science/datasets/housing.csv')
        self.assertTrue(housing['longitude'].between(-123, -121).all())
        self.assertTrue(housing['latitude'].between(37, 39).all())
        self.assertTrue(housing['median_income'].between(0, 15).all())
        self.assertTrue(housing['median_house_value'].between(100000, 700000).all())


if __name__ == '__main__':
    unittest.main()
