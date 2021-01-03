# 地址引用
a = 10  # 声明整形变量
b = a


def test():  # 声明函数
    print('-----test-------')


t = test


# print(id(t), id(test))

def func(f):
    print(f)  # <function test at 0x0000017DAD973C18>
    f()
    print('------>func')


# 调用
# func(test)

"""
装饰器 :cvar
特点：
1.函数A是作为参数出现的，(函数B就接收函数A作为参数)
2.要有闭包的特点
"""


# 定义一个装饰器
def decortor(func):
    a = 100
    print('wrapper外层打印测试')

    def wrapper():
        func()
        print('刷漆')
        print('铺地板')

    print('wrapper加载完成....')
    return wrapper


# 使用装饰器
@decortor
def house():
    print("我是毛坯房")


'''
:cvar
1.house被装饰参数
2.将被装饰函数作为参数传给装饰器decorator
3.执行了decorator函数
4.将返回值又赋值给house

'''

# def house1():
#     house()
#     print('刷漆')
#     print('铺地板')


# 调用函数  house()  <---------> decorator(house)()
print(house)
