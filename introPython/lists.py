# lists are data structures in python
# in pyton list can store different data types also!

list1 = ["dogs", 1, "cats", "meoww"]

print(list1[0]) # dogs
print(list1[-1]) # meoww
print(list1) # ['dogs', 1, 'cats', 'meoww']

print("dogs" in list1) # True
print(2 in list1) # False

emptyList = [] # empty list

print(list1[1:3]) #[1, 'cats']
print(len(list1), len(emptyList)) # 4 0





# ***********************************************************************





# Add values in list by : .append()
list1.append("Bhauuu")
list1.append(000)
list1.append(9)
list1.append("nums")
print(len(list1)) # 8
print(list1) # ['dogs', 1, 'cats', 'meoww', 'Bhauuu', 0, 9, 'nums']

# Combine 2 lists together by : .extend()

list1.extend(["list2 Start", "yoyoo", "random"])
print(len(list1)) # 11
print(list1) # ['dogs', 1, 'cats', 'meoww', 'Bhauuu', 0, 9, 'nums', 'list2 Start', 'yoyoo', 'random']

# Alternative of .extend() is "+="

list1 += ["yaaya alternative", "+="]
print(len(list1)) # 13
print(list1) # ['dogs', 1, 'cats', 'meoww', 'Bhauuu', 0, 9, 'nums', 'list2 Start', 'yoyoo', 'random', 'yaaya alternative', '+=']

list1 += "abcd" # will be added as a character, since string is collection of characters
print(len(list1)) # 17
print(list1) # ['dogs', 1, 'cats', 'meoww', 'Bhauuu', 0, 9, 'nums', 'list2 Start', 'yoyoo', 'random', 'yaaya alternative', '+=', 'a', 'b', 'c', 'd']

# changing value of specfic element

list1[2] = "Value interchanged"
print(list1) #['dogs', 1, 'cats', 'meoww', 'Bhauuu', 0, 9, 'nums', 'list2 Start', 'yoyoo', 'random', 'yaaya alternative', '+=', 'a', 'b', 'c', 'd']
# Remove a value by : .remove(value)

list1.remove("Value interchanged")
print(len(list1)) # 16


# Removing and returning the last element of list by : .pop()

val1 = list1.pop()
print(val1) # d
print(len(list1)) # 15

# Inserting a value at specific postition by : .insert(index, value)

print(len(list1)) # 15
list1.insert(1, "Inserted Value")
print(len(list1)) # 16
print(list1) # ['dogs', 'Inserted Value', 1, 'meoww', 'Bhauuu', 0, 9, 'nums', 'list2 Start', 'yoyoo', 'random', 'yaaya alternative', '+=', 'a', 'b', 'c']

# Changing the sliced list

list1[0:1] = ["DOGS", "DOGSSSSS"]
print(len(list1)) # 17
print(list1) # ['DOGS', 'DOGSSSSS', 'Inserted Value', 1, 'meoww', 'Bhauuu', 0, 9, 'nums', 'list2 Start', 'yoyoo', 'random', 'yaaya alternative', '+=', 'a', 'b', 'c']


# WE CAN ALSO SORT THE LIST, BUT LIST SHOULD THEN HAVE SIMILAR DATATYPES VALUES ONLY
# Sorting modfied original content

# Uppercase to lowercase order
strValues = ["urhcwEElo1", "UEUUllo2", "EI3lo3", "MZNlo4", "Blahho5"]

# copied list
strValuesCOPY = strValues[:]

strValues.sort()

print(strValuesCOPY)
print(strValues)

# Ascending order
intValues = [24,5782,994,0,93,-37,48,-4,-383,32]
intValues.sort()
print(intValues)


# SORTING WITHOUT modifing the Original list by : .sorted()

# sorted in a global function and we can pass two parameters there
newList = [923,494,4,-49,0,4,4,-41,34]

print(newList)

# Ascending
print(sorted(newList))

# Descending
print(sorted(newList, reverse=True))

# Absolute values
print(sorted(newList, key=abs))

