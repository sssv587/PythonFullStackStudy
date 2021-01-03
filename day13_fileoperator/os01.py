# 模块：os py

"""
os.path
os.path.dirname(__file__)获取当前文件所在的文件目录(绝对路径)
os.path.join(path,'') 返回的是一个拼接后的新的路径
"""

import os

print(os.path)

# path = os.path.dirname(__file__)  # 获取当前文件所在的文件目录(绝对路径)
# print(path)
# print(type(path))
# result = os.path.join(path,'karsa.jpg')
# print(result)


with open(r'D:/tmp_study/python/karsa.jpg', mode='rb') as stream:
    container = stream.read()  # 读取文件内容
    print(stream.name)
    file = stream.name
    filename = file[file.rfind(r'/') + 1:] # 截取文件名
    print(filename)

    path = os.path.dirname(__file__)
    path1 = os.path.join(path, 'karsa.jpg')

    with open(path1, mode='wb') as wstream:
        wstream.write(container)
