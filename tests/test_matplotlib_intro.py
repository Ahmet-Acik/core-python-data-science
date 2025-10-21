import unittest
import os
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing
import matplotlib.pyplot as plt
from data_science import matplotlib_intro

class TestMatplotlibIntro(unittest.TestCase):
    def tearDown(self):
        # Clean up any files created by save_figure
        if os.path.exists('saved_plot.png'):
            os.remove('saved_plot.png')

    def test_basic_line_plot(self):
        # Should run without error and create a line plot
        try:
            matplotlib_intro.basic_line_plot()
        except Exception as e:
            self.fail(f"basic_line_plot() raised {e}")
        plt.close('all')

    def test_scatter_plot(self):
        try:
            matplotlib_intro.scatter_plot()
        except Exception as e:
            self.fail(f"scatter_plot() raised {e}")
        plt.close('all')

    def test_subplot_example(self):
        try:
            matplotlib_intro.subplot_example()
        except Exception as e:
            self.fail(f"subplot_example() raised {e}")
        plt.close('all')

    def test_save_figure(self):
        matplotlib_intro.save_figure()
        self.assertTrue(os.path.exists('saved_plot.png'))
        plt.close('all')

if __name__ == "__main__":
    unittest.main()
