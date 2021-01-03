# 语法错误和异常
# 语法错误：
# while True:
#       print('-----')


# number = 100
#
# def func():
#     global number
#     number += 1


# 异常:程序运行的时候报出来的。xxxError
def chu(a, b):
    return a / b


x = chu(1, 3)  # ZeroDivisionError: division by zero
# print(x)

# 异常处理:
'''
try:
    可能出现异常的代码
except:
    如果有异常执行的代码
finally:
    无论是否存在异常都会被执行的代码

情况1:
    try:
        有可能会产生多种异常
    except 异常的类型1:
        pass
    except 异常的类型2:
        pass
    except Exception:
        pass
    如果是多个except,异常类型的顺序需要注意,最大的Exception要放到最后

'''


def func():
    try:
        n1 = int(input('输入第一个数字:'))
        n2 = int(input('输入第二个数字:'))
        # +加法
        per = input('输入运算符号(+、-、*、/):')
        result = 0
        if per == '+':
            result = n1 + n2
        elif per == '-':
            result = n1 - n2
        elif per == '*':
            result = n1 * n2
        elif per == '/':
            result = n1 / n2
        print('结果是:', result)
    except ZeroDivisionError:
        print('除数不能为零!!!!')
    except ValueError:
        print('必须输入数字!!!!')
    except Exception as e:
        print('出错啦!' + str(e))
    finally:
        pass


# func()

'''
# 文件操作 stream = open(...) 
try:
    pass
except:
    pass
finally:
    pass
'''


def funcc():
    stream = None
    try:
        stream = open(r'c:sss\sss.txt')
        container = stream.read()
        print(container)
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('----finally-----')
        if stream:
            stream.close()
        return 3


s = funcc()
print(s)
