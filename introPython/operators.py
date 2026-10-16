# Operators : Arthemetic Operators , 
# logical operators, 
# relational operators, 
# boolean operators
# identity operator (is)
# membership operator (in)
# ternary operator

a = 10
b = 3

print(a + b, # addition
      a - b, # subtraction
      a * b, # multiplication
      a / b, # division
      a % b, # modulus : remainder
      a // b, # Floor division : rounds to nearest integer
      a ** b) # exponent : a to the power b

# "+" can also be used to add up two or multiple strings
print("hello " + "! how are you?")

# Assignment operators : += , -=, *=, /=
age = 9
age += 11 # age = age + 11 , so age = 9 + 11
print(age) # 20

# Relational operators
m = 10; n = 9
print(m >= n)
print(m < n)
print(m == n) # "==" checks if both values are equal
print(m != n) # "!=" checks if both values are NOT equal

# Boolean operators : "not" , "and", "or"
# not makes things opposite
# and checks both conditin, any 1 False make it False, for True both values MUST be True
# or checks both condiion, any 1 True makes it True

# True is also represented by 1 and False by 0
# Truthy statments : any number EXCEPT 0
# False statements : any string except being empty

cndt1 = True
cndt2 = False

print(not cndt1) # False
print(not cndt2) # True
print(cndt1 and cndt2) # False
print(cndt1 or cndt2) # True

# ternary operator
age = 19
c = "You are an adult!" if age > 18 else "You are NOT an adult!"
print(c)