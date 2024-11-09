'''
enumerate is a built-in Python function that adds a counter to an iterable 
(such as a list, tuple, or string) and returns an enumerate object. 
This object produces tuples containing the index and value from the iterable.
'''

'''
Syntax:

enumerate(<iterable>, start=0)

iterable: The iterable object (e.g., list, tuple, string) to be enumerated.
start: An optional integer specifying the starting index (default is 0).
'''

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

sentence = 'Hello World!'
for index, char in enumerate(sentence):
    print(index, char)


'''
Use Cases:

Looping with indices:
    When you need to access both the index and value of each item in an iterable, 
    enumerate is a convenient and Pythonic way to do so.

Natural counting:
    Use enumerate with a custom start value to generate a natural counting 
    sequence (e.g., 1-based indexing).

Iterating over a string:
    enumerate can be used to iterate over a string, where the index represents 
    the character position and the value is the character itself.

Data processing:
    In data processing pipelines, enumerate can be used to iterate over a 
    sequence of data, applying transformations or filters based on the index and 
    value.

Reporting and logging:
    When generating reports or logs, enumerate can be used to associate indices 
    with specific values, making it easier to track and analyze data.
'''