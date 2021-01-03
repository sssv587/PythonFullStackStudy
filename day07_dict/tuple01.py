'''
总结列表:
list

1、定义


l = [] 空列表
l = ['aaa']


2.符号
+  ----> 合并 [] + []
*  ----> [] * n
in ----> a in [] False / True
not in ---->
is  地址是否相等
not is

3.系统中给列表提供的函数
len(list)   ----> int 
sorted(list)  ----> 排序
max(list)  ----> 最大值
min(list)  ----> 最小值
list(list)  ----> 转换为list类型
enumeate(list)  ----> index,value

4.列表自身的函数：
添加函数:
	append()  末尾添加
	extend()  末尾添加一组元素
	insert()  指定位置插入

删除：
	del list[index]
	remove(obj) 删除指定的元素，如果指定元素不存在则报异常
	pop() 队列 FIFO 栈 FILO  默认删除最后一个元素
	clear() 清空元素

其他：
    count() 指定元素个数
    sort() 排序
    reverse() 反转

 算法：
    选择排序：
    冒泡排序：
'''


'''
元祖：
类似列表(当成容器)
特点：
1.定义的符号:() 
2.元祖中的内容不可修改
3.关键字:tuple  

列表         元祖
 []           ()
 [1]          (1,)
 [1,2]        (1,2)


'''


t1 = ()
print(type(t1))  # <class 'tuple'>


t2 = ('hello',)  
print(type(t2))

t3 = ('aa','bb')
print(type(t3))



# 
t4 = (3,4,5,1,2,3,4,5,6)

# 增删改 查
import random

list1=[]

for i in range(10):
	ran = random.randint(1,20)
	list1.append(ran)

print(list1)

# tuple()  list()
t5 = tuple(list1)
print(t5)


# 查询：下标index 切片 [:]
print(t5[0])
print(t5[-1])

print(t5[2:-3])

print(t5[::-1])

# 最大值  最小值
print(max(t5))

print(min(t5))

# 求和
print(sum(t5))


# 求长度
print(len(t5))


# 元祖中的函数：
# index()   ----> 个数
# count()   ----> 下标

print(t5.count(1)) # 个数

print(t5.index(1)) # 从t5这个元祖中找出4的下标位置，没有报错 ValueError: tuple.index(x): x not in tuple

