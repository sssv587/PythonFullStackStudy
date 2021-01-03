def func(a, *args, **kwargs):
    print(a, args, kwargs)


t = (1, 2, 3, 4)
func(1, t)  # 1 ((1, 2, 3, 4),) {}

l = [2, 5, 8]
func(*l, 1, c=9, b=6)  # 2 (5, 8, 1) {'c': 9, 'b': 6}
dict1 = {'1': 'qwe', '2': 'wed'}
func(*l, 1, **dict1)  # 2 (5, 8, 1) {'1': 'qwe', '2': 'wed'}