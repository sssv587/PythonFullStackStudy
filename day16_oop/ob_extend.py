# 继承:is a,has a
import random


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


# 声明(定义)Car
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):
        ran_time = random.randint(1, 10)
        msg = '{}品牌的车在{}上以{}速度行驶{}小时'.format(self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的,速度:{}'.format(self.brand, self.speed)


# 创建实例化对象
road = Road('京藏高速', 12000)

car = Car('玛莎拉蒂', '120km/h')

car.get_time(road)
