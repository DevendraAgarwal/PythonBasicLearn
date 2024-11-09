'''
CPU-bound tasks, such as scientific computing or data processing, 
where multiple processes can utilize multiple CPU cores.
'''

import multiprocessing
import time

def worker(num):
    print(f"Process {num} started")
    time.sleep(2)  # simulate CPU-bound task
    print(f"Process {num} finished")

if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()