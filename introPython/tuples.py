# Tuples : unlike lists , TUPLES CANNOT BE MODIFIED
# created by ()

# sorted() and sort() doesnot work on tuples because it CANT be modified (original*)

names = ("Alex", "jones", "dogss")

print(names[0]) # Alex
print(names.index("Alex")) # returns index , 0
print(names.count("Alex")) # 1