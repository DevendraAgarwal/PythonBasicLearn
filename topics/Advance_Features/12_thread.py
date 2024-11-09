'''
I/O-bound tasks, such as network requests or disk operations, where threads 
can efficiently utilize CPU cores.
'''

import threading
import time

def worker(name):
    print(f"{name} started")
    time.sleep(2)  # simulate I/O-bound task
    print(f"{name} finished")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()