# 在发开中看到一些私有化处理:装饰器


class Student:
    def __init__(self, name, age):
        self.name = name  # 长度必须6位
        self.__age = age
        self.__score = 20

    # 先有get
    @property
    def age(self):
        return self.__age

    # 再有set,因为set依赖于get
    @age.setter
    def age(self, age):
        if 0 < age <= 120:
            self.__age = age
        else:
            print('年龄不在规定的范围内!')

    def __str__(self):
        return '姓名:{},年龄:{},考试分数:{}'.format(self.name, self.__age, self.__score)


shy = Student('theshy', 20)

shy.name = 'theshy'

# 私有化赋值
print(shy.age)
shy.age = 40
print(shy)
