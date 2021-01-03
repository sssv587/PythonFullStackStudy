"""
greenlet已经实现了协程，但是这个人工切换，有点麻烦
python还有一个比greenlet更强大的并且能够自动切换任务的模块'gevent'
其原理是当一个greenlet遇到IO(指的是input output输入输出
比如网络、文件操作等)操作时，比如访问网络，就自动切换到其他的greenlet，等到IO完成，
在适当的时候切换回来继续执行

由于IO操作非常耗时，经常使程序处于等到状态，有了gevent我们自动切换协程，
就保证总有greenlet在运行，而不是等待IO

"""

import time

import gevent
from gevent import monkey

monkey.patch_all()


def a():  # 任务a
    for i in range(5):
        print('A' + str(i))
        time.sleep(0.5)


def b():  # 任务b
    for i in range(5):
        print('B' + str(i))
        time.sleep(0.5)


def c():  # 任务b
    for i in range(5):
        print('C' + str(i))
        time.sleep(0.5)


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()

    print('--------------finish--------------')
