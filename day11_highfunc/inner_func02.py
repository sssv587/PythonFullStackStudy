a = 100  # 全局变量
print(globals())


def func():
    b = 99

    def inner_func():
        nonlocal b
        global a
        c = 88
        # 尝试修改
        c += 12
        b += 1
        a += 1
        print(id(a), id(b), id(c))

    inner_func()
    # 使用locals()内置函数进行查看，可以看到在当前函数中声明的内容有哪些
    # locals()是一个字典。key:value
    print(locals())


# 调用函数
func()
