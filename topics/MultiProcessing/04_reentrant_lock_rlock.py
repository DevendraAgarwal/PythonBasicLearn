"""
Question: What Is RLock?

Answer: 
    An RLock (Reentrant Lock) is a synchronization primitive in Python's threading module that allows
    a thread to acquire the same lock multiple times without blocking itself. It is a type of lock 
    that can be acquired by the same thread multiple times, allowing for reentrant behavior.

    It is useful in scenarios where a thread needs to acquire a lock that it already holds, 
    such as in recursive functions or nested method calls.
    It is a subclass of the Lock class and provides the same interface as a regular lock, 
    but with additional functionality to support reentrancy.
    It is important to note that while an RLock allows a thread to acquire the same lock multiple 
    times, it must be released the same number of times before it is fully released.
    It is a thread-safe mechanism that ensures that only one thread can access a shared resource 
    at a time,

    An RLock (Reentrant Lock) allows a thread to acquire the same lock multiple times. 
    This is particularly useful when a thread needs to re-enter a critical section it already holds 
    the lock for, such as when recursive functions or nested methods require synchronization.

------------------------------

Question: Why Use RLock?

Answer: 
    Using an RLock (Reentrant Lock) in Python's threading module provides several advantages:

    1. Reentrancy: RLock allows the same thread to acquire the lock multiple times without blocking itself.
    2. Deadlock Prevention: It prevents deadlocks that can occur when a thread tries to acquire a lock it already holds.
    3. Nested Locking: It allows for nested function calls to safely acquire the same lock.
    4. Thread Safety: It ensures that shared resources are accessed in a thread-safe manner, even in complex scenarios.
    5. Performance: In some cases, using an RLock can improve performance by reducing contention between threads.
    6. Flexibility: It provides more flexibility in designing multi-threaded applications, especially when dealing with 
        recursive algorithms or complex locking scenarios.
    7. Simplicity: It simplifies the code by allowing the same lock to be used in different parts of the code without 
        worrying about deadlocks.
    8. Readability: It makes the code more readable and maintainable by clearly indicating that a lock can be 
        acquired multiple times by the same thread.
    9. Compatibility: It is compatible with existing threading libraries and can be easily integrated into existing codebases.
    10. Debugging: It can help in debugging multi-threaded applications by providing a clear indication of 
        which thread holds the lock and how many times it has been acquired.
"""

import threading

class ReentrantExample:
    """
    A simple example of using RLock in Python.
    This class demonstrates how to use RLock to allow a thread to acquire the same 
    lock multiple times.
    """
    def __init__(self):
        self.lock = threading.RLock()

    def outer(self):
        with self.lock:
            print("Entered outer method")
            self.inner()

    def inner(self):
        with self.lock:
            print("Entered inner method")

"""
the outer method acquires the lock and then calls inner, which also attempts to acquire the 
same lock. With RLock, this is safe and won't cause a deadlock.
"""