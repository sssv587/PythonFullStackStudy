"""
基础:
. 任意字符
[] 范围
| 或者
() 一组

量词:
    * >=0
    + >=1
    ? 0,1
    {m} =m
    {m,} >=m
    {m,n} m<= <=n

预定义:
    \s space
    \S not space
    \d digit
    \D not digit
    \w word [0-9a-zA-Z_]
    \W not word [^0-9a-zA-Z_]
    \b
    \D

分组:
() ----> group(1)

1.number
 (\w+)(\d*) ---> group(1) group(2)
 引用:
 (\w+)(\d*)  \1 \2 表示引用前面的内容

2.name
 (?P<name>\w+) (?P=name)

 非贪婪
 * ? + {m,n} 后面加上?变成非贪婪
"""

import re

# 默认是贪婪的,如果想将贪婪模式变成非贪婪模式
msg = 'abc123abc'
result = re.match(r'abc(\d+?)',msg)
print(result)

msg = '<img class="BDE_Image" src="http://tiebapic.baidu.com/forum/w%3D580/sign=a882e696a5fb43161a1f7a7210a54642/86ca0d2442a7d9335d7a622eba4bd11372f00112.jpg" size="137223" changedsize="true" width="560" height="265">'
result = re.match(r'<img class="BDE_Image" src="(.+?)"',msg)
# print(result.group(1))
image_path = result.group(1)

import requests
response = requests.get(image_path)
with open('aa.jpg','wb') as wstream:
    wstream.write(response.content)