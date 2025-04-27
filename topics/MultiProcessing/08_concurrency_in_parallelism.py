import multiprocessing
import threading
import time
import os

def thread_task(thread_id):
    print(f"    [Thread-{thread_id}] running inside Process-{os.getpid()}")
    time.sleep(5)
    print(f"    [Thread-{thread_id}] finished inside Process-{os.getpid()}")

def process_task(process_id):
    print(f"[Process-{process_id}] started with PID {os.getpid()}")

    threads = []
    for i in range(5):  # Each process spawns 5 threads
        t = threading.Thread(target=thread_task, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"[Process-{process_id}] finished with PID {os.getpid()}")

def main():
    processes = []
    for i in range(3):  # Spawn 3 processes
        p = multiprocessing.Process(target=process_task, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Main program finished.")

if __name__ == "__main__":
    main()


"""In this example, we create a main program that spawns multiple processes.
Creates 3 processes (using multiprocessing).
Each process creates 5 threads (using threading).
Each thread sleeps for 5 second to simulate work.
You will see true parallelism because:
Processes run in parallel → no GIL blocking across processes.
Threads inside a process run concurrently → they share memory.


Multiprocessing creates separate memory spaces, bypassing the GIL.
Threading inside a single process is limited by the GIL, but still shows concurrency for I/O-bound tasks (like sleep).
Concurrency under Parallelism:
Multiple threads (concurrent) are running inside multiple processes (parallel).
"""