'''
class ChildClass(ParentClass):
    # additional attributes and methods
'''

'''
Key Concepts:

Parent Class:
    The class from which the child class inherits attributes and methods.
    Also known as the base class.

Child Class:
    The new class that inherits from the parent class. 
    Also known as the derived class or subclass.

Inheritance:
    The process of creating a child class from a parent class.

Method Overriding:
    When a child class provides a different implementation for a 
    method inherited from the parent class.

Method Overloading:
    Not supported in Python; instead, use optional arguments or 
    default values to achieve similar functionality.
'''

'''
Types of Inheritance:

Python supports multiple inheritance, where a child class can inherit from 
multiple parent classes. However, this can lead to complexity and ambiguity, 
so single inheritance is often preferred.

Single Inheritance: A child class inherits from a single parent class.

Multiple Inheritance: A child class inherits from multiple parent classes.
'''

class Vehicle:
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def start_engine(self):
        print("Starting engine...")

    def stop_engine(self):
        print("Stopping engine...")

class Car(Vehicle):
    def __init__(self, color, wheels, doors):
        super().__init__(color, wheels)  # Call Vehicle's __init__()
        self.doors = doors

    def honk_horn(self):
        print("Honking horn...")

# Create a Car object
my_car = Car("red", 4, 4)
print(my_car.color)  # Output: red
print(my_car.wheels)  # Output: 4
my_car.start_engine()  # Output: Starting engine...
my_car.honk_horn()  # Output: Honking horn...