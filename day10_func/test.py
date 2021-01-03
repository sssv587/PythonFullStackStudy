s = {1, 3, 4, 5, 6, 7, 8}

for i in s:
    print(i)

for index, i in enumerate(s):
    print(index, i)

print(enumerate(s))
# <enumerate object at 0x000001AF33B65E08>


list1 = []
index = 0
for i in s:
    t1 = (index, i)
    list1.append(t1)
    index += 1

print(list1)

for index, value in list1:
    print(index, value)


# 复用
def enumerate_s(value1):
    list2 = []
    index2 = 0
    for j in value1:
        t2 = (index2, j)
        list2.append(t2)
        index2 += 1
    print(list2)


s1 = {1, 2, 3, 4, 5, 6, 7}
enumerate_s(s1)

list1 = [1, 2, 3, 4, 5, 6]
list2 = list1
list1.remove(5)
print(list2)
