import os

result = os.path.isabs(r'C:\Users\10926\PycharmProjects\PythonFullStackStudy\day13_fileoperator\karsa.jpg')
print(result)
# True

# ../表示当前文件的上一级
result = os.path.isabs('./karsa.jpg')
print(result)
# False

# 获取路径：directory 目录  文件夹
# 当前文件所在文件夹的路径
path = os.path.dirname(__file__)
print(path)
# C:/Users/10926/PycharmProjects/PythonFullStackStudy/day13_fileoperator

# 通过相对路径得到绝对路径
path = os.path.abspath('karsa.jpg')
print(path)
# C:\Users\10926\PycharmProjects\PythonFullStackStudy\day13_fileoperator\karsa.jpg

# 获取当前文件的绝对路径
path = os.path.abspath(__file__)
print(path)
# C:\Users\10926\PycharmProjects\PythonFullStackStudy\day13_fileoperator\os02.py

path = os.getcwd()
print(path)
# C:\Users\10926\PycharmProjects\PythonFullStackStudy\day13_fileoperator

# os.path
path = r'C:\Users\10926\PycharmProjects\PythonFullStackStudy\day13_fileoperator\os02.py'

result = os.path.split(
    path)  # ('C:\\Users\\10926\\PycharmProjects\\PythonFullStackStudy\\day13_fileoperator', 'os02.py')

print(result[1])
# filename = path[path.rfind('\\')+1:]

result = os.path.splitext(path)  # 分割文件与扩展名
print(result)
# ('C:\\Users\\10926\\PycharmProjects\\PythonFullStackStudy\\day13_fileoperator\\os02', '.py')

size = os.path.getsize(path)  # 获取文件大小  单位字节
print(size)

result = os.path.join(os.getcwd(), 'file', 'a1.jpg')
print(result)
# C:\Users\10926\PycharmProjects\PythonFullStackStudy\day13_fileoperator\file\a1.jpg

'''
os.path
dirname()
join()

split()
splittext()
getsize()

isabs()
isfile()
isdir()
'''
