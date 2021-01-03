# dictionary 字典

'''
应用：
貂蝉 ---> ['屠龙刀','手榴弹'] 800
诸葛亮 ---> ['鹅毛扇','碧血剑','98k'] 300

字典：
特点：
1.符号：{}
2.关键字：dict
3.保存的元素是：key:value


列表   元祖    字典
[]     ()      {}
list   tuple  dict
ele    ele     kv

element 元素
'''



# 定义
dict1 = {}  # 空字典
 
dict2 = dict()  # 空字典  list = list()  空列表   tuple1 =  tuple() 空元祖


dict3 = {'ID':'212141241240','name':'lucky','age':18} # ['124141341','lucky',18]


# dict4 = dict(('name','lucky'))  # {'name':xxx,'lucky':xxx}
# print(dict4)

dict4 = dict([('name','lucky'),('age',18)]) # 'name': 'lucky', 'age': 18
print(dict4)

# dict5 = dict([('name','lucky',1),('age',18,3)]) # ValueError: dictionary update sequence element #0 has length 3; 2 is required
# print(dict5)


# 注意事项：list可以转成字典 但是前提：列表中的元素都要成对出现

# 字典的增删改查：

# 增加：格式：dict6[key] = value
# 特点：按照上面的格式，如果在字典中存在同名的key，则发生值的覆盖（后面的值覆盖原来的）
# 如果没有同名的key，则实现添加功能(key:value添加到字典中)

dict6 = {}

#

dict6['brand'] = 'huawei' # {'brand','huawei'}

print(dict6)

dict6['brand'] = 'mi'

dict6['type'] = 'p30 pro'

dict6['price'] = 9000

dict6['color'] = '黑色'

print(dict6)