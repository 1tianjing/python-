'''
王者荣耀的登录和注册
'''
#王者荣耀的注册
def register(account,password):
    #创建一个用于存储帐号的文件
    f = open('account.txt','w+')
    f.write(account)
    f.close()
    f2 = open('password.txt','w+')
    f2.write(password)
    f2.close()
#登录功能
def login(account,password):
    f = open('account.txt','r')
    b = f.readlines()
    f2 = open('password.txt','r')
    c = f2.readlines()
    if account == b[0]:
        if password == c[0]:
            print('登录成功')
    f.close()
    f2.close()
a = input('请输入帐号')
b = input('请输入帐号')
register(a,b)
login(a,b)
    
