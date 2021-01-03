# + - * / 算术运算符
# 扩展的算术运算符： ** // %

a = 9
b = 2

result = a * b
print('乘法运算：',result)

result = a / b
print('除法运算：',result)

b = 2
result = a ** b # b = 2 8 * 8 = 64  8 * 8 * 7 = 512
print('乘方运算：',result)


result = a // b # 整除 9/2 = 4.5 取整：4
print('整除运算：',result)


result = a % b # 9 % 2 = 1
print('取余数运算：',result)