#注册的函数
def register(account,password):
    #打开文件
    f = open('account.txt','r')
    #读取内容
    account_list = f.readlines()
    #本地的帐号我已经取出来了，然后要判断本地的帐号有没有，如果本地是一个空白的文件，什么都没有，那么意味着我们可以随便创建帐号都不会重复
    length = len(account_list)
    f.close()
    if length == 0:
        print('可以创建帐号')
        f = open('account.txt','w')
        f.write(account)
        f.close()
    else:
        names = []
        for name in account_list:
            names.append(name.rstrip())
        if account in names:
            print('帐号已经存在')
        else:
            #在这里可以创建帐号
            f = open('account.txt','a')
            #字符串拼接
            account = '\n'+account
            f.write(account)
            f.close()
            account = account.lstrip()
            login(account,10)
#登录的函数
def login(account,password):
    #以只读的方式打开文件
    f = open('account.txt','r')
    account_list = f.readlines()
    #先看看本地有没有帐号，如果没有就直接告诉用户输入失败
    #len(account_list)
    names = []
    for name in account_list:
        names.append(name.rstrip())
    if account in names:
        print('登录成功')
    else:
        print('登陆失败')
account = input('请输入帐号')
register(account,10)
    
