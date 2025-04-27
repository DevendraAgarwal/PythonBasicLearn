'''
Python Generator Expressions

A generator expression is a concise way to create a generator object in Python. 
It is similar to a list comprehension, but instead of creating a list, it generates 
values “just in time” like a class-based iterator or generator function would.

Syntax
A generator expression uses parentheses () instead of square brackets [] like a 
list comprehension. The basic syntax is:

(expression for variable in iterable)
'''

# Python code to illustrate generator expression 
generator = (num ** 2 for num in range(10)) 
for num in generator:
    print(num)

string = 'Generator'
li = list(string[i] for i in range(len(string)-1, -1, -1))
print(li)