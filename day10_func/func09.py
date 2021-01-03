# 函数的综合应用
"""
用户登录
输入用户名
输入密码
输入验证码 -----> 封装成一个函数
"""
import random


def generate_checkcode(n):
    s = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(n):
        ran = random.randint(0, len(s))
        code += s[ran]
    return code


def login():
    username = input('输入用户名：')
    password = input('输入密码：')
    # 得到一个验证码
    code = generate_checkcode(5)  # 函数间调用
    print('验证码是:', code)
    code1 = input('输入验证码：')
    # 验证
    if code1.lower() == code.lower():
        # 验证码输入正确
        if username == 'lijiaqi' and password == '123456':
            print('用户登录成功！')
        else:
            print('用户名或者密码有误！')
    else:
        print('验证码输入有误！')


# 调用函数
login()