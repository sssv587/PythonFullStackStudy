import os

# 文件复制
src_path = r'D:\tmp_study\python\p1'
target_path = r'D:\tmp_study\python\p2'


def copy(src_path, target_path):
    # 获取文件夹里面内容
    filelist = os.listdir(src_path)
    # 变量列表
    for file in filelist:
        # 拼接路径
        path = os.path.join(src_path, file)
        # 判断是文件夹还是文件
        if os.path.isdir(path):
            finnal_path = target_path + r'\{}'.format(file)
            # 递归调用copy
            copy(path, finnal_path) if os.path.exists(finnal_path) else os.mkdir(finnal_path), copy(path, finnal_path)
        else:
            with open(path, 'rb') as rstream:
                container = rstream.read()
                path1 = os.path.join(target_path, file)
                with open(path1, 'wb') as wstream:
                    wstream.write(container)
    else:
        print('复制完成')


copy(src_path, target_path)
