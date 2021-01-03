# 匿名函数：简化函数定义
# 格式： lambda  参数1,参数2... : 运算

# def func():
#     print('aaaa')
#
#
# def add(a, b):
#     s = a + b
#     return s

s = lambda a, b: a + b  # <----> def add(a,b):return a+b
print(s)  # s就是一个函数function

s1 = lambda x, y: x * y
print(s1(3, 5))


# 匿名函数作为参数出现
def func(x, y, func):
    print(x, y)
    print(func)
    print(func(x, y))


# 调用func
func(1, 2, lambda x, y: x + y)

# 匿名函数与内置函数的结合使用：
# max sorted zip...

list1 = [1, 5, 3, 6, 8, 2, 45]
m = max(list1)
print('列表的最大值:', m)

list2 = [{'a': 10, 'b': 20}, {'a': 13, 'b': 23}, {'a': 19, 'b': 22}]
result = max(list2, key=lambda x: x['a'] + x['b'])
print('列表的最大值:', result)
