# 函数：带参数的
"""
def 函数名(参数,参数,...):
    函数体
调用:
    pass
"""
import random


# 取随机数的函数，产生随机数的个数？
def generate_random(number):  # 形参：形式上的参数 number=5
    for i in range(number):
        ran = random.randint(1, 20)
        print(ran)


print(generate_random)
# <function generate_random at 0x0000016808014AF8>

# 调用
generate_random(5)  # 实参:实际的参数，具体的值


# generate_random(8)

# 求加法的函数
def add(a, b):
    result = a + b
    print('和是:', result)


# 调用
add(4, 5)
