class AnimalFactory:
    def create_animal(self, species):
        if species == "dog":
            return Dog()
        elif species == "cat":
            return Cat()
        else:
            raise ValueError("Unknown species")

class Dog:
    pass

class Cat:
    pass

# Usage:
factory = AnimalFactory()
dog = factory.create_animal("dog")
print(isinstance(dog, Dog))  # True