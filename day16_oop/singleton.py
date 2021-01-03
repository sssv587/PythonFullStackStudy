# 单例模式
# 开发模式

# class Student:
#     pass
#
#
# s = Student()
#
# s1 = Student()
#
# print(s)
# print(s1)

class singleton:
    # 私有化
    __instance = None
    name = 'jack'

    # 重写：__init__
    def __new__(cls, *args, **kwargs):
        print('----->__new__')
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def show(self, n):
        print('----->show', singleton.name, str(n))


s = singleton()
s1 = singleton()
print(s)
print(s1)

s.show(2)
s1.show(3)
