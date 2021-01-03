# student book computer
"""
知识点:
    1.has a
        一个类使用了另外一种自定义的类型
        student使用computer  book
    2.类型:
        系统类型:
            str int float
            list tuple dict set
        自定义类型:
            算是自定义的类,都可以将其当成一种类型
            s = Student()
            s是Student类型的对象
"""


class Computer:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def online(self):
        print('正在使用电脑上网...')

    def __str__(self):
        return self.brand + '\t' + self.type + '\t' + self.color


class Book:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def __str__(self):
        return self.bname + '\t' + self.author + '\t' + str(self.number)


class Student:  # has a
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)

    def borrow_book(self, book):
        for book1 in self.books:
            if book1.bname == book.bname:
                print('已经借过了!')
            else:
                # 将此参数添加到列表中
                self.books.append(book)
                print('添加成功!')

    def show_book(self):  # book就是一个book对象
        for book in self.books:
            print(book.bname)

    def __str__(self):
        return self.name + '\t' + str(self.computer) + '\t' + str(self.books)


# 创建对象
computer = Computer('mac', 'mac pro 2018', '深灰色')
book = Book('盗墓笔记', '南派三叔', 10)

stu = Student('sss', computer, book)
print(stu)

# 看借了哪些书
stu.show_book()

book1 = Book('鬼吹灯', '天下霸唱', 8)
stu.borrow_book(book1)

print('---------------------')

stu.show_book()
