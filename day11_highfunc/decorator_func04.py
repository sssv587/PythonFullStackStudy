# 装饰器
"""
:cvar
如果装饰器是多层的，谁距离函数最近就优先使用多个哪个装饰器

"""


def zhuang1(func):
    print('------->1')

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('刷漆')

    print('------>2')
    return wrapper


def zhuang2(func):
    print('------->1')

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('铺地板')

    print('------>2')
    return wrapper


@zhuang1
@zhuang2
def house():
    print('我是毛坯房......')


house()
