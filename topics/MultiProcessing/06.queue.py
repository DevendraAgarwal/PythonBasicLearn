"""
Question: What Is Queue?

Answer:
    The Queue module provides thread-safe FIFO queues, which are ideal for implementing producer-consumer patterns.

Question: Why Use Queue?

Answer: 
    The Queue module is used for inter-thread communication and synchronization. It allows multiple threads to safely 
    exchange data without the need for explicit locks or semaphores.
    
    This is particularly useful in multi-threaded applications where threads need to share data or coordinate their actions.
    The Queue module provides a simple and efficient way to manage data exchange between threads, 
    making it easier to build concurrent applications.
    It is also useful for implementing producer-consumer patterns, where one or more threads produce data and 
    one or more threads consume it.
    The Queue module provides a thread-safe FIFO queue, which allows multiple threads to safely 
    add and remove items from the queue without the need for explicit locks or semaphores.
    This makes it easier to build concurrent applications that need to share data or coordinate their actions.

Question: What Are the Benefits of Using Queue?
Answer:
    The Queue module provides several benefits for inter-thread communication and synchronization:
    1. Thread-Safe: The Queue module is designed to be thread-safe, meaning that multiple threads can safely add and remove items from the queue without causing data corruption
    2. Built-in Synchronization: Handles all necessary locking internally, simplifying code and reducing the risk of errors
"""

import queue
import time

q = queue.Queue()

# Producer thread
def producer(q, count):
    for i in range(count):
        item = f"item-{i}"
        q.put(item) # Add item to the queue
        print(f"Produced {item}")
        time.sleep(1)
    q.put(None)  # Sentinel value to indicate completion

# Consumer thread
def consumer(q):
    while True:
        item = q.get() # Remove item from the queue
        if item is None:
            break
        print(f"Consumed {item}")
        q.task_done()   # Mark the task as done

"""
the producer thread adds items to the queue, and the consumer thread processes them. 
The sentinel value None signals the consumer to exit.
"""