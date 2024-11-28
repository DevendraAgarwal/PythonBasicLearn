'''
Monkey patching in Python refers to the dynamic modification of a class or module
at runtime. This allows you to change or extend the behavior of libraries or 
classes without modifying the original source code.

However, there are specific scenarios where monkey patching might be necessary
advantageous:
Third-Party Libraries: 
    When working with third-party libraries where you don’t have control over 
    the source code, you can’t modify or extend the classes directly. 
    Monkey patching provides a way to tweak or extend the functionality without 
    altering the original library code.

Drawbacks of Monkey Patching:
Maintenance: 
    It can make code harder to understand and maintain, especially for 
    developers unfamiliar with the patches.
Debugging:
    Issues introduced by monkey patches can be difficult to trace.
Compatibility:
    Future updates to the library or framework might conflict with your patches.
'''

class MyClass:
    def greet(self):
        return "Hello, World!"
obj = MyClass()
print(obj.greet())  # Output: Hello, World!

def new_greet(self):
    return "Hello, Monkey Patch!"

# Apply monkey patch
MyClass.greet = new_greet
print(obj.greet())  # Output: Hello, Monkey Patch!