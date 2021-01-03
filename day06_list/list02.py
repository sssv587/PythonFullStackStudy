# 增删改

brands = ['hp','dell','thinkpad','支持华为','lennovo','mac','神州']

# 改
# print(brands)

# print(brands[-1])


brands[-1]='HASEE' # 赋值   步骤:1.找到(使用下标) 2.通过=赋值 3.新的覆盖原有的
# print(brands)


# HUAWEI

# for brand in brands:
# 	if '华为' in brand:
# 		brand = 'HUAWEI'

# print(brands)

for i in range(len(brands)):
	# i是1,2,3,4... 下标
	if '华为' in brands[i]:
		brands[i] = 'HUAWEI'
		break

# print(brands)



# 删除 del 是delete的缩写
# del brands[2]
# print(brands)


# 删除  只要是 hp mac 都要删除
# for i in range(len(brands)):
# 	if 'hp' in brands[i] or 'mac' in brands[i]:
# 		del brands[i]

for brand in brands:
		if 'hp' in brand or 'mac' in brand:
			brands.remove(brand)

print(brands)

# print(brands)

# l = len(brands)
# i=0
# while i < l:
# 	if 'hp' in brands[i] or 'mac' in brands[i]:
# 		del brands[i]
# 		l -= 1
# 		print(brands)
# 		print('---->',l)
# 	print(brands[i])
# 	i+=1
# 	print(i)

# print(brands)


'''
They are student
yews