'''
The Method Resolution Order (MRO) defines the order in which a method or attribute
is searched for in a class hierarchy. This is particularly important when dealing
with multiple inheritance, where a class inherits from multiple parent classes.

How MRO works?

Depth-First Left-to-Right (DFLR) Python 2: 
    Python uses a depth-first left-to-right (DFLR) algorithm to resolve methods.
    This means that it searches for a method in the current class, then in its 
    immediate parent class, and so on, until it reaches the root of the inheritance
    tree.

C3 Lineariation Python 3:
    The MRO is also known as the linearization of a class, which is a list of 
    classes in the order they are searched. This list is used to resolve method 
    calls.
'''

class A:
    def printSomething(self):
        print("In class A")

class B:
    def printSomething(self):
        print("In class B")

class C(A, B):
    pass

c = C()
c.printSomething()  # Output: In class A