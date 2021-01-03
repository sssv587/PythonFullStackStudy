import re

msg = '佟丽娅娜扎热巴黛丝'
pattern = re.compile('佟丽娅')
result = pattern.match(msg)  # 没有匹配
print(result)

# 使用正则re模块方法：match
s = '娜扎热巴黛丝佟丽娅'
result = re.match('佟丽娅', s)  # 只要从开头进行匹配,如果匹配不成功则就返回None
print(result)

result = re.search('佟丽娅', s)  # search进行正则字符串匹配方法,匹配的是整个字符串
print(result)

print(result.span())  # 返回位置

print(result.group())  # 使用group提取到匹配的内容
print(result.groups())

# a2b h6k
# [] 表示的是一个范围

s = '哈哈8u'

result = re.search('[0-9][a-z]', s)
print(result)

msg = 'abvd6sadasd7adaxc8dfg'

result = re.search('[a-z][0-9][a-z]', msg)  # search 只要有匹配的后面就不会继续进行检索，找到一个匹配的就会停止
print(result.group())

result = re.findall('[a-z][0-9][a-z]', msg)  # findall 匹配整个字符串，找到一个继续向下找一直到字符串结尾
print(result)

# 正则符号
# a7a a88a a7878a
msg = 'abvd6sadasd78daxc889dfg'
result = re.findall('[a-z][0-9]+[a-z]', msg)
print(result)

# qq号码验证:5-11位 开头不能是0
qq = '4457444789'
result = re.match('^[1-9][0-9]{4,10}$', qq)
print(result)

# 用户名可以是字母或数字或者_，不能是数字开头，用户名长度必须6位以上[0-9a-zA-Z]
username = 'admin001'
result = re.match('^[a-zA-Z][0-9a-zA-Z]{5,}$', username)
print(result)

result = re.search('^[a-zA-Z_]\w{5,}$', username)
print(result)

msg = 'aa.py ab.txt bb.py kk.png uu.py apyb.txt'
result = re.findall(r'\w*\.py\b', msg)
print(result)

"""
   总结:
   . 任意字符除(\n)
   ^ 开头
   $ 结尾
   [] 范围 [abc] [a-z] [a-z*%#]
   
   正则预定义:
   \s   空白(空格)
   \b   边界
   \d   数字
   \w   word [0-9a-zA-Z_]
   
   大写反面 \S 非空白 \D 非数字
   
   '\w[0-9]' ----> \w [0-9] 只能匹配一个数字
   
   量词:
   * >= 0
   + >= 1
   ? 0,1
   
   手机号码正则
   re.match('^1[3456789]\d{9}',phone)
   
   {m}:固定m位
   {m,}:>=m位
   {m,n}:phone >= m phone<=n
   
"""
