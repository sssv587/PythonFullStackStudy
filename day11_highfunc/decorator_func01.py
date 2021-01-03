# 装饰器

"""
加入购物车，付款，修改收货地址。。。。
判断用户的登录状态，

"""


def func(number):
    a = 100

    def inner_func():
        nonlocal a, number
        number += 1
        for i in range(number):
            a += i
        print('修改后的a:', a)

    return inner_func


# 调用func
f = func(5)
f()

# 函数作为参数
a = 50
f1 = func(a)  # a是一个实参
print(f1)