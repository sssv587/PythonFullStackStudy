# map函数
from functools import reduce

list1 = [2, 3, 34, 5, 31, 3, 435, 13, 134, 2]
result = map(lambda x: x + 2, list1)
print(list(result))

# func = lambda x: x if x % 2 == 0 else x + 1
# result = func(5)
# print(result)

# 对列表中的奇数进行加1操作
result = map(lambda x: x if x % 2 == 0 else x + 1, list1)
print(list(result))

for index, i in enumerate(list1):
    if i % 2 != 0:
        list1[index] = i + 1

# reduce():对列表中的元素进行加减乘除运算的函数
tuple1 = (3, 5, 7, 9, 11)
result = reduce(lambda x, y: x + y, tuple1)
print(result)

tuple2 = (1,)
result = reduce(lambda x, y: x - y, tuple2, 100)
print(result)

# filter()函数
list1 = [12, 6, 8, 15]
result = filter(lambda x: x > 10, list1)
print(list(result))

list2 = []
for i in list1:
    if i > 10:
        list2.append(i)
print(list2)
print(list1)

students = [
    {'name': 'tom', 'age': 20},
    {'name': 'lucy', 'age': 19},
    {'name': 'lily', 'age': 13},
    {'name': 'mark', 'age': 21},
    {'name': 'jack', 'age': 28}
]
# 找出所有年龄大于20岁学生
result = filter(lambda x: x['age'] > 20, students)
print(list(result))

# 按照年龄从小到大排序
result = sorted(students, key=lambda x: x['age'], reverse=True)
print(result)

'''
:cvar
max()
min()
sorted()

map()
reduce()
filter()
'''