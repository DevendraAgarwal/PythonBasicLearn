'''
NonLocal Statement

The nonlocal statement in Python serves as a bridge between nested functions,
allowing an inner function to access and modify a variable from its enclosing 
scope.
'''

def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
    inner()
    print("outer:", x)
outer()  # Output: outer: 2