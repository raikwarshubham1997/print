# We can convert Json object to Python dictionary
# firsly I've read data of name_csv.txt then with the help of some operation    # is an object into Javascrip / and (in python is called dictionary) "name_csv.txt"

# store with the help of python dictionary

import json

# I've still created a Empty list
json_list = []

file = open("name_csv.txt","r")

for line in file.readlines():
    name,age,gender,email,contact = line.strip().split(',')
    # create a variables
    informations = {
        'name' : name,
        'age' : age,
        'gender' : gender,
        'email' : email,
        'contact' : contact,
        }
    json.append(informatins)

file.close()

# Now we have write information'name_json.txt'

my_file = open("name_json.txt","w")
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

json.dump(json_list,my_file)
