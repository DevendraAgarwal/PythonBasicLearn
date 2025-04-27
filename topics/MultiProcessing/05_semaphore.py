"""
Question: What Is Semaphore?

Answer: 
    A Semaphore manages access to a resource by multiple threads. It maintains a counter 
    representing the number of threads that can access the resource simultaneously.

Question: Why Use Semaphore?

Answer: 
    It is useful for controlling access to a limited number of resources, such as database connections 
    or network sockets. Semaphores can be used to limit the number of threads that can access a resource 
    at the same time, preventing resource exhaustion and ensuring fair access.

Resource Limiting:
    Controls access to a finite number of resources (e.g., limiting the number of concurrent database connections).
Thread Coordination:
    Ensures that only a specified number of threads can perform a particular operation at the same time.
"""

import threading
import time

class LimitedResource:
    """
    A simple example of using a semaphore to limit access to a resource.
    This class demonstrates how to use a semaphore to control access to a shared resource.
    """
    def __init__(self, max_connections):
        self.semaphore = threading.Semaphore(max_connections)

    def access(self, thread_id):
        with self.semaphore:
            print(f"Thread {thread_id} accessing resource")
            time.sleep(1)
            print(f"Thread {thread_id} releasing resource")
            # The semaphore is automatically released when the with block is exited
            # No need to explicitly release the semaphore
            # self.semaphore.release()  # Not needed, handled by the context manager

"""
the LimitedResource class uses a semaphore to limit the number of threads that can access the access method concurrently.
"""
