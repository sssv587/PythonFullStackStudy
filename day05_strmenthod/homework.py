'''
输入两个字符串，从第一个字符串中删除第二个字符串中所有的字符
例如，输入"They are students."和"aeiou"
则删除之后的第一个字符串变成"Thy r stdnts."

'''

# s1 = 'They are students.'
# s2 = 'aeiou'
# s3 = ''

# 字符串： 'hdfasfa'
# 方法一:
# for i in s1:  # 类似range(6)
# 	# print(i,end='')
# 	if i not in s2: # t not in 'they'
# 		s3+=i
# print(s3)

# s1 = s3
# print(s1)

# 方法二:
# for i in s2:
# 	s1 = s1.replace(i,'')
# print(s1)

# 方法三:
# for i in s2:
# 	if i not in s3:
# 		s3+=i
# print(s3) #去除重复项

# for i in s3:
# 	s1=s1.replace(i,'')

# print(s1)

'''
小易喜欢的单词具有如下特点:
1.单词每个字母都是大写字母
2.单词没有连接相等的字母

例如:
小易不喜欢"ABBA",因为这里有两个连续的'B'
小易喜欢'A',"ABA"和"ABCBA"这些单词
给你一个单词，你要回答小易是否会喜欢这个单词
'''


# word = input('请输入单词:') # 'HELLO'

# for i in range(len(word)): # 循环单词的长度的次数
# 	if word[i] > 'Z' or word[i] < 'A':
# 		print('不喜欢,不是大写的！')
# 		break
# 	else:
# 		# A~Z
# 		if i<len(word)-1 and word[i]==word[i+1]:
# 			print('不喜欢！是叠词！')
# 			break
# else:
# 	print('喜欢')





s=''

while True:
	username = input('请输入用户名:')
	password = input('请输入密码:')
	email = input('请输入密码:')

	username = username[0:20]
	password = password[0:20]
	email = email[0:20]

	msg = '{}\t{}\t{}\n'.format(username,password,email)

	msg = msg.expandtabs(20)

	s+=msg

	if username=='q' or username == 'Q' or password=='q' or password == 'Q' or email=='q' or email == 'Q':
		break


print(s)