"""
共享数据:
如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。
同步:一个一个的完成，一个做完另一个才能进来
效率就会降低。

使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，对于那些需要每次只允许一个线程操作的数据，
可以将其操作放到acquire和release方法之间。

多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。
但是当线程需要共享数据时，可能存在数据不同步的问题。为了避免这种情况，引入了锁的概念。

lock = threading.Lock()

lock.acquire() 请求得到锁
......
lock.release() 释放锁

只要不释放其他的线程都无法进入运行状态

"""

import threading
from time import sleep

lock = threading.Lock()

list1 = [0] * 10


def task1():
    # 获取线程锁，如果已经上锁，则等待锁的释放
    # lock.acquire()  # 阻塞
    for i in range(len(list1)):
        list1[i] = 1
        sleep(0.5)
    # lock.release() # 释放锁


def task2():
    # lock.acquire()  # 阻塞
    for i in range(len(list1)):
        print('---->', list1[i])
        sleep(0.5)
    # lock.release() # 释放锁


if __name__ == '__main__':
    th1 = threading.Thread(target=task1, name='th1')
    th2 = threading.Thread(target=task2, name='th2')

    th2.start()
    th1.start()

    th2.join()
    th1.join()

    print(list1)
