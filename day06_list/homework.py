'''
字符串中可以使用的符号
+
*
in
not in
is 
not is
[]
'''

'''
列表支持的符号
+
*
in
'''

l1 = [1,2,3]
l2 = [4,5,6]

l3 = l1 + l2
print(l3)

l4 = l1 * 3
print(l4)


result = 3 in [1,2,3,4]
print(result)

result = [3] in [1,2,3,4]
print(result)

'''
列表中的元素:
整形
字符串类型
浮点型
列表
元组
字典
对象
'''



# list(range(1,10,3))

print(range(1,10,3)) # 1,4,7

'''
类型转换
str()
int()
list() 将指定的内容转成列表,可迭代的内容可以放到list中

s = 'abc'
result = list(s) # ['a','b','c']

iterable 可迭代的 for...in里面可以循环的就是可迭代的

'abcdef' ---> a b c

for i in range(5):
	pass
'''
print(list(range(1,10,3))) # 1,4,7

s = 'abc'
result = list(s)
print(result)


x = 'abc'
y = 'def'
z = ['d','e','f']
print(x.join(y))
print(x.join(z))
