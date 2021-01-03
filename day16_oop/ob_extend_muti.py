# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print('------->eat1')
#
#     def eat(self, food):
#         print('------->eat{}'.format(food))
#
#
# p = Person('sss')
# p.eat('狮子头')
import inspect


class Base(object):
    def test(self):
        print('------Base------')


class A(Base):
    def test(self):
        print('------>AAA')


class B(Base):
    def test1(self):
        print('------>BBB')


class C(Base):
    def test2(self):
        print('------>CCC')


class D(A, B, C):
    pass


d = D()

print(inspect.getmro(D))
print(D.__mro__)
d.test()
d.test1()
d.test2()

"""
python允许多继承:
def 子类(父类1,父类2,...):
    pass

如果父类中有相同名称方法,搜索顺序:
广度优先顺序
"""