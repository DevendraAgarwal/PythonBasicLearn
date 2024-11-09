'''
Static Functions

Python does not have traditional static functions like C++ or Java. However,
you can achieve similar behavior using:

Class Methods:
    You can define a class method, which is a method that is bound to the class rather than an 
    instance of the class.

Functions with a Class Reference:
    You can define a regular function and pass a class reference as an argument to create a 
    “static” function.
'''

# Class Methods

class Counter:
    count = 0
    @classmethod
    def increment(cls):
        cls.count += 1
        print(cls.count)

Counter.increment()  # Counter.count = 1

# Functions with a Class Reference

def static_func(cls):
    cls.count += 1
    return cls.count

class CounterTwo:
    count = 1

print(static_func(CounterTwo))  # Counter.count = 2