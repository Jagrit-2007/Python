# Functions are created by "def" keyword
# Parameters are the values accepted by FUNCTION defintion
# Arguments are the values we pass to function when we call it
# Argument can have default value



# ***************************************************************


# name = input("What's your name? ")
# age = int(input("What's your age? "))

# def student(name = "random", age = 1):
#     print(f"Hey {name}, Congratulations on being {age} years old!")

# student(name, age)
# student()

# ****************************************************************

def names(index):
    Names = ["alex", "jonex", "meoww"]
    Names[index] = "Changed"
    return Names

res = names(0)
print(res)