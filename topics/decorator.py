# Decorator : Add Extra Functionality in Existing Function

""" 
Decorator Use Function as a parameter and also return a function

@decorator_name
def function_name(param)
    pass
    
    
Decorator Structure

def <decorator_name>(func):
    def <wrapper_function_name>(*args, **kwargs):
        <Code Before Function Execution>
        return_value = func(*args, **kwargs)
        <Code After Function Execution>
        
        return return_value
    return <wrapper_function_name>

"""

def decorator_function(func):
    def wrapper(*args, **kwargs):
        
        print(f"{func.__name__} Function Called")
        print("Before Function Execution")
        
        return_value = func(*args, **kwargs)
        
        print("After Function Execution")
        
        return return_value
    return wrapper

@decorator_function
def custom_function(a: int, b: int):
    print("Inside a Function")
    return a+b

print(custom_function(5,9))

""" 
Usages of Decorator:

1. Logging
2. Auth and Validation

Whenever you want to extend or add New Functionality without modify the original function
"""
