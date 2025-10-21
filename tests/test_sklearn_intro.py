import unittest
import os
from data_science import sklearn_intro
import joblib

class TestSklearnIntro(unittest.TestCase):
    def tearDown(self):
        # Clean up any files created by model persistence
        if os.path.exists('sklearn_intro_model.joblib'):
            os.remove('sklearn_intro_model.joblib')

    def test_load_and_split(self):
        X_train, X_test, y_train, y_test = sklearn_intro.load_and_split()
        self.assertEqual(X_train.shape[0] + X_test.shape[0], 150)
        self.assertEqual(len(y_train) + len(y_test), 150)

    def test_train_and_evaluate(self):
        try:
            sklearn_intro.train_and_evaluate()
        except Exception as e:
            self.fail(f"train_and_evaluate() raised {e}")

    def test_pipeline_example(self):
        try:
            sklearn_intro.pipeline_example()
        except Exception as e:
            self.fail(f"pipeline_example() raised {e}")

    def test_cross_validation_example(self):
        try:
            sklearn_intro.cross_validation_example()
        except Exception as e:
            self.fail(f"cross_validation_example() raised {e}")

    def test_grid_search_example(self):
        try:
            sklearn_intro.grid_search_example()
        except Exception as e:
            self.fail(f"grid_search_example() raised {e}")

    def test_feature_selection_example(self):
        try:
            sklearn_intro.feature_selection_example()
        except Exception as e:
            self.fail(f"feature_selection_example() raised {e}")

    def test_model_persistence_example(self):
        sklearn_intro.model_persistence_example()
        self.assertTrue(os.path.exists('sklearn_intro_model.joblib'))
        loaded = joblib.load('sklearn_intro_model.joblib')
        self.assertTrue(hasattr(loaded, 'predict'))

    def test_multiclass_roc_example(self):
        try:
            sklearn_intro.multiclass_roc_example()
        except Exception as e:
            self.fail(f"multiclass_roc_example() raised {e}")

if __name__ == "__main__":
    unittest.main()
