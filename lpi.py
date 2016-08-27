import csv

import openpyxl
import math
import matplotlib.pyplot as plt
from scipy import stats

wb = openpyxl.load_workbook(
    "Living Planet Index-07-04-2016.xlsx")
LPI_sheet = wb.active
body_sizes= []
slopes = []
for row in range(2, 401):
    species_name = LPI_sheet.cell(row=row, column=2).value
    with open("eol_download_2379.csv", "rb") as f:
        reader = csv.reader(f)
        for eol_row in reader:
            test_species_name = eol_row[1].decode('utf-8')
            if test_species_name == species_name:
                body_size = eol_row[4]
                body_size = body_size.replace(",","")
                body_sizes.append(float(body_size))
                column = 3
                years = []
                abundances = []
                while (LPI_sheet.cell(row=row, column=column).value != None):
                    year = LPI_sheet.cell(row=row, column=column).value
                    abundance = LPI_sheet.cell(row=row,column=column+1).value
                    years.append(float(year))
                    abundances.append(float(abundance))
                    column = column + 2
                log_abundances = []
                for abundance in abundances:
                    log_abundances.append(math.asinh(abundance))
                abnormal_slope, _, _, _, _ = stats.linregress(years, log_abundances)
                first_item = log_abundances[0]
                if first_item == 0:
                    first_item = 0.00000000000000001
                slope = abnormal_slope / first_item * 100
                slopes.append(float(slope))
                break
print stats.linregress(body_sizes, slopes)
plt.plot(body_sizes, slopes, "o")
plt.xlim([0, 300000])
plt.ylim([-100, 100])
plt.show()
