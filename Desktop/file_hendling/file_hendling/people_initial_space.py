## CSV files with Initial Spaces
import csv

csv.register_dialect('myDialect',delimiter = ',', skipinitialspace = True)

# by default "skipinitialspace" is False but in our situation we have to make it True.

with open("people.csv", "r") as  csvFile:
    reader = csv.reader(csvFile, dialect = 'myDialect')
    for row in reader:
        print(row)

csvFile.close()
# without whitespace output
