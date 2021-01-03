# 字符串内建函数: ecode decode

# 编码: 网络应用  (中文一般设计编码问题)

# msg='上课啦！认真听课！' # 中文的
 

# gbk 中文 gb2312 简体中文 unicode 

# result = msg.encode('utf-8')

# print(result) # 


# # 解码
# m = result.decode('utf-8')
# print(m)


# 字符串内建函数: startswith() endswith()  返回值都是布尔类型 True False

# startswith判断是否是以xxx开头的，endswith判断是否是以xxx结尾的

# 文件上传 只能上传(jpg,png,bmp,gif)

# filename='笔记.doc'

# result = filename.endswith('doc') # filename是否是以txt结尾的

# print(result)


# s = 'hello'

# result = s.startswith('he')
# print(result)


# 文件上传 只能上传(jpg,png,bmp,gif)
# file = input('请选择文件:') # C:\foo\bar\desk_background.jpg
# path = 'C:\\foo\\bar\\desk_background.jpg'

# # 分析:要上传的文件的路劲path---->文件名----->通过文件名再判断是否是图片类型
# p = path.rfind('\\')

# filename = path[p+1:]
# print(p,filename)

# # 判断是否是图片类型？
# if filename.endswith('jpg') or filename.endswith('png') or filename.endswith('bmp'):
# 	print('是图片，允许上传！')
# else:
# 	print('不是图片格式，只能上传图片！')



'''
练习:
    给定一个路径，上传文件（记事本txt或者是图片jpg，png）
    如果不是对应格式的，允许重新指定上传文件
    如果符合上传规定的则提示上传成功

'''
while True:
	file = input('请选择文件:') # C:\foo\bar\desk_background.jpg

	# 分析:要上传的文件的路劲path---->文件名----->通过文件名再判断是否是图片类型
	p = file.rfind('\\')

	filename = file[p+1:]  # 通过切片截取出来文件名
	print(p,filename)

	# 判断是否是图片类型？
	if filename.endswith('jpg') or filename.endswith('png') or filename.endswith('txt'):
		print('是图片，允许上传！')
		break
	else:
		print('不是图片格式，只能上传图片！')
		s = input('请确定是否重新上传?y/n')
		if s.upper() == 'Y':
			continue
		else:
			break