# Enums are readable names that are bound to constant values
# Enums are used to create constants

from enum import Enum

# 2 variables created State.INACTIVE and State.ACTIVE = 1
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.INACTIVE) # State.INACTIVE
print(State.INACTIVE.value) # 0

print(State(1)) # State.ACTIVE

print(len(State)) # 2