try:
    print('test1')
    open('123.txt','r')
    print('test2')
except IOError:
    pass
