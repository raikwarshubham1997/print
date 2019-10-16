import csv
with open("maths_csv.csv","r") as file:
    content = file.read()

##for row in content:
##    print(row[0:1])
##    for col in content():
##        total += int(col)
##print(total)
file.close()
##

with open("maths_csv2.csv") as fin:
    headerline = fin.write(fin)
    total = 0
for row in csv.reader(fin):
    total += int(row[1])
for row in csv.reader(fin):
    print(col) # for troubleshooting
    
    for col in row[1]:
      total += int(col)
print(total)
        
