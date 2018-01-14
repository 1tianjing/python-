try:
    print('----test--1----')
    open('123.txt','r')#如果123.txt文件不存在，那么会产生IOError异常
    print('----test--2----')
    print(num)#如果num变量没有定义，那么会产生NameError异常
except (IOError,NameError):
    #如果想通过一次except捕获到多个异常可以用一个元祖的方式
    #errorMsg里回报存捕获到的错误信息
    print(errorMsg)
