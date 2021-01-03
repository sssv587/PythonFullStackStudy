"""
加入购物车
判断用户是否登录，如果登录，成功加入购物车，否则表示请登录之后添加

成功 True 失败 False

def add_ShoppingCart(goodsName):
        pass

def login(username,password):
        pass
"""

islogin = False  # 用于判断用户是否登录变量 默认是没有登陆的


def add_ShoppingCart(goodsName):
    if islogin and goodsName:
        # 登陆的
        print('成功将{}加入到购物车中！'.format(goodsName))
    else:
        # 没有登陆
        print('用户没有登陆！或者没有添加任何商品！')


def login(username, password):
    if username == 'admin' and password == 'admin':
        # 登陆成功
        print('登陆成功')
        return True
    else:
        print('用户名或者密码有误！')


# 调用函数：添加商品到购物车中
un = input('请输入用户名：')
pw = input('请输入密码：')
is_login = login(un, pw)

add_ShoppingCart('阿玛尼红唇')
