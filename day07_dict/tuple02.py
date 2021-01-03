# 拆包

t1 = (4,7,3)

# a,b=t1 # ValueError:too many values to unpack(拆包) (expected 3, got 2)
a,b,c = t1

print(a,b,c)

a = t1

print(a)

# x,y,z = (6,) # ValueError: not enough values to unpack (expected 3, got 1)


# s1 = 'hello'
# s2 = s1

# 变量个数与元祖个数不一致
t1 = (12,23,42,12,43)

a,*_,c = t1

print(a,c,_)

a,c,*_ = t1

print(a,c,_)

a,*b,c = t1

print(a,c,b)

t1 = (9,4,9)

a,*b = t1
print(a,b)  # *b表示未知个数0~n  0--[]  多个元素的话 ~ [1,2,3,4,5,.....]

print(*b)

'''
字符串 
列表

通用

'''

t2 = (9,)

x,*y=t2

print(x,y) # 9,[]

# 添加元素
y.append('a')
y.append('b')
print(y)  # ['a','b']


print(*y) # print()  print(4,8,6)  4 8 6

'''
元祖:
1.符号(1,2,3) tuple
2.关键字 tuple
3.元祖的元素只能获取，不能增删改

符号：
+
*
is not
in / not in

系统函数：
max()
min()
sum()
len()
sorted() -----> 排序，返回的结果就是列表
tuple() -----> 元祖类型的强制转换

元祖自带函数：
index()
count()


拆装包:
x,*y = (1,2,3,4,5)
print(y)
print(*y)

'''


t2 = (4,5)+(1,2)
print(t2)

t3 = (3,4)*2
print(t3)


print(t2 is t3)

print(3 not in t3)

print(len(t2))

print(sorted(t2))

print(tuple(sorted(t2)))