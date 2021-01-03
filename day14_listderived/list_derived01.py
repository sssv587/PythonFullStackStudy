# 列表推导式  字典推导式 集合推导式
# 旧的列表 -----> 新的列表

# 1.列表推导式： 格式：[表达式  for 变量 in 旧列表] 或者 [表达式  for 变量 in 旧列表 if 条件]

# 过滤掉长度小于或者等于3的人名
names = ['tom', 'lily', 'abc', 'jack', 'steven', 'bob', 'ha']
result = [name for name in names if len(name) > 3]
print(result)

result = [name.capitalize().strip() for name in names if len(name) > 3]
print(result)

# 将1-100之间能被3整除，组成一个新的列表
newlist = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(newlist)

# 0~5 偶数 0~10奇数
# [(偶数),(奇数),()...] [(0,1),(0,3)...,(0,9),...(5,9)]
newlist = [(i, j) for i in range(5) if i % 2 == 0 for j in range(10) if j % 2 != 0]
print(newlist)

# list1 = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]] ---> [3,6,9,5]
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
newlist = [i[2] for i in list1]
print(newlist)

dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'lucy', 'salary': 8000}
dict3 = {'name': 'jack', 'salary': 4500}
dict4 = {'name': 'lily', 'salary': 4800}

list1 = [dict1, dict2, dict3, dict4]

# 如果薪资大于5000加工资加200，低于等于5000加500

newlist = [person['salary'] + 200 if person['salary'] > 5000 else person['salary'] + 500 for person in list1]
print(list1)
print(newlist)

newlist = [
    {person['name'], person['salary'] + 200} if person['salary'] > 5000 else {person['name'], person['salary'] + 500}
    for person in
    list1]
print(newlist)

'''
def func():
    newlist = []
    for name in names:
        if len(name)>3:
            name = name.title()
            newlist.append(name)
        return newlist

def func():
    newlist = []
    for i in range(5): # 偶数
        if i%2==0:
            for j in range(10):
                if j%2!=0:
                    newlist.append((i,j))
    return newlist    
'''

# 集合推导式 {}类似列表推导式，在列表推导式的基础上添加了一个去除重复项
list1 = [1, 2, 1, 4, 5, 6, 3, 4, 5, 8]

set1 = {x + 1 for x in list1 if x > 5}

print(set1)

# 字典推导式
dict1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'C'}

newdict = {value: key for key, value in dict1.items()}
print(newdict)
