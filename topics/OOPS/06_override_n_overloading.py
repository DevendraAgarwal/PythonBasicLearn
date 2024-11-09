'''
Overloading:

Python does not support traditional method overloading like some other languages 
(e.g., Java, C++). In Python, you cannot define multiple methods with the same 
name but different parameters within the same class.

However, you can achieve similar behavior using the following techniques:

Default arguments:
    You can define a single method with default arguments, allowing it to accept 
    different numbers of parameters.

Variable-length arguments:
    You can use the *args and **kwargs syntax to define a method that can accept 
    a variable number of positional and keyword arguments.

Dynamic method dispatch:
    You can use a dictionary or a metaclass to dynamically create methods at 
    runtime, allowing you to simulate method overloading.
'''

class Calculator:
    def calculate(self, x, y=None):
        if y is None:
            return x  # single argument, returns x
        return x + y  # two arguments, returns their sum

calc = Calculator()
print(calc.calculate(5))  # returns 5
print(calc.calculate(5, 3))  # returns 8

'''
Method Overriding

Method overriding in Python occurs when a subclass provides a specific 
implementation of a method that is already defined in its parent class. 
The subclass method must have the same name, parameters, and return type as 
the parent class method.
'''

class Animal:
    def sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog Sounds Woof!")

my_dog = Dog()
my_dog.sound()  # Output: Woof!