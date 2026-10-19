# Everything in python is Object like integers, strings, tuples, dictionaries & so on

# Objects have attributes & methods and are accessed by "."


# Checking memory address of the object

age = 19
print(id(age)) # 11370672

age = 199
print(id(age)) # 11376432 , different

age = 19
print(id(age)) # 11370672

# so every time value changes it creates a new object at new adress
# hence proving integers are IMMUTABLE