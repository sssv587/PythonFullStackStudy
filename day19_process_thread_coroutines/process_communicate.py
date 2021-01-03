# 进程间通信

from multiprocessing import Queue, Process
from time import sleep

q = Queue(5)


# q.put('A')
# q.put('B')
# q.put('C')
# q.put('D')
# q.put('E')
# print(q.qsize())
# if not q.full():  # 判断队列是否已满  q.empty() 判断队列是否是空的
#     q.put('F', timeout=3)  # put() 如果queue满了则只能等待，除非有‘空地’ 则添加成功
# else:
#     print('队列已满!')
#
# # 获取队列的值
# print(q.get(timeout=2))
# print(q.get(timeout=2))
# print(q.get(timeout=2))
# print(q.get(timeout=2))
# print(q.get(timeout=2))


# q.put_nowait()

def download(q):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print('正在下载:', image)
        sleep(0.5)
        q.put(image)


def getfile(q):
    while True:
        try:
            file = q.get(timeout=5)
            print('{}保存成功!'.format(file))
        except Exception as s:
            print('保存完毕!')
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print('00000000000')
