'''
I/O-bound tasks, such as network requests or database queries, 
where coroutines can efficiently utilize a single thread.
'''

import asyncio

async def worker(name):
    print(f"{name} started")
    await asyncio.sleep(2)  # simulate I/O-bound task
    print(f"{name} finished")

async def main():
    tasks = []
    for i in range(5):
        task = asyncio.create_task(worker(f"Task-{i}"))
        tasks.append(task)
    await asyncio.gather(*tasks)

asyncio.run(main())

'''
Conclusion

Thread:
    Suitable for I/O-bound tasks, but still subject to GIL limitations.

MultiProcessing:
    Ideal for CPU-bound tasks, but has higher creation overhead.

AsyncIO:
    Efficient for I/O-bound tasks, with low creation overhead and no GIL limitations.
'''

'''
Comparison:

	                | Thread	           |MultiProcessing	    |AsyncIO
Concurrency Model   | Lightweight threads  |Separate processes  |Coroutines (single-threaded)
Use Case	        | I/O-bound tasks	   |CPU-bound tasks	    |I/O-bound tasks
GIL	                | No(*) 	           |No	                |No
Creation Overhead	| Low	               |High	            |Low
'''