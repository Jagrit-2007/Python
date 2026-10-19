# CLASSES are blueprints , means the structure and
# instances can be created from it called "OBJECTS"

# creating a "Pet" class
class Pet:
    # initializing , its called constructor
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def statments(self):
        print(f"this is a {self.species}, named : {self.name}")    

# creating an object instance
dog = Pet(name="buddy", species="Dog")

# accessing value
print(dog.name)

dog.statments()