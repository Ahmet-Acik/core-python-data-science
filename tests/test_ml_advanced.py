import unittest
import os
from data_science import ml_advanced
import joblib

class TestMLAdvanced(unittest.TestCase):
    def test_random_forest_example(self):
        try:
            ml_advanced.random_forest_example()
        except Exception as e:
            self.fail(f"random_forest_example() raised {e}")

    def test_pca_kmeans_example(self):
        try:
            ml_advanced.pca_kmeans_example()
        except Exception as e:
            self.fail(f"pca_kmeans_example() raised {e}")

    def test_cross_val_and_roc(self):
        try:
            ml_advanced.cross_val_and_roc()
        except Exception as e:
            self.fail(f"cross_val_and_roc() raised {e}")

    def test_grid_search_example(self):
        try:
            ml_advanced.grid_search_example()
        except Exception as e:
            self.fail(f"grid_search_example() raised {e}")

    def test_save_and_load_model(self):
        ml_advanced.save_and_load_model()
        self.assertTrue(os.path.exists('rf_model.joblib'))
        loaded = joblib.load('rf_model.joblib')
        self.assertTrue(hasattr(loaded, 'predict'))
        os.remove('rf_model.joblib')

    def test_feature_importance_example(self):
        try:
            ml_advanced.feature_importance_example()
        except Exception as e:
            self.fail(f"feature_importance_example() raised {e}")

if __name__ == "__main__":
    unittest.main()
