# 登录校验
import time


def decorator(func):
    def wrapper(*args, **kwargs):
        print("正在启动校验")
        time.sleep(2)
        print('校验完毕')
        # 调用原函数 args ---> 元祖()
        func(*args, **kwargs)

    return wrapper


@decorator
def f1(n):
    print('-------f1--------', n)


f1(5)


@decorator
def f2(name, age):
    print('-------f2--------', name, age)


f2('lucy', 20)


@decorator
def f3(students, clasz='1908'):
    for stu in students:
        print(stu, clasz)


f3(['张三', '李四'], 'sssya')


@decorator
def f4():
    print('-------f4--------')

f4()