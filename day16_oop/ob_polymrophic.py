# 多态 封装 继承 ----> 面向对象
class Person:
    def __init__(self, name):
        self.name = name

    def feed_pet(self, pet):  # pet既可以接收cat，也可以接受dog，还可以接受tiger
        # isinstance(obj,类)  ----> 判断obj是不是类的对象或者判断obj是不是该类子类的对象
        if isinstance(pet, Pet):
            print('{}喜欢养宠物{}：{}'.format(self.name, pet.role, pet.nickname))
        else:
            print('不是宠物类型。。。')


class Pet:
    role = 'Pet'

    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def show(self):
        print('昵称:{}，年龄:{}'.format(self.nickname, self.age))


class Cat(Pet):
    role = '猫猫'

    def catch_mouse(self):
        print('抓老鼠....')


class Dog(Pet):
    role = '狗狗'

    def watch_house(self):
        print('看家高手....')


class Tiger:
    def eat(self):
        print('小tiger呀')


# 创建对象
cat = Cat('小花花', 2)

dog = Dog('大黄', 4)

p = Person('sss')

p.feed_pet(cat)
p.feed_pet(dog)

# Pet
# pet 父类     cat dog 子类
# pet 大类型   cat dog 小类型

