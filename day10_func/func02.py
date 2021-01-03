# 可变参数 + 关键字参数
# 关键字参数：key=value

def add(a, b=10):  # 关键字参数  此时的b就是默认值
    result = a + b
    print(result)


# 调用
add(5)

add(4, 7)  # a=4,b=7  此时7就会覆盖b原来的默认值


def add_1(a, b=10, c=4):
    print(a, b, c)
    result = a + b + c
    print(result)


add_1(1)

add_1(1, 5)  # 是给b赋值成功

# 给c赋值而不是给b赋值
add_1(2, 6)  # 默认6是赋值给b了
add_1(2, c=6)  # 如果想将6赋值给c，则需要结合关键字的key使用

# 函数:打印每位同学的姓名和年龄
students = {
    '001': ('泰隆', 20),
    '002': ('劫', 19),
    '003': ('梦魇', 19),
    '004': ('小鱼人', 19)
}


def print_boys(name, **persons):  # persons=students
    print(persons)  # 字典
    print('{}喜欢玩的英雄是:'.format(name))
    if isinstance(persons, dict):
        for name, age in persons.values():
            print('{}的年龄是:{}'.format(name, age))


# 调用
print_boys('蕊蕊', **students)


def func(**kwargs):  # 必须是key=value形式
    print(kwargs)


# 调用
func(a=1, b=2, c=3)  # 关键字参数  {'a': 1, 'b': 2, 'c': 3}

func()  # {}
func(a=1)  # {'a': 1}

dict1 = {'001': 'python', '002': 'java', '003': 'c++'}
print(*dict1)

# **dict的方式将字典进行拆包 001=python,002=java,003=c++
func(**dict1)
