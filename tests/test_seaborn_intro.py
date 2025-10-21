import unittest
import os
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing
import seaborn as sns
import matplotlib.pyplot as plt
from data_science import seaborn_intro

class TestSeabornIntro(unittest.TestCase):
    def tearDown(self):
        # Clean up any files created by savefig
        if os.path.exists('seaborn_intro_boxplot.png'):
            os.remove('seaborn_intro_boxplot.png')

    def test_basic_scatter(self):
        try:
            seaborn_intro.basic_scatter()
        except Exception as e:
            self.fail(f"basic_scatter() raised {e}")
        plt.close('all')

    def test_categorical_plot(self):
        try:
            seaborn_intro.categorical_plot()
        except Exception as e:
            self.fail(f"categorical_plot() raised {e}")
        plt.close('all')

    def test_regression_plot(self):
        try:
            seaborn_intro.regression_plot()
        except Exception as e:
            self.fail(f"regression_plot() raised {e}")
        plt.close('all')

    def test_style_customization(self):
        seaborn_intro.style_customization()
        self.assertTrue(os.path.exists('seaborn_intro_boxplot.png'))
        plt.close('all')

if __name__ == "__main__":
    unittest.main()
