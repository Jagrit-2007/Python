# FOR LOOPS ; range(start, end, increment)

values = [293,484,94,3,5,4,7,8,5,4,78,8]

for value in values:
    print(value)

for nums in range(1, 100): # 1 inclusive , 100 exclusive
    print(nums)  

for nums in range(0,101,5):
    print(nums)

# enumerate() returns index of value
for index, value in enumerate(values):
    print(index, value)

for num in values:
    if num == 5:
        break    # "continue" can be used too
    else:
        print(num)