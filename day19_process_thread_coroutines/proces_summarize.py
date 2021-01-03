"""
process = Process(target=函数,name=进程名字,args=(给函数传递的参数))
process对象

对象调用方法
process.start() 启动进程并执行任务
process.run() 只是执行了任务但是没有启动进程
terminate() 终止
"""

# 进程创建
from multiprocessing import Process
from time import sleep

m = 1  # 不可变类型
list1 = []


def task1(second):
    while True:
        sleep(second)
        global m
        m += 1
        list1.append('task{}'.format(m))
        print('这是任务1.....', m, list1)


def task2(second):
    while True:
        global m
        sleep(second)
        m += 1
        list1.append('task{}'.format(m))
        print('这是任务2......', m, list1)


number = 1
if __name__ == '__main__':
    # 子进程
    p = Process(target=task1, name='任务1', args=(1,))
    p.start()
    print(p.name)
    p1 = Process(target=task2, name='任务2', args=(2,))
    p1.start()
    print(p1.name)

    while True:
        sleep(1)
        m += 1
        print('------>main', m)

    # while True:
    #     number += 1
    #     sleep(0.2)
    #     if number == 100:
    #         p.terminate()
    #         p1.terminate()
    #         break
    #     else:
    #         print(number)
