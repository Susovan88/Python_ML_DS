#### multitrading with tread pool 

"""
#### ✅ What is ThreadPoolExecutor?
It's part of Python’s concurrent.futures module.
It helps you run multiple functions (tasks) in parallel using threads.
You don’t need to manually create and manage threads. It manages a pool of worker threads for you.

⚡ Why use ThreadPoolExecutor?
✅ When you have multiple tasks that don’t depend on each other, and you want to run them simultaneously instead of one-by-one.
✅ Great for I/O-bound operations like:
Waiting for API responses.
Reading/writing files.
Database queries.
Downloading files.
✅ It saves time because while one thread is waiting (e.g., for an API), another thread can continue working.

max_workers=2 means 2 threads will run tasks in parallel.
 submit() schedules a function to run with its arguments.
 executor.map() applies square() to each item in numbers in parallel and returns the results in the same order

"""

from concurrent.futures import ThreadPoolExecutor
import time

def print_num(num):
    time.sleep(2)
    return f"Number is - {num} "

nums=[1,2,3,4,5,6,7,89,123,]

st_time=time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_num,nums)

for val in results:
    print(val)

end_time=time.time()

print("total time takes - ",{end_time-st_time})