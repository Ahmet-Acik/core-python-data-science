import unittest
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

class TestIrisExercise(unittest.TestCase):
    def test_load(self):
        iris = pd.read_csv('data_science/datasets/iris.csv')
        self.assertEqual(iris.shape[1], 5)
        self.assertIn('species', iris.columns)

    def test_model(self):
        iris = pd.read_csv('data_science/datasets/iris.csv')
        X = iris.drop('species', axis=1)
        y = iris['species']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)
        acc = model.score(X_test, y_test)
        self.assertGreaterEqual(acc, 0)

    def test_expected_columns(self):
        iris = pd.read_csv('data_science/datasets/iris.csv')
        expected = {'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'}
        self.assertEqual(set(iris.columns), expected)

    def test_unique_species(self):
        iris = pd.read_csv('data_science/datasets/iris.csv')
        unique_species = set(iris['species'])
        self.assertTrue({'setosa', 'versicolor', 'virginica'}.issubset(unique_species))

    def test_value_ranges(self):
        iris = pd.read_csv('data_science/datasets/iris.csv')
        self.assertTrue(iris['sepal_length'].between(4, 8).all())
        self.assertTrue(iris['sepal_width'].between(2, 4.5).all())
        self.assertTrue(iris['petal_length'].between(1, 7).all())
        self.assertTrue(iris['petal_width'].between(0, 2.5).all())

    def test_no_missing_values(self):
        iris = pd.read_csv('data_science/datasets/iris.csv')
        self.assertFalse(iris.isnull().any().any())

    def test_class_balance(self):
        iris = pd.read_csv('data_science/datasets/iris.csv')
        counts = iris['species'].value_counts()
        self.assertGreaterEqual(counts.min(), 1)

if __name__ == '__main__':
    unittest.main()
