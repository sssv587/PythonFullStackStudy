# 闭包的作用
# 闭包：

"""
1.保存返回闭包时的状态(外层函数状态)


闭包有什么缺点呢？
闭包的缺点1：作用域没有那么直观
闭包的缺点2：因为变量不会被垃圾回收所有有一定的内存占用问题

闭包作用：
1.可以使用同级的作用域
2.读取其他元素的内部变量
3.延长作用域

闭包总结
1.闭包优化了变量，原本需要类对象完成的工作，闭包也可以完成
2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
3.闭包的好处，使代码简洁，便于阅读代码
4.闭包使理解装饰器的基础

"""


def func():
    a = 100

    def inner_func1():
        b = 90
        s = a + b
        print(s)

    def inner_func2():  # define
        inner_func1()  # 调用inner_func1
        print('------> inner_func2', a)
        return 'hello'

    return inner_func2


# 调用func
f = func()
print(f)
ff = f()  # inner_func2()
print(ff)
