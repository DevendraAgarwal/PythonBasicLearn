# ------------------------------getattr------------------------------------
'''
Retrieve the value of an object's attribute.

Syntax: getattr(object, attribute_name, default_value)
'''
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
name = getattr(person, "name")  # Returns "Alice"
age = getattr(person, "age", 30)  # Returns 30, because "age" doesn't exist

print(name, age)

# ------------------------------setattr------------------------------------
'''
Set the value of an object's attribute.

Syntax: setattr(object, attribute_name, value)
'''

class PersonTwo:
    def __init__(self, name):
        self.name = name

person = PersonTwo("Alice")
setattr(person, "name", "Bob")  # Changes the name attribute to "Bob"
setattr(person, "age", 25)  # Adds a new attribute "age" with the value 25

print(person.name, person.age)

# ------------------------------zip--------------------------------------
'''
Combines elements from two or more iterables (e.g., lists) into tuples.
Each tuple contains elements from the corresponding positions in the input 
iterables.
'''

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

combined = zip(names, scores)
print(list(combined))  # Output: [('Alice', 85), ('Bob', 90), ('Charlie', 78)]

# ------------------------------any--------------------------------------
'''
Returns True if at least one element in the iterable is True. Returns False 
if all elements are False or if the iterable is empty.
'''

values = [0, None, False, 5]
result = any(values)
print(result)  # Output: True

# ------------------------------all--------------------------------------
'''
Returns True if all elements in the iterable are True. Returns False if 
any element is False or if the iterable is empty.
'''

values = [1, 2, 3, 4]
result = all(values)
print(result)  # Output: True

values = [1, 0, 3]
result = all(values)
print(result)  # Output: False


# ------------------------------eval-------------------------------------
'''
Evaluates a string expression and returns the result. 
It's used to execute dynamic Python expressions.
'''

expression = "3 * 4 + 5"
result = eval(expression)
print(result)  # Output: 17

# ------------------------------assert-----------------------------------
'''
Tests if a condition is True. If it is not True, 
it raises an AssertionError with an optional message.
'''

x = 5
assert x > 0, "x should be greater than 0"  # No error

y = -1
# Raises AssertionError: y should be greater than 0
# assert y > 0, "y should be greater than 0"