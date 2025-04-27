'''
Iterator: 
An iterator is an object that allows you to iterate over a sequence (such as a 
list, tuple, or string) and access its elements one at a time. It implements the 
iterator protocol, which consists of two methods: __iter__() and __next__(). 
The __iter__() method returns the iterator object itself, while the __next__() 
method returns the next element in the sequence.

Generator: 
A generator is a special type of iterator that can be used to generate a sequence 
of values on the fly, rather than computing them all at once and storing them in 
memory. It is implemented using a function that contains the yield keyword, which 
allows it to produce a series of values over time, rather than computing them all 
at once and returning them in a list, for example.

Key differences:

Implementation: 
    An iterator is typically implemented using a class, while a generator is 
    implemented using a function.

Usage: 
    An iterator is used to iterate over an existing sequence, while a generator 
    is used to generate a sequence of values on the fly.

Memory usage: 
    An iterator typically requires more memory than a generator, since it 
    needs to store the entire sequence in memory. A generator, on the other hand, 
    only needs to store the current state of the sequence, making it more 
    memory-efficient.

Yield statement: 
    A generator uses the yield statement to produce a series of values, 
    while an iterator does not use this statement.
'''

# Iterator example
class MyIterator:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# Generator example
def my_generator(max):
    for i in range(max):
        yield i

# Usage
my_iterator = MyIterator(5)
for num in my_iterator:
    print(num)

my_gen = my_generator(5)
for num in my_gen:
    print(num)