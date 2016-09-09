import openpyxl
import csv

read_wb = openpyxl.load_workbook(
    "Living Planet Index-07-04-2016.xlsx")
LPI_sheet = read_wb.active
species_info = {}

def find_species_size_info(file_name, species_name, size_type):
    with open(file_name, "rb") as f:
        reader = csv.reader(f)
        species_info.setdefault(species_name, {})
        species_info[species_name].setdefault(size_type, None)
        species_info[species_name].setdefault(size_type + " Measurement", None)
        for eol_row in reader:
            test_species_name = eol_row[1].decode('utf-8')
            if test_species_name == species_name:
                species_info[species_name][size_type] = eol_row[4]
                species_info[species_name][size_type + " Measurement"] = eol_row[7]
                break
               

for row in range(2, 401):
    species_name = LPI_sheet.cell(row=row, column=2).value    
    find_species_size_info("eol_download_2379.csv", species_name, "Mass")
    find_species_size_info("eol_download_2416.csv", species_name, "Body Length VT")
    find_species_size_info("eol_download_2419.csv", species_name, "Body Length CMO")
    print(species_name)

print species_info
write_wb = openpyxl.Workbook()
sheet = write_wb.active
columns = ["Mass", "Mass Measurement", "Body Length VT", 
    "Body Length VT Measurement", "Body Length CMO", "Body Length CMO Measurement"]
sheet['A1'] = "Species Name"
column_number = 2
for column in columns:
   sheet.cell(row=1, column=column_number).value = column
   column_number +=1
row_number = 2
for species in species_info:
    print species + "making workbook"
    sheet.cell(row=row_number, column=1).value = species
    for num in range(2, 8):
        column_header = columns[num - 2]
        sheet.cell(row=row_number, column=num).value = species_info[species][column_header]
    row_number += 1 
write_wb.save("tidy_lpi_data.xlsx")    