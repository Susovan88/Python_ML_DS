'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.
'''

import multiprocessing
import time
import sys
import math

sys.set_int_max_str_digits(1000000)

def get_factorial(num):
    print(" compute factorial of ",num )
    result=math.factorial(num)
    print(" -> ",result)
    return result

if __name__=="__main__":

    nums=[2000,800,1000,6000,7000] 
    st_time=time.time()

    ## creat pool of worken processes
    with multiprocessing.Pool() as pool:
        result=pool.map(get_factorial,nums)
    
    finish_time=time.time()-st_time
    print("finised time - ",finish_time)


    
