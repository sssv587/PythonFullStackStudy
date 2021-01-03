person = '大圣哥'
address = '北京市海淀区中关村智诚科技大厦4层'
phone = '1588588888'
num = 5

# '+' 符号 拼接   字符串 + 字符串 --> ok 字符串 + int --> TypeError
# print('订单的收件人是：'+ person + '收货地址是：'+ address + '联系方式是：'+ phone + '商品的数量是：' + num)


print('订单的收件人是：%s,收货地址是：%s,联系方式是：%s,商品的数量是：%s'%(person,address,phone,num))