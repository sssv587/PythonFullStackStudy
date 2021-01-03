# 定义函数：随机数的产生
import random


def generate_random():
    for i in range(10):
        ran = random.randint(1, 20)
        print(ran)


print(generate_random)  # 打印函数名
# <function generate_random at 0x00000194E18F4AF8>

# 调用：函数名()  找到函数并执行函数体的内容
generate_random()
