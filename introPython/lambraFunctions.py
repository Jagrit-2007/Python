# Lambda functions : these are tiny anonymous function, they have no name and
# have only 1 expression as there body
# defined using "lambda" keyword 

sol1 = lambda num : num * 2 

# here, lambda is keyword, num is argument, num * 2 is expression

# lambda can accept multiple inputs like :

sol2 = lambda a,b : a * b

print(sol1(2)) # 4 (2 * 2)
print(sol2(2,4)) # 8 (2 * 4)
