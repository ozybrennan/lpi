import lpi

from scipy import stats
import matplotlib.pyplot as plt

results = lpi.analyze_LPI("eol_download_2379.csv", "weight", "slopes")
counter = results[0]
body_sizes = results[1]
slopes = results[2]

print counter
print stats.linregress(body_sizes, slopes)
#plt.plot(body_sizes, slopes, "o")
#plt.xlim([0, 5000])
#plt.ylim([200, -200])
#plt.show()
