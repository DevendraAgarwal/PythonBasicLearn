'''
Dictionary comprehension is a concise way to create dictionaries in Python. 
It allows you to transform one dictionary into another by applying a 
transformation function to each key-value pair. The syntax is similar to list 
comprehensions, but instead of creating a list, it creates a dictionary.
'''

'''
Syntax:

<key_expression>: <value_expression> for <item> in <iterable>
'''

numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

'''
Use Cases

Data Transformation: 
    Convert a list of numbers to a dictionary where keys are the numbers and 
    values are their squares.

Filtering: 
    Create a dictionary with only specific key-value pairs from a larger dictionary.

Conditional Dictionary Creation:
    Create a dictionary only if a certain condition is met.

Grouping:
    Group a list of items by a common attribute and create a dictionary 
    with the grouped items.

Flattening: 
    Convert a nested dictionary to a flat dictionary.
'''