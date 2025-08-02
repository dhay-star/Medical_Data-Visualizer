import unittest
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from medical_data_visualizer import draw_cat_plot, draw_heat_map

class MedicalDataVisualizerTestCase(unittest.TestCase):
    def test_cat_plot(self):
        fig = draw_cat_plot()
        self.assertIsNotNone(fig, "Returned figure is None")
        self.assertEqual(type(fig).__name__, 'Figure', "draw_cat_plot should return a matplotlib.figure.Figure object")

    def test_heat_map(self):
        fig = draw_heat_map()
        self.assertIsNotNone(fig, "Returned figure is None")
        self.assertEqual(type(fig).__name__, 'Figure', "draw_heat_map should return a matplotlib.figure.Figure object")

if __name__ == "__main__":
    unittest.main()
