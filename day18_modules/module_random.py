# random 模块

import random

ran = random.random()  # 0~1之间的随机小数
print(ran)

ran = random.randrange(1, 10, 2)  # randrange(start,end,step)  1 ~ 10 step=2 ---> 1,3,5,7,9
print(ran)

ran = random.randint(1, 10)
print(ran)

list1 = ['sss', 'syh', 'sss1', 'sss2']
ran = random.choice(list1)  # 随机选择列表的内容
print(ran)

pai = ['红桃A', '黑桃A', '方块A', '梅花A']
random.shuffle(pai)  # 打乱顺序
print(pai)


# 验证码 大小写字母与数字的组合
def func():
    code = ''
    for i in range(4):
        ran1 = random.randint(1, 9)
        ran2 = chr(random.randint(65, 90))
        ran3 = chr(random.randint(97, 122))
        r = random.choice([ran1, ran2, ran3])
        code += str(r)
    return code


print(func())


# chr ord

print(chr(65))  # Unicode码 -----> str
print(ord('A'))  # str ----> Unicode码

print(ord('下'))  # 19979

print(chr(19979))

# print() input() list() str() dict() tuple()
# int() chr() ord() bin() hex() oct() isinstance()