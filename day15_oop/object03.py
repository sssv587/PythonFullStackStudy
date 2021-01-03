# 类中方法：动作
# 种类：普通方法 类方法 静态方法 魔术方法

"""
普通方法格式：
def 方法名(self[,参数,参数]):
    pass
"""


class Phone:
    brand = 'xiaomi'
    price = 4999
    type = 'mate30'

    # Phone类里面的方法：call
    def call(self):
        print('----->', self)
        print('正在访问通讯录:')
        for person in self.address_list: # [{},{}]
            print(person.items())
        print('正在打电话.....')
        print('留言：', self.note)


phone1 = Phone()
print(phone1)
phone1.note = '我是phone1的note'
phone1.address_list = [{'123243435': '张三'}, {'211241343': '李四'}]
phone1.call()  # call(phone1) ----> self.note

phone2 = Phone()
print(phone2)
phone2.note = '我是phone2的note'
phone2.call()  # call(phone2) ----> self.note
