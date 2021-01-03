import sys

"""
__del__:
    1.对象赋值
        p = Person()
        p1 = p
        说明:p和p1共同指向同一个地址

    2.删除地址的引用
        del p1 删除p1对该地址的引用

    3.查看地址的引用的次数
        import sys
        sys.getrefcount(p)

    4.当一块空间没有了任何引用，默认执行__del__
        ref = 0
"""


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('------del------')


p = Person('jack')
p1 = p
p2 = p

p1.name = 'tom'
print(p.name)
print(p2.name)

del p2
print(p.name)

del p1
print(p.name)

# del p
print(sys.getrefcount(p))

# 对象赋值
n = 5
n1 = n
print(n1)
