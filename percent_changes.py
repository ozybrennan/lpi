import lpi

from scipy import stats

results = lpi.analyze_LPI("eol_download_2379.csv", "weight", "percent change")
counter = results[0]
body_sizes = results[1]
average_changes = results[2]

print counter
print body_sizes
print average_changes
print stats.linregress(body_sizes, average_changes)
