# is a  base class  父类  基类
"""
继承：
    Student、Employee、Doctor ----> 都属于人类
    相同代码 ----> 冗余,可读性不高

    将相同代码提取 ----> Person类
     Student、Employee、Doctor ---> 继承Person

     class Student(Person):
            pass

特点：
    1.如果类中不定义__init__,调用父类 super class的__init__
    2.如果类继承父类也需要定义自己的__init__,就需要在当前类的__init__调用一下父类__init__
    3.如何调用父类__init__:
        super().__init__(参数)
        super(类名,对象).__init__(参数)
    4.如果父类有eat(),子类也定义一个eat方法,默认搜索的原则,先找当前类,再去找父类
        s.eat()
        overried  重写(覆盖)
        父类提供的方法不能满足子类的需求,就需要在子类中定义一个同名的方法,这种行为:重写
    5.子类的方法也可以调用父类方法
        super().方法名(参数)
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, *args):
        print(self.name + '正在吃饭...')

    def run(self):
        print(self.name + '正在跑步...')


class Student(Person):
    # def __init__(self, name, age):
    #     # 如何调用父类__init__
    #     super().__init__(name, age)  # super() 父类对象
    #     print('----->student对象的init')
    def __init__(self, name, age, clazz):
        super(Student, self).__init__(name, age)
        self.clazz = clazz

    def study(self, course):
        print('{}同学正在学习{}课程'.format(self.name, course))

    def eat(self, food):
        super(Student, self).eat()
        print('{}正在吃饭...喜欢吃宫保鸡丁和{}'.format(self.name, food))


class Employee(Person):
    def __init__(self, name, age, salary, manager):
        super(Employee, self).__init__(name, age)
        self.salary = salary
        self.manager = manager


class Doctor(Person):
    def __init__(self, name, age, patient):
        super(Doctor, self).__init__(name, age)
        self.patient = patient


s = Student('jack', 18, 'python')
s.run()
s.eat('盖浇饭')
s.study('python基础')

e = Employee('tom', 23, 10000, 'king')
e.run()

lists = ['zhangsan', 'lisi', 'wangwu']
d = Doctor('lucy', 30, lists)
d.run()
