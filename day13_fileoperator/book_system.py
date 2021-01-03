# 图书管理系统
# list 元组，字典 ---> 内存

# 用户注册
def register():
    username = input('输入用户名:')
    password = input('输入密码:')
    repressor = input('输入确认密码:')

    if password == repressor:
        # 保存信息
        with open(r'D:\tmp_study\python\p2\users.txt', 'w') as wstream:
            wstream.write('{} {}\n'.format(username, password))
        print('用户注册成功!')
    else:
        print('密码不一致!')


# 用户登录
def login():
    username = input('输入用户名:')
    password = input('输入密码:')

    if username and password:
        with open(r'D:\tmp_study\python\p2\users.txt') as fstream:
            while True:
                user = fstream.readline()  # admin 123456\n
                if not user:
                    print('用户名或者密码输入有误!')
                    break

                input_user = '{} {}\n'.format(username, password)

                if user == input_user:
                    print('用户登陆成功!')
                    break


def show_books():
    print('-------图书馆里面的图书有:---------')
    with open(r'D:\tmp_study\python\p2\book.txt', encoding='utf-8') as rstream:
        books = rstream.readlines()
        for book in books:
            print(book)


# 调用函数
# register()
# login()
# show_books()
