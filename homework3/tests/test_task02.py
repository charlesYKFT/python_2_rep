import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework3/')
import time
from tasks.task02 import slow_calculate
import multiprocessing
import pytest



def test_slow_calculate():
    """Checks if the slow_calculation function returns the correct result within less than 1 minute."""
    start_time = time.time()
    with multiprocessing.Pool(processes=61) as pool:
        results = pool.imap(slow_calculate, range(501))
        total_sum = sum(results)
    end_time = time.time()
    total_time = end_time-start_time
    assert total_time < 60, "The code execution too longer than 1 minute."
    assert total_sum == 1025932


if __name__ == '__main__':
    pytest.main()

"""The final code execution takes around 20.63 seconds."""

"""
                                                      Additional info
A 'short' story how I did this task.Correctly to say, me and two my partners: my classmate (Human) and ChatGPT (Bot).
First of all I chucked this assignment into ChatGPT. He told me an answer, but this solution took 83 seconds to finish. So I was upset and dropped this idea. Next day I tried to use ChatGPT again and he gave me another solution. This solution was shorter, but time was the same: 83 seconds. I was angry, so I wrote this Bot to speed up my solution. We had a long chat... He gave me different solutions (even changing slow_function). But all solutions didin't work. He replaced map() function at 14 line with imap(). He also started to add processes till the command (multiprocessing.cpu_count)  at 13 line. I was mad, I wanted to tell this Bot everything I think about AI for programming. In the end my classmate recommended me to write my own number of processes. I started to write numbers of degree 2. At the 64 he raised and error that it is too much for my laptop. I decreased this number to 61 and it worked. It gave a result in less than 20 seconds!
The next problem was to write a test. First I started to write a program, which executes all code from other file. It was so stupid that I am sorry even for an attempt to do this. Later my classmate told me to write all multiprocessing things in test_file. I did it, but it didn't worked.
After an hour of "correcting (cursing everything in the world)" I have found two errors:
1. Instead of assert total_time == ... I did assert total_sum == ...
2. I forgot to write if __name__ == '__main__' and my test didn't even executed.
Finally, after 2.5 hours I had solved it and had written test to it.
ChatGPT is great when you know programming. It can save you some time on writing typical construction (usually you have to correct it a little). But he can't help you if you don't know Python. Anyway I will continue using it :)

You may ask why I wrote all this stuff. I dont't know, really. Think of it as a written report on this completed assignment. I'll be glad if this report makes you a little happier in these not-so-easy times. And sorry for my English mistakes because I wrote it myself.
                                                                                                Anurev D.V, 20.31
"""
