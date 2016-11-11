import lpi
import openpyxl
import matplotlib.pyplot as plt

wb = openpyxl.load_workbook(
    "Living Planet Index-07-04-2016.xlsx")
LPI_sheet = wb.active
for row in range(2, 401):
    species_name = LPI_sheet.cell(row=row, column=2).value
    print species_name
    years, abundances = lpi.years_and_abundances(LPI_sheet, row)
    if max(abundances) > 40:
        continue
    plt.plot(years, abundances)
plt.show()
