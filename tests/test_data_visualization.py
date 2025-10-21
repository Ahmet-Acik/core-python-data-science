import unittest
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for tests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
from data_science import data_visualization

class TestDataVisualization(unittest.TestCase):
    def test_plot_line(self):
        # Should not raise error and create a figure
        plt.close('all')
        data_visualization.plot_line()
        self.assertTrue(len(plt.get_fignums()) > 0)
        plt.close('all')

    def test_plot_histogram(self):
        plt.close('all')
        data_visualization.plot_histogram()
        self.assertTrue(len(plt.get_fignums()) > 0)
        plt.close('all')

    def test_plot_pandas(self):
        plt.close('all')
        data_visualization.plot_pandas()
        self.assertTrue(len(plt.get_fignums()) > 0)
        plt.close('all')

    def test_plot_plotly(self):
        # Should not raise error and create a plotly figure
        fig = px.scatter(px.data.iris(), x='sepal_width', y='sepal_length', color='species')
        self.assertIsNotNone(fig)

if __name__ == '__main__':
    unittest.main()
