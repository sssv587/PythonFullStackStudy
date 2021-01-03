# 找出列表的最大值

# 自己封装一个求最大值的函数

def max_collection(iterable):
    max_num = iterable[0]
    for i in iterable:
        if i > max_num:
            max_num = i
    print('最大值是:', max_num)


# 调用：测试是否能找出最大值
list1 = [4, 1, 3, 4, 6, 7, 8, 0]
max_collection(list1)

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 98)
max_collection(tuple1)

#  sort min reverse
#  type(iterable)
print(type(tuple1) == tuple)  # 查看是什么类型

# 判断是不是什么类型：isinstance(变量,类型关键字)
print(isinstance(2, int))  # 返回值是False、True

if isinstance(tuple1, tuple):
    print('不能翻转和排序!')