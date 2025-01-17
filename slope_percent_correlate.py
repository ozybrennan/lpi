import lpi
from scipy import stats
import openpyxl

wb = openpyxl.load_workbook(
        "Living Planet Index-07-04-2016.xlsx")
LPI_sheet = wb.active
slopes = []
percent_changes = []
for row in range(2, 401):
    species_name = LPI_sheet.cell(row=row, column=2).value
    print species_name
    slopes.append(lpi.calculate_abundance_slopes(LPI_sheet, row))
    percent_changes.append(lpi.calculate_percent_changes_deprecated(LPI_sheet, row))

print stats.linregress(slopes, percent_changes)
