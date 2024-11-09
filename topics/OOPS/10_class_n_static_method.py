'''
A class method in Python is a method that is bound to the class and not the 
instance of the class. It is defined using the @classmethod decorator and takes 
cls as its first parameter, which refers to the class itself.

Key Characteristics:

Bound to the class:
    Class methods are associated with the class, not instances of the class.

cls parameter:
    The first parameter of a class method is cls, which refers to the class itself.

Access class state:
    Class methods can access and modify class-level attributes and variables.

Can be used as alternative constructors:
    Class methods can be used to create new instances of the class.
'''

class MyClass:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1

    def __init__(self):
        self.instance_var = 0

obj1 = MyClass()
obj2 = MyClass()

obj1.increment_count()  # also increments class-level count
print(MyClass.count)  # prints 1

MyClass.increment_count()  # increments class-level count
print(MyClass.count)  # prints 3

obj1.increment_count()  # also increments class-level count
print(MyClass.count)  # prints 3


'''
Static Methods in Python

A static method in Python is a method that is not bound to the class or instance 
and does not have access to any instance or class state. It is defined using 
the @staticmethod decorator and takes no special parameters.

Key Characteristics:

Not bound to the class or instance:
    Static methods are standalone functions within the class namespace.

No self or cls parameter:
    Static methods do not receive any implicit parameters.

No access to instance or class state:
    Static methods cannot access or modify instance or class-level attributes.

Utility functions:
    Static methods are often used for utility functions that are related to the 
    class but do not depend on instance or class state.
'''

class MyClass:
    @staticmethod
    def add(x, y):
        return x + y

result = MyClass.add(2, 3)  # returns 5
print(result)

'''
When to Use Each:

Class Methods:
    Use when you need to access or modify class-level attributes,
    or when you need to create alternative constructors.

Static Methods:
    Use when you have a utility function that does not depend on instance or
    class state and is related to the class.

Remember, class methods are bound to the class and can access class state,while 
static methods are standalone functions with no access to instance or class state
'''