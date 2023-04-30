"""
Here's a not very efficient calculation function that calculates something important::

    import time
    import struct
    import random
    import hashlib

    def slow_calculate(value):
        '''Some weird voodoo magic calculations'''
        time.sleep(random.randint(1,3))
        data = hashlib.md5(str(value).encode()).digest()
        return sum(struct.unpack('<' + 'B' * len(data), data))

Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""

import struct
import hashlib
import multiprocessing
import time
import random


def slow_calculate(value):
    '''Some weird voodoo magic calculations'''
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))

# This code was added just to show the fastest time to run this code.


if __name__ == '__main__':
    start_time = time.time()
    with multiprocessing.Pool(processes=61) as pool:
        results = pool.imap(slow_calculate, range(501))
        total_sum = sum(results)
    end_time = time.time()
    total_time = end_time-start_time
    print("Total sum: ", total_sum)
    print("Calculation time: ", end_time - start_time, " seconds")
