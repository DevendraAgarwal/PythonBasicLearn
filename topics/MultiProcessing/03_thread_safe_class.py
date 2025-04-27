import threading

# Thread-safe class example
# In Python, a thread-safe class is one that can be safely used by multiple threads at the same time without causing data corruption or inconsistent state.
# This is typically achieved by using synchronization mechanisms such as locks, semaphores, or other concurrency primitives
# to control access to shared resources.

class ThreadSafeCounter:
    '''
    This class demonstrates how to create a thread-safe class in Python
    using threading locks to ensure that only one thread can modify the state of the class at a time.
    This is important in multi-threaded applications to prevent race conditions and ensure data integrity.
    The class below implements a simple counter that can be incremented and decremented in a thread-safe manner.
    The `ThreadSafeCounter` class uses a lock to ensure that only one thread can modify the counter at a time.
    '''
    def __init__(self, initial=0):
        self._value = initial
        self._lock = threading.Lock()  # Lock object to control access

    def increment(self):
        with self._lock:  # Lock is acquired before proceeding
            self._value += 1
            return self._value

    def decrement(self):
        with self._lock:  # Lock is acquired before proceeding
            self._value -= 1
            return self._value

    def get_value(self):
        with self._lock:  # Reading is also protected
            return self._value

'''
What Makes It Thread Safe?

The threading.Lock() object is used to control access.
Before reading or writing the shared variable self._value, we acquire the lock (with self._lock).
When one thread is inside the with block, other threads are blocked until the lock is released.
This ensures one thread at a time can modify or read the counter.
'''

'''
Feature | Description
----------------|------------------------------------------------
threading.Lock | Ensures mutual exclusion — only one thread accesses at a time.
with statement | Automatically acquires and releases the lock, even if an exception occurs inside.
Safe for Read/Write | Even read operations (get_value) are protected, to avoid stale data.
'''

# Example usage
# Create a thread-safe counter
counter = ThreadSafeCounter()

def worker():
    for _ in range(100):
        counter.increment()

threads = []

# Create 5 threads
for _ in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("Final Counter Value:", counter.get_value()) 
# Output: Final Counter Value: 500
# The final counter value should be 500, as each of the 5 threads increments the counter 100 times.
# In this example, the `ThreadSafeCounter` class uses a lock to ensure that only one thread can modify the counter at a time.

'''
How it Helps to Maintain Threads Easily

Avoids Race Conditions: Threads don’t overwrite each other's changes.
Predictable Behavior: Your program becomes reliable and easier to debug.
No Manual Lock/Unlock Needed: Using with ensures the lock is correctly handled even if exceptions occur.
Scales Well: You can increase the number of threads without worrying about synchronization manually.
'''