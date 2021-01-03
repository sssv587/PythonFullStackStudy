# pip install numpy -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

class stu(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


def run():
    return 'hello world'


s = run()
s1 = stu('加强')
print(s1)
