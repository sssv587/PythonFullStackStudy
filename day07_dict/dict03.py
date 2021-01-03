'''
增加元素 (key:value)
dict[key]=value -----> {key,value}

特点：key在字典中是唯一的,value值可以是不唯一的
{'name':'tom','name':'aaa'}  错误定义
{'张三':100,'李四':100,'王五':100}  正确

增加元素对比：
list1 = []
list1.append(element)

dict1 = {}

dict1[key] = value

修改：
list[index] = newvalue

dict1[key] = newvalue

查询：
list1[index] -----> element

dict1[key] -----> value

取值：字典都是根据key获取value值

'''

list1 = [3,5,7,8]

print(list1[2]) # 列表中找元素根据下标

dict1 = {'0':'张三','1':'李四','2':'王五'}

print(dict1['0']) # 字典中找元素根据key

dict2 = {'张三':100,'李四':99,'王五':89}

print(dict2['王五']) # key

# 考试分数大于90分的人
# 尝试对字典遍历

# for key in dict2:
# 	print(key)

# 单独遍历的结果是：字典的key


# 字典里面的函数：
# items() values() keys()
# print(dict2.items())

# 考试分数大于90分的人
# for i in dict2.items():
# 	print(i) # ('zhangsan',100)

# a,b = ('aa','bb')
for key,values in dict2.items():
	# print(key,values)
	if(values>=90):
		print(key)

# values:取出字典中所有的值，保存到列表中
result = dict2.values()
print(result)

for score in dict2.values():
	print(score)



total = sum(result)
avg = total/len(result)
print(avg)

# keys():获取字典中所有key键 (键值对)

names = dict2.keys()
print(names)

for name in names:
	print(name)

# 找人： in 也可以用于字典操作  用于判断元素有没有在字典的key中

# 8 in list1

print('王五' in dict2) 

'''
1.根据key获取值,如果key在字典中没有存在，则报出keyError
 dict[key] = value

2.字典的内置函数：get()
 get(key) ----> 如果取不到值则不会报错，则返回None
 get(key,default) ----> value 如果能够取到值则返回字典中的值，如果取不到则返回default的值

items()
keys()
values()
'''

# dict2['zhaofei']
print(dict2.get('zhaofei',99))