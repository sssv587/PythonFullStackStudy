# 函数和类里面定义的方法

# def func(name):
#     print('---->',name)
#
# username = 'admin'
# func(username)

def func(names):
    for name in names:
        print(name)


name_list = ['aa', 'bb', 'cc']
func(name_list)


class Phone:
    # 魔术方法之一: 称作魔术方法 __名字__()
    def __init__(self):  # 初始化
        self.brand = 'xiaomi'
        self.price = 4000

    def call(self):  # self是不断发生改变
        print('------>call')
        print('价格:', self.price)  # 不能保证每个self中都存在price


p = Phone()
p.price = 5000
p.call()


class Person:
    name = '张三'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self,food):
        print('{}正在吃{}！'.format(self.name,food))

    def run(self):
        print('{}的年龄是{},正在跑步~~~'.format(self.name, self.age))


p = Person('李四', 50)
p.eat('黄焖鸡')
p.run()

p1 = Person('王五', 20)
p1.eat('酸菜鱼')
p1.run()

p2 = Person('赵六', 19)
p2.run()