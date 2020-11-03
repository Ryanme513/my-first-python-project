# A dictionary is a unordered set of key: value pairs
names = ["alex", "john", "ryan"]

names_and_heights = {
    "tyler": 5,
    "jacky": 5,
    "ryan": 3
}

print(names_and_height["jacky"])

names_and_heights = {
    "tyler": {"feet": 5, "inches": 11},
    "jacky": {"feet": 6, "inches": 5},
    "ryan": {"feet": 3, "inches": 11}
}

print(str(names_and_heights["tyler"]["feet"]) + "' " + str

prices = {}

prices["oatmeal"] == 3 #oatmeal is the key and 3 is the value 

names_and_heights["ryan"]["feet"] = 7 #updating an existing key

names_and_heights["ramiro"] = {"feet": 5, "inches": 3} #adding a new key: value pair(you can only add one pair)

names_and_heights.update({
    "angelo": {"feet": 0, "inches": 0}, 
    "allistar": {"feet"}: 0, "inches": 0
    }) #adding new key:value pairs (you can add multiple using update)

print(names_and_heights)

for value in names_and_heights:
    print(value) #prints out all the values in the dictionary

for key in names_and_heights:
    print(key) #prints out all the keys in the dictionary