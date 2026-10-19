# Global variable
age1 = 19

def fnc1():
    print(age1) # 19

fnc1()



def fnc2(age2):
    # Local variable
    age2 = 10
    print(age2)

age2 = 100
fnc2(age2) # 10