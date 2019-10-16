import json
csvfile = open("name_csv.txt","r")
data = json.load(csvfile)

csvfileclose()

print(data['friends'][0])
