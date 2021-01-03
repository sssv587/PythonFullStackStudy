# 阻塞式进程
import os
import random
import time
from multiprocessing import Pool

"""
    特点:
    添加一个任务执行一个任务，如果一个任务不结束另一个任务就进不来。
    
    进程池：
    pool = Pool(max)  创建进程池对象
    pool.apply()  阻塞式
    pool.apply_async()  非阻塞式
    
    pool.close()
    pool.join()  让主进程让步
"""


def task(task_name):
    print('开始做任务啦!', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random.random() * 2)
    end = time.time()
    # print('完成{} 任务用时:{}  进程id:{}'.format(task_name, (end - start), os.getpid()))
    print('完成{} 任务用时:{}  进程id:{}'.format(task_name, (end - start), os.getpid()))


if __name__ == '__main__':
    pool = Pool(5)

    tasks = ['听音乐', '吃饭', '洗衣服', '打麻将', '散步', '看孩子', '做饭']

    for task1 in tasks:
        pool.apply(task, args=(task1,))

    pool.close()  # 添加任务结束
    pool.join()  #

    print('over!!!!')
