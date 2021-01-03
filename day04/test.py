# 补充:
sum=0

for i in range(1,51): # 0 ~ 49
	b=0
	b+=i

	if i%2==0:
		sum+=i

print('sum=',sum)
print('完成for循环之后i的值是:',i)
print('b=====>',b)


'''
目的:
1.声明变量的位置:声明在for，while的外层，sum+=i 相当于累加，如果放在for、while循环的内部，相当于每次循环都会执行sum=0

2.python 在for、while循环中没有变量的作用域，在for、while循环结构的外层都可以获取值

'''

'''
break,continue 跳转语句:

'''

# 方式一:
sum=0 
for i in range(10):
	if i%3!=0:
		sum+=i
print('sum0------1111',sum)

# 方式二:
sum=0

for i in range(10):
# 任务1
	if i%3==0:
		# pass break continue 
		# break # 跳出整个for循环结构
		# pass  # 什么都不管继续执行
		# continue # 跳出本次循环
		continue
	sum+=i
print('sum0------2222',sum)


