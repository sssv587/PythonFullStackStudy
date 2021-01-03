# 加密算法:md5  sha1 sha256...
import hashlib

msg = '我是一只皮卡丘!'
md5 = hashlib.md5(msg.encode('utf-8'))

print(md5.hexdigest())  # 32位 69668ba167ab27f70e1ba1862a819b88

sha1 = hashlib.sha1(msg.encode('utf-8'))
print(sha1.hexdigest())  # 40位

sha256 = hashlib.sha256(msg.encode('utf-8'))
print(sha256.hexdigest())  # 64位

password = '123456'

list1 = []

sha256 = hashlib.sha256(password.encode('utf-8'))
list1.append(sha256.hexdigest())

pwd = hashlib.sha256(input('输入密码:').encode('utf-8')).hexdigest()

for i in list1:
    if pwd == i:
        print('登陆成功!')
