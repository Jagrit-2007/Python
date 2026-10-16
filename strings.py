# strings in python are collection of characters enclosed in quotes
# string indexing start from 0

name = "Jagrit"
name += " is my name!"
print(name)

# print("""""") : this is multi-line string

print("""
yoo bro
this is
multi line

Comment
""")


# ************************************************************************


# Built-in string methods : they DONOT alter exisiting stringsss

# 1. isalpha() : checks if string contains only characters AND is NOT empty
# 2. isalnum() : checks if string contains characters OR digits AND is NOT empty
# 3. isnumeric() : checks if string contains all numeric digits
# 4. lower() : converts all chars to lowercase
# 5. upper() : converts all chars to uppercase
# 6. title() : converts first char to uppercase
# 7. replace() : to replace a part of String
# 8. split() : to split a string on specific character seprator
# 9. strip() : to trim whitspace from string
# 10. join() : to append new characters to string
# 11. find() : to find position of substring
# 12. startswith() : checks whether string start with specific substring
# 13. endswith() : checks whether string ends with specific substring
# 14. len(string) : to check string length

greetings1 = "hello"
greetings2 = "MEOWWW"

print(greetings1.upper()) # Converts all characters to UPPERCASE
print(greetings2.lower()) # COnverts all characters to LOWERCASE
print(greetings1.title()) # Converts first letter to uppercase
print(greetings1.islower()) # Checks whether every character is lowercase or NOT
print(greetings1.isupper()) # checks if every character is uppercase or NOT
print(len(greetings1)) # checks length of string

# string indexing start from 0

name1 = "hello world" # 0 to 10 index , so 0 index is 1st char and 10th index is 11th char
print(name1[0])
print(len(name1))
# print(name1[11]) IndexError: string index out of range
print(name1[10]) # last index
print(name1[-1]) # last index can also be represnted by : -1

# Slicing : string[start:end] , start is inclusive BUT end is exclusive
print(name1[1:7]) # ello w

print(name1[1:]) # will go to end of the string, ello world
