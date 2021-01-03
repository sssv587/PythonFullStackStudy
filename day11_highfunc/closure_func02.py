# 闭包


def func(a, b):
    c = 10

    def inner_func():
        s = a + b + c
        print('相加之后的结果是:', s)

    return inner_func


# 调用func
# fun = func(6, 9)
# fun1 = func(60, 9)
# print(globals())
# fun()
# fun1()

# 计数器
def generate_count():
    container = [0]

    def add_one():
        container[0] += 1
        print('当前是第{}次访问'.format(container[0]))

    return add_one


# 内部函数就是一个计数器
generate_count()()
generate_count()()
generate_count()()
