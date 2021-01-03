# 不重复的集合
list1 = [2,342,4,435,46,1,34,346,3,2]

# 声明集合：set

s1 = set()

s2 = {1,3,7} # 字典：{key:value,key:value,...}  集合 {元素1，元素2，元素3.....}

print(type(s1))
print(type(s2))

# 应用： 如何将一个列表快速去重 set()
s3 = set(list1)
print(s3)  # {1,2,3,4,5,....}

# 增删改查：

# 1.增加  s1 = set()
s1.add('hello')

s1.add('小猪佩奇')

s1.add('lucy')

print(s1)

# add()  添加一个元素
# update() 添加多个元素，

t1 = ('aa','bb','cc')
s1.update(t1) # {'aa', 'bb', 'cc', 'lucy', '小猪佩奇', 'hello'}
print(s1)

s1.add(t1)
print(s1) # {'aa', 'bb', 'cc', 'lucy', ('aa', 'bb', 'cc'), '小猪佩奇', 'hello'}


#2.删除 remove # 如果元素存在则删除，如果不存在则报错keyError 
#       pop 随机删除  (一般删除第一个元素)
#       clear  清空
#       dicard() 类似remove() 在移除不存在的元素的时候不会报错

s1.remove('aa')
print(s1)

# s1.remove('道明寺') # KeyError
# print(s1)


s1.pop()
print(s1)

s1.clear() # 清空
print(s1)