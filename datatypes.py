# Datatypes in Python : 

# int for integers
# float for decimal values
# str for strings
# complex for complex numbers
# bool for boolean
# list for lists
# tuple for tuples
# range for ranges
# dict for dictionaries
# set for sets

a = 10 # int
b = "hello" # str 
c = 29.433 # float 
d = "93.3" # str

print(type(a), type(b), type(c), type(d))

print(type(d) == str) # True , cus datatype is str itself not as a string "str"
print(type(d) == "str") # False

# we can also use "isinstance" , like pass a arguement to check if , it is

print(isinstance(d, str)) # True
print(isinstance(a, int)) # True

# TYPECASTING : 
# Converting one datatype to other
# Strings can't be converted to int or float

num1 = 100
print(type(num1)) # int

num2 = float(num1)
print(type(num2)) # float

age = "20"
# checking whther age is int or not
print(isinstance(age, int)) # False

age = int(age)
print(isinstance(age, int)) # True


# ************************************************************



# abs : absolute value : always start from zero
print(abs(-5.5)) # 5.5

# round : rounds to nearest integer but also till we want
num1 = 10
num2 = 3
print(num1 / num2) # 3.333333333333333
print(round(num1/num2)) # 3
print(round(num1/num2, 2)) # 3.33