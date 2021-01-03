'''
str()
int()
len()
list()
sorted()
print()
input()
enumerate()

'''


# l1 = ['a','abc','jk','oppo']

# for index,value in enumerate(l1):
# 	print(index,value)

# for index,value in enumerate('happy'):
# 	print(index,value)


# 算法
# 冒泡排序

numbers = [5,4,3,2,1]
# numbers = sorted(numbers) 
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

# 自定义排序方法

for i in range(len(numbers)):
	for j in range(i+1,len(numbers)):
		if numbers[i] > numbers[j]:
			# 快速交换
			numbers[i],numbers[j] = numbers[j],numbers[i]
			print(numbers)
	print('------------> %d'%i)


# mylist = [4,7,1,0]

# for i in range(len(mylist)-1):
# 	# 每一轮的比较，注意range的变化，这里需要进行length-1长的比较，注意i的意义（可以减少比较已经排好序的元素）
# 	for j in range(len(mylist)-i-1):
# 		if mylist[j]>mylist[j+1]:
# 			mylist[j],mylist[j+1] = mylist[j+1],mylist[j]

# print(mylist)


# numbers = [5,4,3,2,1,2]

# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-i-1):
#         if numbers[j] > numbers[j+1]:
#             numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
#         print('------> %d'%j)
#     print('外层------> %d'%i)

# print(numbers)