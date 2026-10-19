# Exception handling 

# ZeroDivisionError

try:
    res = 2 / 0
except ZeroDivisionError:
    print("CANNOT divide by zero")
# finally block always get execute
finally:
    res = 1

print(res)         