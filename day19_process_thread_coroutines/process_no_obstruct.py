"""
非阻塞式:全部添加到队列中,立刻返回,并没有等待其他的进程执行完毕,但是回调函数是等待任务完成之后才调用
阻塞式:
"""
import os
import random
import time
from multiprocessing import Pool


# 非阻塞式进程

def task(task_name):
    print('开始做任务啦!', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random.random() * 2)
    end = time.time()
    # print('完成{} 任务用时:{}  进程id:{}'.format(task_name, (end - start), os.getpid()))
    return '完成{} 任务用时:{}  进程id:{}'.format(task_name, (end - start), os.getpid())


container = []


def callback_func(n):
    container.append(n)


if __name__ == '__main__':
    pool = Pool(5)

    tasks = ['听音乐', '吃饭', '洗衣服', '打麻将', '散步', '看孩子', '做饭']

    for task1 in tasks:
        pool.apply_async(task, args=(task1,), callback=callback_func)

    pool.close()  # 添加任务结束
    pool.join()  #

    print(container)
    print('over!!!!')
