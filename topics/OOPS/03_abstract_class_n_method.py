'''
An abstract class is a class that cannot be instantiated directly and is intended
to be subclassed. It provides a blueprint for other classes to follow, ensuring a 
consistent interface and encouraging code reuse. Abstract classes are defined 
using the abc (Abstract Base Class) module.

Key Characteristics:

Cannot be instantiated:
    You cannot create an object directly from an abstract class.

Intended for subclassing:
    Abstract classes are meant to be inherited by other classes,
    which must provide concrete implementations for abstract methods.

Abstract methods:
    Methods declared in an abstract class without an implementation are called 
    abstract methods. Subclasses must override these methods
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Dog Sounds Woof!"

class Cat(Animal):
    def sound(self):
        return "Cat Sounds Meow!"

# Error: Cannot instantiate Animal directly
# animal = Animal()

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Woof!
print(cat.sound())  # Output: Meow!