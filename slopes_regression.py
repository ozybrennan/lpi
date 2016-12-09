import lpi

from scipy import stats
import matplotlib.pyplot as plt

results = lpi.analyze_LPI("eol_download_2416.csv", "length", "slopes")
counter = results[0]
body_sizes = results[1]
slopes = results[2]

lpi.create_plot(body_sizes, slopes, "small")
