'''
for variable in iterable:
    <code to be executed>
'''

'''
Key Features

Iteration:
    The for loop iterates over the elements of the iterable object.

Variable assignment:
    Each iteration assigns the next element of the iterable to the variable specified.

Body of the loop:
    The code inside the loop is executed for each iteration.

Advanced Topics

Looping over multiple iterables:
    Use the zip() function to iterate over multiple sequences simultaneously.

Looping with conditions:
    Use if statements or conditional expressions within the 
    loop body to control iteration.

Breaking out of the loop:
    Use the break statement to exit the loop prematurely.
'''

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Iterating over a string
word = 'hello'
for char in word:
    print(char)

#  Iterating over a range
for i in range(5):
    print(i)