""" 
Static Variables

Python does not have traditional static variables like C++ or Java.
However, you can achieve similar behavior using class variables or instance 
variables with some creative workarounds. 
Here are a few approaches:

Class Variables:
    You can define a class variable and access it through the class itself or 
    its instances. Class variables are shared by all instances of the class.

Instance Variables with a Twist:
    You can use instance variables and initialize them lazily using a decorator
    or a factory function. This approach allows you to create a “static” variable
    per instance.

Namespace-based Solution:
    You can use a dictionary or a namespace to store “static” variables and
    access them through a factory function or a decorator.
"""

# Class Variables

class Counter:
    count = 0

    def increment(self):
        Counter.count += 1
        return Counter.count

c1 = Counter()
c2 = Counter()

print(c1.increment())  # Counter.count = 1
print(c2.increment())  # Counter.count = 2

# Instance Variables with a Twist

def lazy_static(func):
    def wrapper(self):
        if not hasattr(self, '_static_var'):
            setattr(self, '_static_var', func())
        return getattr(self, '_static_var')
    return wrapper

class CounterTwo:
    def __init__(self):
        self._static_var = None

    @lazy_static
    def get_count(self):
        return 0

c1 = CounterTwo()
c2 = CounterTwo()

print(c1.get_count())  # 0
print(c2.get_count())  # 0

# Namespace-based Solution

_counter_ns = {}

def static_var(name, default):
    if name not in _counter_ns:
        _counter_ns[name] = default
    return _counter_ns[name]

class CounterThree:
    def __init__(self):
        self.count = static_var('count', 0)

c1 = CounterThree()
c2 = CounterThree()

print(c1.count)  # 0
print(c2.count)  # 0