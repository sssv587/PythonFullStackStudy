import os

# 文件复制
src_path = r'D:\tmp_study\python\p1'
target_path = r'D:\tmp_study\python\p2'


# 封装成函数
def copy(src, target):
    if os.path.isdir(src) and os.path.isdir(target):
        filelist = os.listdir(src)

        for file in filelist:
            path = os.path.join(src, file)
            with open(path, 'rb') as rstream:
                container = rstream.read()
                path1 = os.path.join(target, file)
                with open(path1, 'wb') as wstream:
                    wstream.write(container)
        else:
            print('复制完毕!')


# 调用函数
copy(src_path, target_path)
