# 文件的复制

"""
原文件：D:/tmp_study/python/karsa.jpg
目标文件：D:/tmp_study/karsa.jpg

with 结合open使用，可以帮助我们自动释放资源
"""

with open(r'D:/tmp_study/python/karsa.jpg', mode='rb') as stream:
    container = stream.read()  # 读取文件内容

    with open(r'D:/tmp_study/karsa.jpg', mode='wb') as wstream:
        wstream.write(container)

print('文件复制完成！')
