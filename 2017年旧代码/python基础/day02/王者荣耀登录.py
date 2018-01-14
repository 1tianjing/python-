#王者荣耀登录页面
#注册，登录功能  注册：register  登录：login
#一、定义注册的函数
#1、先判断这个帐号存不存在，不存在就可以创建，如果存在，就不能创建
def register(a,b):
    #先要从本地文件里面取出所有的内容
    #open()    第一个函数是文件名  第二个参数是模式  模式：读  写   读写
    #r 读取内容  如果本地没有这个文件就会报错
    f = open('account.txt','r')
    #readlines() 可以取出所有数据，并且取到的数据是一个列表 
    account_list = f.readlines()
    #这是个容器，存放我们清洗干净的数据
    f.close()
    length = len(account_list)
    #如果文件里面没有内容，就不存在比较，直接开始随便添加，因为添加任何东西都不存在重复
    if length == 0:
        f = open('account.txt','w')
        f.write(a)
        f.close()
    else:
        #在这个else里面说明本地有内容，我们需要进行进一步的比较
        names = []
        for name in account_list:
             name = name.rstrip()
             names.append(name)
        #判断用户需要注册的帐号再本地有没有存在   如果存在  注册失败
        if a in names:
            print('登陆失败')
        else:
            print('可以注册')
            #重新打开这个文件   然后以追加的模式
            a = '\n'+a
            f = open('account.txt','a')
            f.write(a)
            f.close()
#二、定义登录的函数
#三、调用函数
a = input('请输入帐号')
register(a,1)

