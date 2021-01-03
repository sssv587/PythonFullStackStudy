import threading

"""
线程是可以共享全局变量的
GIL 全局解释器锁
"""

ticket = 1000


def run1():
    global ticket
    for i in range(100):
        ticket -= 1


def run2():
    global ticket
    for i in range(100):
        ticket -= 1


if __name__ == '__main__':
    # 创建线程
    th1 = threading.Thread(target=run1, name='th1')
    th2 = threading.Thread(target=run1, name='th2')
    th3 = threading.Thread(target=run1, name='th3')
    th4 = threading.Thread(target=run1, name='th4')

    # 启动
    th1.start()
    th2.start()
    th3.start()
    th4.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()

    print('money=', ticket)
