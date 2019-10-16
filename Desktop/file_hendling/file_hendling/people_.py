#"""In python, we use csv.reader() module to read the csv file. Here,
# we will show you how to read different types of csv files with different
# delimiter like quotes(""), pipe(|) and comma(,)"""
##We have a csv file called people.csv having default delimiter comma(,) with following data:
import csv

with open("people.csv","r") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)

csvFile.close()
# with whitespace output
print("*************************************************")

import csv

file = open("people.csv","r")
data = file.read()
file.close()
print(data)
