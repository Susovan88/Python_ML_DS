import time
import multiprocessing

def print_square():
    for i in range(1, 6):
        print(f"Square Number: {i**2}")
        time.sleep(1)

def print_cube():
    for i in range(1, 6):
        print(f"Cube Number: {i**3}")
        time.sleep(1.5)

"""
✅ Why do we use if __name__ == "__main__":?
To make sure certain code only runs when the file is executed directly, not when it’s imported.

"""
if __name__ == "__main__":

    st = time.time()

    # create two processes
    p1 = multiprocessing.Process(target=print_square)
    p2 = multiprocessing.Process(target=print_cube)

    # start multiprocessing
    p1.start()
    p2.start()

    # wait for both processes to finish
    p1.join()
    p2.join()

    end_time = time.time() - st
    print("finished time - ", end_time)
