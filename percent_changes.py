import lpi

from scipy import stats
import matplotlib.pyplot as plt

results = lpi.analyze_LPI("eol_download_2416.csv", "length", "percent change")
counter = results[0]
body_sizes = results[1]
average_changes = results[2]

print counter
print stats.linregress(body_sizes, average_changes)
lpi.create_plot(body_sizes, average_changes, "small")
