# 开发：登陆验证
import time

islogin = False  # 默认是没有登陆的


# 定义一个登陆函数
def login():
    username = input('输入用户名:')
    password = input('输入密码:')
    if username == 'admin' and password == 'admin':
        return True
    else:
        return False


# 定义一个装饰器,进行付款验证
def login_required(func):
    def wrapper(*args, **kwargs):
        global islogin
        print('-------付款--------')
        # 验证用户是否登录
        if islogin:
            func(*args, **kwargs)
        else:
            # 跳转到登录页面
            print('用户没有登录，不能付款！')
            islogin = login()
            print('islogin:', islogin)

    return wrapper


@login_required
def pay(money):
    print('正在付款,付款金额是:{}元'.format(money))
    print('付款中....')
    time.sleep(2)
    print('付款完成!')


pay(10000)

pay(1)
