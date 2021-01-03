# 私有化
# 封装:1.私有化属性 2.定义共有set和get方法
# __属性:就是将属性私有化，访问范围仅仅限于类中

"""
好处:
1.隐藏属性不被外界随意修改
2.也可以修改:通过函数
  def setXXX(self,xxx):
        3.筛选赋值的内容
            if xxx是否符合条件
                赋值
            else:
                不赋值
3.如果想获取具体的某一个属性
  使用get函数
    def getXXX(self):
        return self.__xxx

"""


class Student:
    def __init__(self, name, age):
        self.__name = name  # 长度必须6位
        self.__age = age
        self.__score = 20

    # 定义共有set和get方法
    # set是为了赋值
    def setAge(self, age):
        if 0 < age <= 120:
            self.__age = age
        else:
            print('年龄不在规定的范围内!')

    def setName(self, name):
        if len(name) == 6:
            self.__name = name
        else:
            print('名字长度必须是6位!')

    # get是为了取值
    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def __str__(self):
        return '姓名:{},年龄:{},考试分数:{}'.format(self.__name, self.__age, self.__score)

    # attribute:setName getName _str__ __init__


susses = Student('susses', 18)
print(susses)
susses.setAge(95)
print(susses)

print(dir(Student))
print(__name__)
print(dir(susses))

print(susses._Student__age)  # 其实它就是__age,只不过系统自动改名字了
print(susses.__dir__())
