# Dictionary : python dat structure 
# allows to create KEY-VALUE pairs

# Key can be any immutable value such as String, number or a tuple
# Values are mutuable, i.e they can be changed

Student1 = {
    "name" : "Alexx",
    "age" : 18
}
Student2 = {
    "name" : "Joness",
    "age" : 19
}

print(Student1) # {'name': 'Alexx', 'age': 18}

print(Student1["name"])
print(Student1["age"])

Student1["name"] = "Badmoshh!"

print(Student1) # {'name': 'Badmoshh!', 'age': 18}

# To get a speific element use "get" method

print(Student1.get("name")) # Badmosh!, because "name" is a key
print(Student1.get("color")) # None , because "color" is not any key.. So we use default value
print(Student1.get("color", "Black")) # Black

# We can delete a key by "pop" method

Student1.pop("name") # so it deletes the key and its value
print(Student1) # {'age': 18}

# checking if a key is present in the dictionary

print("age" in Student1) # True

# print all keys by "keys" method

print(Student2.keys()) # dict_keys(['name', 'age'])

# print all values of keys by "values" method

print(Student2.values()) # dict_values(['Joness', 19])

print(Student2.items())  # dict_items([('name', 'Joness'), ('age', 19)])
# Converting to list
print(list(Student2.items())) # [('name', 'Joness'), ('age', 19)]


# We can also add new key-value pair in dictionary

Student2["fav food"] = "paneerr"
print(Student2)  # {'name': 'Joness', 'age': 19, 'fav food': 'paneerr'}

# Delete a key value pair

del Student2["age"]
print(Student2) # {'name': 'Joness', 'fav food': 'paneerr'}