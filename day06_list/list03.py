'''
['hello','good','apple','world','digit','alpha']
提示输入一个单词:比如hello，如果输入的单词在列表中则删除
最后打印删除后的列表

'''

words = ['hello','good','gooo','world','digit','alpha']

w = input('请输入一个单词:')

# 方式1：
# if w in words:
# 	print('存在此单词!')

# 'abc' in ['abc','hello','aaaaa',....] 内容有没有在列表中存在
# 'go' in 'good' 判断字符串w有没有出现在word
# for word in words:  # ''  in [....]  判断内容有没有在列表中存在
# 	if w in word: # w in word 判断字符串w有没有出现在word中
# 		print('存在此单词!')
# 		break

# for word in words:
# 	if w in word:
# 		del word
# 		break

# print(words)

i = 0 # 表示下标

l = len(words)

# 方法一:
# while i<l:
# 	if w in words[i]:
# 		l-=1
# 		del words[i]
# 	else:
# 		i+=1
# print(words)

# 方法二:
while i<l:
	if w in words[i]:
		l-=1
		del words[i]
		continue
	i+=1
print(words)