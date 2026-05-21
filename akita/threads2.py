from threading import Thread, Lock
import array as arr
import ctypes
import time
import timeit

numbers = arr.array('H');

def func1(my_lock):
    my_lock.acquire()
    for i in range(5):
        numbers.append(i * 10)
    my_lock.release()


def func2(my_lock):
    my_lock.acquire()
    for i in range(5, 10):
        numbers.append(i * 10)
        time.sleep(0.05)
    my_lock.release()

my_lock = Lock()


print("O tempo de func1: ",timeit.timeit((lambda: Thread(target=func1, args=(my_lock,)).start()), number=1))
print("O tempo de func2: ",timeit.timeit(lambda: Thread(target=func2, args=(my_lock,)).start(), number=1))