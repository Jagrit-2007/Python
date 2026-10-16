# Sets are not ordered BUT store unique values ONLY, SETS cannot be added

# Immutuable sets are called frozen sets , Just like
# Immutable lists are called tuples

set1 = {"meow", "bhauu", "hehehe"}
set2 = {"bhauu", "FAHH"}

# Intersecting two sets

intersect = set1 & set2
print(intersect) # {'bhauu'}

# Union of two stes

union = set1 | set2
print(union) # {'meow', 'bhauu', 'FAHH', 'hehehe'}

# Difference of two sets

diff = set1 - set2 # set1 me se minus kiye hai
print(diff) # {'hehehe', 'meow'}

# SETS CANNOT BE ADDED

# add = set1 + set2
# print(print)

# SUBSET & SUPERSET by > and <