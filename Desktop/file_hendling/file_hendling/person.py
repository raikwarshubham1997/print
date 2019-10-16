# ask the user for a list of three friend
# for each friend, we'll tell the user whether they are nearby
# for each nearby friend, we'll save there  name 'person_nearby.csv'
import csv

friends = input("Enter your three friends names, separated by commas (no space, please): ")

my_file = open("person_friends.csv","r")
person_nearby = [line.strip() for line in my_file.readlines()]

my_file.close()

friends_set = set(friends)
person_nearby_set = set(person_nearby)

friends_nearby_set = friends_set.intersection(person_nearby_set)

nearby_friends_file = open("person_nearby.csv","w")

for friend in friends_nearby_set:
    print(f"{friend} is nearby! meet up with them")
    nearby_friends_file.write(f"{friend}\n")

nearby_friends_file.close()
