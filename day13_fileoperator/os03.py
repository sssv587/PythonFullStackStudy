# os.path里面的函数
# os中函数
import os

dir = os.getcwd()
print(dir)

all = os.listdir(r'./')  # 返回指定目录下的所有的文件和文件夹,保存到列表中
print(all)

# 创建文件夹
# if not os.path.exists(r'c:\f1'):
#     f = os.mkdir(r'c:\f1')
#     print(f)

# 删除文件夹
# f = os.rmdir(r'g:/asdasd') # 只能删除空的文件夹

# f = os.removedirs(r'c:\p3')  # 空删除目录
# print(f)

os.remove(r'c:\f3\aa.txt')

# 删除p4文件夹
path = r'c:\p3\p4'

filelist = os.listdir(path)

for file in filelist:
    path = os.path.join(path, file)
    os.remove(path)
else:
    os.rmdir(path)
print('删除成功')

# 切换目录

f = os.chdir(r'c:\p1\p2')
print(f)
path = os.getcwd()
print(path)

'''
os模块下方法:
os.getcwd() 获取当前目录
os.listdir() 浏览文件夹
os.mkdir() 创建文件夹
os.rmdir() 删除空文件夹
os.remove() 删除文件
os.chdir() 切换目录
'''
