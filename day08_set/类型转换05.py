# 类型转换
# str() int() list() dict() set() tuple()

# str ----> int,list,set,tuple

s = '8'

i = int(s)

s = 'abc'

l = list(s)

print(l) # ['a', 'b', 'c']

s = set(s)
print(s)

t = tuple(s)
print(t)



# 反过来: int,list,set,tuple,dict,float  ---->  str 

i = 8

s = str(i)

l = str(['a','b','c'])

print(l,type(l))



# list ---> set(),tuple(),可以转成字典[(k,v),(k,v),(k,v)]

# tuple、set ----> list

tuple1 = (1,2,3,4)

print(list(tuple1))

set1= {1,2,3,4}

print(list(set1))

dict1 = {1:'a',2:'b'}

print(list(dict1)) # 只是将key保存在list中