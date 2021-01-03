# and or not 
# and 表示逻辑与
# or 逻辑或
# not 逻辑非


# 逻辑运算符的运算结果也是返回True False

# 
'''
只要一边为假False,结果就是False
True and True  ---->  True 其他情况
True and False  ---->  False 
False and True  ---->  False 
False and False  ---->  False
'''


n1 = 8 
n2 = 5
n3 = 3

result = n1 >= (n2+n3) and n1 > n2

'''
1.n1>=(n2+n3)   8 >= 8 True
2.n1>n2 8>5 True
3.True and True
4.结果:True
'''

n2 = n2 + n3
# n2 ---> 8

result = n1 >= n2 and n1 == n3
# True and False  ---> False

n4 = (n1 + n3) - n2
result = n4 < n1 and (n4 + n3) > n2 # False

'''
or:或者
手机号  或者  账户名

只要有一边为真True，结果即为真True
True or True  ---> True
False or True  ---> True
True or False  ---> True
False or False  ---> False
'''


# 判断是否存在用户
username = 'admin123'

email = '433434434@qq.com'

result = username == 'admin123' or email == '433434434@qq.com'
# False  or True ----> True

print('or ---->',result)

a = 2
b = 5
c = 7

result = (a+b) != c or c > a
print('or---222-->',result)


flag = False

result = not flag # not就是取反
print('not --->',result)