"""
🧠 What is ProcessPoolExecutor?
ProcessPoolExecutor is part of Python’s concurrent.futures module.

It lets you run multiple tasks in parallel, but each task runs in a separate process.

It uses the multiprocessing module internally.

Think of it like this:
📦 You have a pool of workers (processes).
⚡ Each worker runs on a different CPU core, so tasks can execute truly in parallel.

⚡ Why use ProcessPoolExecutor?
✅ It allows you to use multiple CPU cores to speed up CPU-intensive tasks.

Examples:
✔ Complex math (factorials, matrix multiplications).
✔ Data processing on large datasets.
✔ Image or video processing.

🕑 When to use ProcessPoolExecutor?
Use it if:
✅ Your program spends most time doing calculations.
✅ You want real parallelism (not just concurrency).
✅ Your task is CPU-bound, not waiting for input/output.

Don’t use it for I/O-bound tasks—it’s overkill.

"""

from concurrent.futures import ProcessPoolExecutor
import time

def square_num(num):
    time.sleep(2)
    return f" square is - {num**2}"

if __name__=="__main__":

    nums=[2,4,5,8,9,12,34,98,67]

    st_time=time.time()

    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_num,nums)

    for i in results:
        print(i)

    end_time=time.time()
    print("total time takes - ",{end_time-st_time})

    """

🧠 Why do we need if __name__ == "__main__": for multiprocessing?
When you use multiprocessing, Python creates new processes by importing your script as a module.

If you don’t protect the entry point with:

python
Copy code
if __name__ == "__main__":
then every new process will execute the entire script again, leading to infinite process creation (or crashing your program).
   
     """