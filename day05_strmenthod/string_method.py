# 字符串的内建函数：声明一个字符串，默认可以调用内建函数(准备好的一些函数)

# 第一部分：大小写
# capitalize() title() istitle() upper() isupper() lower() islower()

# message = 'zhaorui is a beautiful girl!'

# msg = message.capitalize()  # 将字符串额第一个字符转成大写的表示形式
# print(msg)



# msg = message.title() # 将字符串的每个单词的首字母大写
# print(msg)

# result = message.istitle() # 返回的结果是布尔类型，True False
# print(result)

# msg = message.upper() # 将字符串全部转成大写的表示形式
# print(msg)

# result = msg.lower() # 将大写全部转小写
# print(result)

# 案例：验证码案例

s='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'

# print(len(s)) # 求字符串长度 str(len),返回值是一个整形的数值


# 四个随机数
code=''

import random as rd

# IndexError:string index out of range
# index:0~len(s)-1  0~61 

for i in range(4):
	ran = rd.randint(0,len(s)-1)
	print(ran)

	code+=s[ran] # code=code+'V'

print('验证码是：'+code)

# 提示用户输入验证码

user_input=input('请输入验证码:')

if user_input.lower()==code.lower():
	print('验证码输入正确！')
else:
	print('验证码输入错误！')