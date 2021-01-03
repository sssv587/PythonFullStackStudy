'''
应用场景:
1.猜大小   ---> 反复的猜大小
2.消消乐   ---> 反复充值
3.用户登录 ---> 登陆多次
  用户名
  密码 

循环结构：
for 变量名 in 集合
    语句

怎么用？
'''

# 使用系统给定的range()完成范围指定
# print(range(8)) # range(0,8)  包含0但是不包含8 0,1,2,3,4,5,6,7,8


# 打印三次
# for i in range(3):
# 	print('hello ---->',i)


# print('----game over----')



'''
循环：吃5个馒头

'''
name = '赵飞'

# 方式1：
# for i in range(5):
# 	print('{}很饿，正在吃第{}馒头'.format(name,i+1))

# 方式2：
# for i in range(1,6):
#     print('{}很饿，正在吃第{}馒头'.format(name,i))
# print('{}说：终于吃饱了'.format(name))

# range(n)  ---> 0~n-1
# range(m,n) ---> m~n-1


'''
吃馒头：在第三个馒头上抹了一点鹤顶红

'''

name = '张无忌'
for i in range(1,6):
	# 判断i的值是多少，i==3 别吃
	if i == 3:
		print('{}赶快扔了这个馒头，有剧毒："鹤顶红"!!!'.format(name))
	else:
		print('{}很饿，正在吃第{}馒头'.format(name,i))
print('{}说：终于吃饱了'.format(name))
