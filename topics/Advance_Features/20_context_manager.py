'''
A Context Manager is an object that defines the runtime context for a block of 
code. It’s a mechanism in Python that allows you to manage resources, such as 
files, database connections, or network sockets, in a way that ensures they are 
properly initialized and cleaned up, regardless of whether the code block 
completes normally or raises an exception.

A Context Manager is typically implemented as a class that defines two special 
methods: __enter__() and __exit__().

__enter__() is called when the context manager is entered (i.e., when the with 
    statement is executed). It initializes the resource and returns it.

__exit__() is called when the context manager is exited (i.e., when the with 
    block is completed or an exception occurs). It cleans up the resource.
'''

'''
Use of Context Managers

Context Managers have several benefits:

Resource Management: They ensure that resources are properly initialized and 
    cleaned up, preventing resource leaks and making your code more robust.

Error Handling: If an exception occurs within the with block, the __exit__() 
    method is called, allowing you to handle the error and release resources.

Code Readability: Context Managers simplify your code by encapsulating resource 
    management and error handling, making it easier to understand and maintain.

Flexibility: You can use Context Managers with various types of resources, 
    such as files, databases, network sockets, and more.

Common use cases for Context Managers include:

File operations: Opening and closing files, ensuring they are properly closed 
    even if an exception occurs.

Database connections: Establishing and closing database connections, handling 
    errors and releasing resources.

Network sockets: Managing network connections, ensuring they are properly closed 
    and released.

Subprocesses: Running subprocesses and ensuring they are properly terminated 
    and cleaned up.
'''

# ------------------Class Based Context Manager--------------

class FileContextManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileContextManager('example.txt') as f:
    f.write('Hello, world!')

# ------------------Decorator Based Context Manager--------------

import contextlib

@contextlib.contextmanager
def file_context_manager(filename):
    file = open(filename, 'w')
    try:
        yield file
    finally:
        file.close()

with file_context_manager('example.txt') as f:
    f.write('Hello, world!')