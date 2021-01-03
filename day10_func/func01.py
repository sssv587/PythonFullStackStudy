# 可变参数


# def add(a, b):
#     pass


# 定义方式:
# def add(*args):  # arguments 参数
#     # print(args)]
#     sum_1 = 0
#     if len(args) > 0:
#         for i in args:
#             sum_1 += i
#         print('累加和是:', sum_1)
#     else:
#         print('没有值可计算 sum:', sum_1)
#
#
# add()  # ()空元组
# add(1)  # (1,)
# add(1, 2, 3, 4, 5, 6)


def add(name, age, *args):  # name,*args = '飞飞', 4, 6, 8
    print(name, age, args)
    sum_1 = 0
    if len(args) > 0:
        for i in args:
            sum_1 += i
        print('%s累加和是:%s' % (name, sum_1))
    else:
        print('没有值可计算 sum:', sum_1)


# 调用
add('飞飞', 4, 6, 8)

add('阿文', 10)  # name, age, *args='阿文', 10

# a,*b = 1,2,3,4,5,6

# 注意：可变参数必须放在后面：name,*args
