# 位运算

# 二进制： 0 1
'''

8   4   2   1


'''
a = 3

print(bin(a))  # 0b 11

a = 13

print(bin(a))

b = 0b10111  # 0b 二进制   二进制的表示:0b100101

print(b)

print(int(b))


# 1 byte = 8 bit    8个二进制位等于1个字节

c = -8  # -0b1000    0000 1000

print(bin(c))



c = 0o6430  # 0o 开头的都是八进制    里面的数字不能超过8

print(int(c))


# 开头表示0x   0-9 a-f
# 应用： FFFFFF   000000  FF0000  00FF00 表示颜色等

d = 0x9ab16


print(int(d))


'''
&
|
~
^
<<
>>
'''

print(3 & 2)
'''
  0000 0011
& 0000 0010
------------
  0000 0010

  | 类似 or
'''

print(5 | 3)

print(~5)  # 取反  将十进制的数字对应的二进制进行取反操作
'''
 0000 0101
取反：
 1111 1010

看第一位(第一位是符号位，只要第一位为1的就是负数，第一位是0的就是正数)

-6
 0000 0110
 1111 1001  反码
 1111 1010  补码
'''



# 异或  ^   相同的是0，不同的是1

print(3^5)  

'''
1.左边的数字转成二进制
2.右边的数字转成二进制
3.对齐，上下进行比较(相同的是0，不同的是1)
4.将计算的结果转成十进制


3   0000   0011
5   0000   0101
----------------
    0000   0110   -->  6

'''




# 左移
print(2<<1) # 4

print(2>>1) # 1

'''
2的二进制:

0000 0010

左移(低位补0): m << n   m * 2的n次方
右移(高位补原最高位): m >> n   m//2的n次方
'''

print(16<<2) # 64

print(16>>2) # 4