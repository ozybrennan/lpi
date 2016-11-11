import lpi

from scipy import stats
import matplotlib.pyplot as plt

results = lpi.analyze_LPI("eol_download_2379.csv", "weight", "percent change")
counter = results[0]
body_sizes = results[1]
average_changes = results[2]

lpi.create_plot(body_sizes, average_changes, "small", "percent_change")
