# 返回值:

def add(a, b):
    result = a + b
    return a, b, result


# 调用函数
x = add(1, 2)
print(x)

'''
return返回值
1.return后面可以是一个参数 接收的时候x=add(1,2)
2.return后面也可以是多个参数，如果是多个参数则底层会将多个参数先放在一个元组中，将元组整体返回
x = add(1,2) ---> x=(1,2,3)
3.接收的时候也可以是多个参数: return 'hello','world' x,y=('hello','world') 拆包
'''
