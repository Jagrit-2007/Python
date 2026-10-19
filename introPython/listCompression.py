# list compressions

# create a new list sqList by squaring even numbers of list1

list1 = [29,48,0,93,5,62]

sqList = [n**2 for n in list1 if n % 2 == 0]

print(sqList)