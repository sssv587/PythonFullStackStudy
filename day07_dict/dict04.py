# 增加 改 查(key)  删除
# 删除:
list1 = [3,6,7,8]

del list1[1]

print(list1)

dict1 = {'张三':100,'李四':99,'王五':89}

del dict1['王五']

print(dict1)


# del dict1['haha'] # keyError

# 字典的内置函数:删除
# dict1.remove('李四')  # 不存在这个方法 报错
# pop(key[,default]) ----> 根据key来删除字典中的键值对，返回值是删除成功的键值对的值
# pop的默认值，往往是在删除的时候没有找到对应的key，则返回default默认值

result = dict1.pop('李四','80') 
print(result)
print(dict1)

result = dict1.pop('张小三',80)
print(result)


# popitem():随即删除字典中键值对(一般是从末尾删除元素)

dict1 = {'张三':100,'李四':99,'王五':89}

result = dict1.popitem()
print(result)

print(dict1)


# clear() 同列表的clear()

dict1.clear()
print(dict1)


'''
删除：
del dict[key]

dict.pop[key[,default]]

dict.popitem()

dict.clear()

'''

'''
其他的内置函数：
update()     [] + []  合并操作
fromkeys(seq)  ------> 将seq转成字典的形式  如果没有指定默认的value则用None
list1 = ['aa','bb','cc']  new_dict = dict1.fromkeys(list1,10)  ----> {'aa': None, 'bb': None, 'cc': None}
               ------> 如果指定default，则用default替代None这个value值
list1 = ['aa','bb','cc'] new_dict = dict1.fromkeys(list1,10)  ----> {'aa': 10, 'bb': 10, 'cc': 10}
'''

dict1 = {0:'tom',1:'jack',2:'lucy'}

dict2 = {0:'lily',4:'ruby'}


print(dict1.update(dict2))

# dict1 = dict1 + dict2 报错的

print(dict1)
print(dict2)

list1 = ['aa','bb','cc']
new_dict = dict1.fromkeys(list1,10)
print(new_dict)