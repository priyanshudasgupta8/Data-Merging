import csv
from os import stat_result

bright_stars = []
dwarf_stars = []

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        bright_stars.append(row)

with open("dwarf_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dwarf_stars.append(row)

headers_1 = bright_stars[0]
bright_stars_data = bright_stars[1:]

headers_2 = dwarf_stars[0]
dwarf_stars_data = dwarf_stars[1:]

for data_point in bright_stars_data:
    data_point[2] = data_point[2].lower()

for data_point in dwarf_stars_data:
    data_point[2] = data_point[2].lower()

headers = bright_stars_data + dwarf_stars_data
stars_data = []
for index, data_row in enumerate(bright_stars_data):
    stars_data.append(bright_stars_data[index] + dwarf_stars_data[index])

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)
