# 局部和全局
# 全局变量如果是不可变在函数中进行修改需要添加global，如果全局变量是可变的，则在函数中修改的时候就不需要添加global

name = '月月'

list1 = [1, 2, 4, 6]


def func():
    name = 'adad'
    print(name)
    print(list1)


def func1():
    global name
    print(name)
    name += '真漂亮！'

    # 修改列表
    list1.append(100)
    print(list1)


def func2():
    name1 = 'lucy'
    name1 += 'hhhh'

    print(name1)  # 自己的

    global name
    print(name)


# func1()
# func()
func2()
