def func():
    print('---------循环导入2里面的func1----------')
    from recall_import1 import task1
    task1()
    print('---------循环导入2里面的func2----------')