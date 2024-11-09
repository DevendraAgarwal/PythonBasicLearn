'''
A generator in Python is a special type of function that returns an iterator,
allowing you to generate a sequence of values on-the-fly, without storing them 
all in memory at once. This makes generators particularly useful when working 
with large datasets or infinite sequences.
'''

def countdown(n):
    '''
    This countdown generator function takes an integer n as input and yields the 
    numbers from n down to 0, one at a time.
    '''
    while n > 0:
        yield n
        n -= 1

gen = countdown(5)
for num in gen:
    print(num)

gen = countdown(5)
print(next(gen))  # 5
print(next(gen))  # 4
print(next(gen))  # 3

'''
Use Cases

Lazy Evaluation:
    Generators allow you to compute values only when needed, reducing memory usage
    and improving performance.

Infinite Sequences:
    Generators are ideal for creating infinite sequences, such as generating 
    prime numbers or random numbers.

Large Datasets:
    Generators can process large datasets without loading the entire dataset 
    into memory at once.

Pipelining:
    Generators can be chained together to create complex data processing pipelines.

Cooperative Multitasking:
    Generators can be used to implement cooperative multitasking, where multiple 
    tasks yield control to each other.
'''

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for i in range(11):
    print(next(fib))