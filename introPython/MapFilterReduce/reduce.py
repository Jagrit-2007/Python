# reduce() is used by importing "functools" library

from functools import reduce


# WITHOUT REDUCE : calculating expense of day

expense1 = [
    ('Dinner', 80),
    ('Car repair', 80)
]

sum1 = 0
for expense in expense1:
    sum1 += expense[1]

print(sum1)    

# WITH REDUCE

expense2 = [
    ('Dinner', 180),
    ('Car repair', 980),
    ('coffee', 98)
]

# reduce(function, iterable, initializer)

sum2 = reduce(lambda a, b: a + b[1], expense2, 0)

print(sum2)