'''
1.产生10个1~20的随机数，去除里面的重复项
2.键盘输入一个元素，将此元素从不重复的集合中删除

'''

import random


# 方式一：
list1 = []

set1 = set()

for i in range(10):
	ran = random.randint(1,20)
	list1.append(ran)

set1.update(list1)

print(list1)
print(set1)

# num = input('请输入一个数字：')

# set1.discard(num)

# print('删除之后的结果是：',set1)



# 方式二：
set1 = set()

for i in range(10):
	ran = random.randint(1,20)
	set1.add(ran)

print(set1)

# num = input('请输入一个数字：')

# set1.discard(num)

# print('删除之后的结果是：',set1)



# 其他：符号操作
print(6 in set1)

set2 = {2,3,4,5,6}
set3 = {2,3,4,5,6,7,8}

print(set2==set3) # 判断两个集合中内容是否相等

# 测试
print(set2 != set3) # True

# 不支持:+ *
# - 差集 
# & 交集
# | 并集

# set4 = set2 + set3 # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# set5 = set2*2 # TypeError: unsupported operand type(s) for *: 'set' and 'int'

set4 = set3 - set2 # 差集  difference()
print(set4)

set5 = set3.difference(set2)
print(set5)


# & 交集  intersection()
set6 = set3 & set2
print(set6)

set7 = set3.intersection(set2)
print(set7)

# | 并集 union() 联合
set8 = set3|set2
print(set8)

set9 = set3.union(set2)
print(set9)