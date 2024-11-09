'''
try:
    code that may raise an exception
except ExceptionType:
    code to handle the exception
except ExceptionType2:
    code to handle the ExceptionType2
finally:
    clean up resources or perform final actions
    The finally block is optional and is executed regardless of whether an exception was raised or not. 
    It’s useful for cleaning up resources or performing final actions
'''

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    else:
        print(f"The result of {a} divided by {b} is: {result}")

divide_numbers(10, 2)
divide_numbers(10, 0)

'''
Exception Types
Python has several built-in exception types, including:

Exception: The base class for all exceptions.
TypeError: Raised when a type error occurs 
    (e.g., trying to add a string and an integer).
ValueError: Raised when a value error occurs 
    (e.g., trying to convert a non-numeric value to a number).
ZeroDivisionError: Raised when attempting to divide by zero.
RuntimeError: Raised when a runtime error occurs 
    (e.g., trying to access an undefined variable)
'''