'''
A meta class is a class whose instances are classes. In other words,
a meta class is a class that creates classes. It’s a class that defines the 
behavior of another class, often referred to as a “class factory”. 
Meta classes are used to customize or extend the behavior of class creation, 
allowing you to modify or replace the default class creation process.

Key Concepts

Class:
    A class is a blueprint or a template for creating objects.

Meta Class:
    A meta class is a class whose instances are classes.

Instance:
    An instance is an object created from a class.


How Meta Classes Work?

When you define a class in Python, you can specify a meta class using the 
metaclass keyword argument. The meta class is responsible for creating the class 
and its attributes. 
Here’s a high-level overview of the process:

1. The meta class is initialized with the class name, base classes, and dictionary 
    of attributes (methods and variables).
2. The meta class calls its __new__ method, which returns a new class object.
3. The new class object is then used to create instances of the class.
'''

class AddAttributeMeta(type):
    def __new__(meta, name, bases, namespace):
        namespace['custom_attr'] = 'Hello, World!'
        return type.__new__(meta, name, bases, namespace)

class MyClass(metaclass=AddAttributeMeta):
    pass

print(MyClass.custom_attr)  # Output: Hello, World!
print(type(MyClass))

'''
In this example, AddAttributeMeta is a meta class that adds a custom_attr 
attribute to every class it creates. When we define MyClass with 
metaclass=AddAttributeMeta, it inherits the custom attribute from the meta class.
'''

'''
Use Cases

Meta classes are useful in various scenarios:

Domain-Specific Languages (DSLs):
    Implementing a DSL in Python by creating a meta class that translates 
    custom syntax into Python syntax.

Class Customization:
    Modifying or extending the behavior of class creation, such as adding 
    attributes or methods to every class.

AOP (Aspect-Oriented Programming):
    Implementing aspects (cross-cutting concerns) that can be applied to 
    multiple classes without modifying their code.

Dynamic Class Generation:
    Creating classes dynamically at runtime, such as generating classes for 
    serialization or deserialization.


Best Practices

Use meta classes sparingly:
    Meta classes can introduce complexity and make code harder to understand. 
    Use them only when necessary.

Keep meta classes simple:
    Avoid complex logic in meta classes to maintain readability and maintainability.

Document meta classes:
    Clearly document the purpose and behavior of meta classes to ensure 
    understanding and maintainability.


Conclusion
Meta classes are a powerful tool in Python that allow you to customize and extend 
the behavior of class creation. While they can be complex and introduce additional
complexity, they can also be used to create elegant and maintainable solutions 
for specific problems. When used judiciously, meta classes can be a valuable 
addition to your Python programming toolkit.
'''