# 魔术方法
# __init__:
# 触发时机:初始化对象时触发(不是实例化触发，但是和实例化在一个操作中)

# __new__:实例化的魔术方法
# 触发时机：在实例化对象时触发

# __call__:对象调用方法
# 触发时机:将对象当成函数使用的时候，会默认调用次函数中的内容

# __del__:delete的缩写 析构魔术方法
# 触发时机:当对象没有用(没有任何变量引用)的时候触发

class Person:
    def __init__(self, name):
        print('------->init', id(self))
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('------->new')
        postion = super(Person, cls).__new__(cls)
        print(id(postion), type(postion))
        return postion

    def __call__(self, *args, **kwargs):
        print('------>call', *args)


p = Person('jack')
p('hello0')
print(id(p))

