"""
Python的queue模块中提供了同步的、线程安全的队列类，包括FIFO(先进先出)队列Queue，
LIFO(后入先出)队列LifeQueue，和优先级队列PriorityQueue。这些队列都实现了锁原语
(可以理解为原子操作，即要么不做，要么就做完)，能够在多线程中直接使用
可以使用队列来实现线程的同步

"""
import random
import threading
import time
from multiprocessing import Queue


def product(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put('生产者产生数据:%d' % num)
        print('生产者产生数据:%d' % num)
        time.sleep(1)
        i += 1
    q.put(None)
    # 完成任务
    q.task_done()


def comsume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('消费者获取到:%s' % item)
        time.sleep(4)
    # 完成任务
    q.task_done()


if __name__ == '__main__':
    q = Queue(10)
    arr = []

    # 创建生产者
    th = threading.Thread(target=product, args=(q,))
    th.start()

    # 创建消费者
    tc = threading.Thread(target=comsume, args=(q,))
    tc.start()

    th.join()
    tc.join()

    print('END')

"""
线程:Thread

1.创建线程
    A. t = Thread(target=func,name='',args=(),kwargs=())   新建状态
       t.start()  -----> 就绪状态
       
       run()
       join()
       
    B.自定义线程
        class MyThread(Thread):
            def __init__(self,name):
                super().__init__()
                self.name = name
            def run(self):
                任务
    t = MyThread()
    t.start()

2.数据共享
    进程共享与线程共享区别:
        进程是每个进程中都有一份
        线程是共用一个数据  ----> 数据安全性问题
    
    GIL ----> 伪线程
    
    lock = Lock()
    lock.acquire()
    ....
    lock.release()
    
    ------> 只要用锁:死锁
    避免死锁

3.线程间通信:生产者与消费者
    生产者:线程
    消费者:消费者
    import Queue
    queue = Queue()     
    
    q = Queue(10)
    arr = []

    # 创建生产者
    th = threading.Thread(target=product, args=(q,))
    th.start()

    # 创建消费者
    tc = threading.Thread(target=comsume, args=(q,))
    tc.start()
    
    q.put()
    q.get()
    
扩展:GIL
"""