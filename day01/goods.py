# 变量的命名规则
a = 10
b = 20
c = 30
print(a,b,c)


# 不规范
# 原则：见名知意

# 由字母 数字 不能以数字开头
# 严格区分大小写
# 不能使用python的关键字
# 查看python有哪些关键字
# 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
# 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
# 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'

A = 30
print(A)
print(a,A)

name01 = '张三'
print(name01)

name_01 = '李四'
print(name_01)

_name01 = '王五'
print(_name01)

# 99n = 'abc'  invalid syntax
# print(99n)

# name 01 = 'abc' 错误的命名
# print(name 01)

# 建议：
# 驼峰式
# getName payMoney
# 如果一个名字是由多个单词组成的，则除第一个单词之外以后的每个单词的首字母大写
# getElementsByName
# getElementsById

# 类：GetName 如果定义类名，每个单词的首字母大写
# 下划线式：
# Python中变量的，函数命名：
# get_name(python推荐) ~ getName
# pay_money(python推荐)


goods_num = 10
good_total = 289.9
print('商品数量是：',goods_num)
print('商品的总额是：',good_total)