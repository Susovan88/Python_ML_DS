### using multitrading
import time
import threading

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)

# Create two threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

st=time.time()

# Start both threads
t1.start()
t2.start()

## Wait for both threads to finish
t1.join()
t2.join()

finish_time=time.time()-st
print("finised time - ",finish_time)

