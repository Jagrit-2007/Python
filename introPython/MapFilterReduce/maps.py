numbers = [2,5,6]

def double(a):
    return a * 2

# mapping each item of numbers to double function by "map"
result = map(double, numbers)

print(result) # <map object at 0x733f782b2300>
print(list(result)) # [4, 10, 12]


# SINCE it was a one liner function we can use LAMBDA FUNCTION

res = map(lambda x : x * 2, numbers)

print(list(res)) # [4, 10, 12]