numbers = [94,403,95,35,4,44,0,90]

result = filter(lambda x : x % 2 == 0, numbers)

print(list(result))