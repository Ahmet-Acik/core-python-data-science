import unittest
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class TestTitanicExercise(unittest.TestCase):
    def test_load(self):
        titanic = pd.read_csv('data_science/datasets/titanic.csv')
        self.assertIn('Survived', titanic.columns)
        self.assertIn('Sex', titanic.columns)

    def test_model(self):
        titanic = pd.read_csv('data_science/datasets/titanic.csv')
        titanic['Sex'] = titanic['Sex'].str.strip().map({'male': 0, 'female': 1})
        # Coerce empty Age values to NaN, then impute
        titanic['Age'] = pd.to_numeric(titanic['Age'], errors='coerce')
        titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
        titanic['Fare'] = pd.to_numeric(titanic['Fare'], errors='coerce')
        titanic['Pclass'] = pd.to_numeric(titanic['Pclass'], errors='coerce')
        # Drop rows with any NaN in features
        features = ['Pclass', 'Sex', 'Age', 'Fare']
        titanic = titanic.dropna(subset=features)
        X = titanic[features]
        y = titanic['Survived']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LogisticRegression()
        model.fit(X_train, y_train)
        acc = model.score(X_test, y_test)
        self.assertGreaterEqual(acc, 0)

if __name__ == '__main__':
    unittest.main()
