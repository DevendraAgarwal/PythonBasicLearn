import threading
import queue
import time

class TaskManager:
    """
    A thread-safe task manager that uses a queue to manage tasks and a semaphore to limit the number of concurrent workers.
    The RLock is used to ensure that the processing of tasks is thread-safe, allowing for re-entrant locking.
    """
    def __init__(self, max_workers):
        self.task_queue = queue.Queue()
        self.semaphore = threading.Semaphore(max_workers)
        self.lock = threading.RLock()
        self.workers = []
        self.shutdown_flag = threading.Event()

    def start_workers(self, num_workers):
        for i in range(num_workers):
            worker = threading.Thread(target=self.worker, name=f"Worker-{i}")
            worker.start()
            self.workers.append(worker)

    def add_task(self, task):
        self.task_queue.put(task)

    def worker(self):
        while not self.shutdown_flag.is_set():
            try:
                task = self.task_queue.get(timeout=1)
                with self.semaphore:
                    self.process_task(task)
                self.task_queue.task_done()
            except queue.Empty:
                continue

    def process_task(self, task):
        with self.lock:
            print(f"{threading.current_thread().name} processing {task}")
            time.sleep(0.5)
            print(f"{threading.current_thread().name} completed {task}")

    def stop_workers(self):
        self.shutdown_flag.set()
        for worker in self.workers:
            worker.join()
        print("All workers have been stopped.")

# Example usage
if __name__ == "__main__":
    task_manager = TaskManager(max_workers=3)
    task_manager.start_workers(num_workers=5)

    for i in range(10):
        task_manager.add_task(f"Task-{i}")

    task_manager.task_queue.join()  # Wait for all tasks to be completed
    task_manager.stop_workers()


# In this example, we create a TaskManager class that manages a pool of worker threads.
"""
The TaskManager uses a queue to hold tasks and a semaphore to limit the number of concurrent workers.

The RLock is used to ensure that the processing of tasks is thread-safe, allowing 
for re-entrant locking.
The shutdown flag is used to signal the workers to stop when all tasks are completed.
This implementation allows for a flexible and efficient way to manage tasks in a 
multi-threaded environment.
The TaskManager can be easily extended to include additional features, such as 
task prioritization or error handling.

This example demonstrates how to create a thread-safe task manager using the Queue module,
Semaphore, and RLock in Python.
"""

"""
RLock: Ensures that the process_task method can be safely re-entered by the same thread if needed.
Semaphore: Limits the number of concurrent tasks being processed to max_workers.
Queue: Manages the tasks to be processed in a thread-safe manner.
Event: Signals worker threads to shut down gracefully.

When to Use Each Primitive:
- RLock: Use when a thread needs to acquire the same lock multiple times without blocking itself.
- Semaphore: Use when you want to limit the number of threads that can access a resource at the same time.
- Queue: Use when you need a thread-safe way to manage tasks or data between threads.
- Event: Use when you need to signal between threads, such as for shutdown or completion notifications.

Thread Coordination: Combining these primitives allows for robust and efficient multithreaded applications.
"""