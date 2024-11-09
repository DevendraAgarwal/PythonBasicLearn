'''
A class is a blueprint or a template that defines the characteristics and behavior
of an object. It’s a fundamental concept in object-oriented programming (OOP). 
A class defines a set of attributes (data) and methods (functions) that can be 
used to create objects, which are instances of the class.

Key Features of a Python Class:

Attributes:
    Class attributes are variables defined inside the class, 
    which are shared by all instances of the class. Instance attributes, 
    on the other hand, are variables defined inside instance methods, 
    which are unique to each instance.

Methods:
    Class methods are functions that are part of the class definition and 
    can be called on the class itself. Instance methods are functions that are 
    part of the instance and can be called on individual objects.

Constructor:
    The __init__ method is a special method that is called when an 
    instance of the class is created. It initializes the instance’s attributes.

Inheritance:
    Python supports inheritance, which allows a class to inherit 
    attributes and methods from another class.
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
circle = Circle(5)  # Create a Circle instance with radius 5
print(circle.area())