# 装饰器带参数
"""
:cvar
带参数的装饰器是三层的
最外层的函数负责接收装饰器参数
里面的内容还是原装饰器的内容
"""


def outer(a):  # 第一层：负责接收装饰器的参数
    def decorator(func):  # 第二层：负责接收函数
        def wrapper(*args, **kwargs):  # 第三层：负责接收函数的参数
            func(*args, **kwargs)
            print('----->铺地板{}'.format(a))

        return wrapper  # 返回出来的是：第三层

    return decorator  # 返回出来的是：第二层


@outer(10)
def house(time):
    print('我{}日期拿到的房子钥匙，是毛坯房...'.format(time))


@outer(100)
def street():
    print('新修了街道名字是：黑泉路')


house('2019-6-12')
street()
