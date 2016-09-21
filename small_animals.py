import openpyxl
from scipy import stats

def find_the_smallest(column, datatype):
    species_sizes = []
    for row in range(2, sheet.max_row):
        body_size = sheet.cell(row=row, column=column).value
        if body_size == None:
            continue
        body_size = body_size.replace(",","")
        body_size = float(body_size)
        measurement_unit = sheet.cell(row=row, column=column+1).value
        abundance = float(sheet.cell(row=row, column=2).value)
        if datatype == "mass":
            if measurement_unit == "kg":
                body_size = body_size * 1000
            elif measurement_unit == "log10 grams":
                body_size = 10**body_size
            elif measurement_unit != "g":
                continue
        elif datatype == "length":
            if measurement_unit == "cm":
                body_size = body_size * 10
            elif measurement_unit == "m":
                body_size = body_size * 1000
            elif measurement_unit == "inch":
                body_size = body_size * 25.4
            elif measurement_unit != "mm":
                continue
        data = [body_size, abundance]
        species_sizes.append(data)
    sorted_species = sorted(species_sizes, key=lambda species: species[0])
    bottom_ten_percent = len(sorted_species) / 10
    ten_percent = []
    for num in range(0, len(sorted_species)):
        if num < bottom_ten_percent:
            ten_percent.append(sorted_species[num])
        else:
            break
    return ten_percent    

wb = openpyxl.load_workbook("tidy_lpi_data.xlsx")
sheet = wb.active
smallest_mass = find_the_smallest(3, "mass")
smallest_VT = find_the_smallest(5, "length")
smallest_CMO = find_the_smallest(7, "length")
print len(smallest_mass)
print stats.linregress(smallest_mass)
print len(smallest_VT)
print stats.linregress(smallest_VT)
print len(smallest_CMO)
print stats.linregress(smallest_CMO)