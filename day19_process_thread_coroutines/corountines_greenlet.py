# greenlet 完成协程任务
import time

from greenlet import greenlet


def a():  # 任务a
    for i in range(5):
        print('A' + str(i))
        gb.switch()
        time.sleep(0.5)


def b():  # 任务b
    for i in range(5):
        print('B' + str(i))
        gc.switch()
        time.sleep(0.5)


def c():  # 任务b
    for i in range(5):
        print('C' + str(i))
        ga.switch()
        time.sleep(0.5)


if __name__ == '__main__':
    ga = greenlet(a)
    gb = greenlet(b)
    gc = greenlet(c)

    ga.switch()
