g = (x * 3 for x in range(10))

while True:
    try:
        e = next(g)
        print(e)
    except StopIteration as e:
        print('没有更多元素')
        break

# 定义生成器的方式二:借助函数完成
# 只要函数中出现了yield关键字，说明函数就不是函数，变成生成器啦

# 斐波那契数列
"""
步骤：
1.定义一个函数，函数中使用yield关键字
2.调用函数，接收调用结果
3.得到的结果就是生成器
4.借助于next() __next__()得到元素
"""


def func():
    n = 0
    while True:
        n += 1
        yield n  # return n  + yield(暂停)


# g = func()
# print(g)
#
# print(next(g))
# print(next(g))


# 0,1,1,2,3,5,8,13,21
def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b
        a, b = b, a + b
        n += 1
    return '没有更多元素了' # return就是在得到StopIteration后的信息


g = fib(8)
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))