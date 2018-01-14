'''
淘宝系统管理
1、注册
2、登录
3、添加
4、查询
5、修改
6、删除
7、退出
'''
print('*'*40)
print('淘宝系统功能')
print('1、注册')
print('2、登录')
print('3、添加一个帐号')
print('4、查询帐号')
print('5、修改帐号')
print('6、删除一个帐号')
print('7、退出系统')
print('*'*40)


#登录
#要有一个列表，来存储用户输入的帐号和密码
account_list = []

#先定义函数

def longi(account='tianjing',passwd='123456'):
    '''登录'''
    print('登录')
    account = input('请输入你的帐号')
    passwd = int(input('请输入你的密码'))  
    #遍历
    for dic in account_list:
    #先判断用户输入的帐号是否和系统中的帐号一致
        if account == dic['name']:
    #进入到这里说明帐号正确
            if dic['passwd'] == passwd:
    #判断密码是否正确
                print('登录成功')
            else:
                print('密码错误')
        else:
            print('帐号错误')
    print('请重新输入')    

#注册    
def register(zhanghao = '123',mima = '456'):
    '''注册''' 
    print('注册')
    #先遍历
    for dic in account_list:
        if dic['name'] == zhanghao:
            print('帐号已被占用')
        else:
            #创建临时字典
            tempDic = {}
            tempDic['name'] = zhanghao
            tempDic['passwd'] = mima
            account_list.append(tempDic)
            #把字典添加到列表列里面
            print('帐号创建成功')
            break
    print('-'*40)
    while True:
        print('-'*40)
        print('淘宝')
        print('1、设置昵称')  
        print('2、设置年龄') 
        print('3、设置收货地址')  
        print('4、进入购物车') 
        print('5、进入收藏夹')
        print('6、进入关注的店铺')
        print('7、寻找宝贝')
        she_zhi = int(input('请输入你要选择的功能'))   
        if she_zhi == 1:
        #设置你的昵称
            ni_cheng = input('请输入你的昵称')
        elif she_zhi == 2:
        #设置你的年龄
            age = input('请输入你的年龄')
        elif she_zhi == 3:
        #设置你的收货地址
            addr = input('请输入你的收货地址')
        elif she_zhi == 4:
        #进入你的购物车
            shopping_cart = int(input('是否进入你的购物车,1为是，2为否'))
            if shopping_cart == 1:
                print('进入你的购物车')
            else:
                print('退出')
        elif she_zhi == 5:
        #收藏夹
            favorite = int(input('是否进入你的收藏夹，1为是，2为否'))
            if favorite == 1:
                print('进入你的收藏夹')
            else:
                print('退出')
        elif she_zhi == 6:
        #店铺
            shop = int(input('是否进入你关注的店铺，1为是，2为否'))
            if shop == 1:
                print('进入你关注的店铺')
            else:
                print('退出')
        elif she_zhi == 7:
        #寻找宝贝
            find_baby = int(input('是否搜索宝贝，1为是，2为否'))
            if find_baby == 1:
                print('开始搜索宝贝')
            else:
                print('退出')
        else:
            break
            print('退出')
    print('-'*40)
account = input('请输入帐号')
passwd = input('请输入密码')

#添加账号
def add_account():
    print('添加帐号')
    account = input('请输入你要添加的帐号')
    passwd = input('请输入密码')
    #创建一个字典
    zhmm = {'帐号':account,'密码':passwd}
#把这个存到列表里面
    account_list.append(zhmm)
    print('现在的账户有%s'%account_list)
# 查询账户   
def cha_xun():
    print('查询')
    #遍历
    for dic in account_list:
        print('帐号%s\t密码%s\t'%(dic['帐号'],dic['密码']))
#修改
def xiu_gai():
    #先输入要修改的内容
    print('需要修改的内容')
    account = input('请输入要修改的内容')
    count = 0
    #遍历
    for dic in account_list:
        if dic['帐号'] == account:
            account_list[count]['帐号'] = input('请输入帐号')
            account_list[count]['密码'] = input('请输入密码')
        else:
            count += 1
    print('现在有哪些账户%s'%account_list)

#删除账户
def shan_chu():
    #先输入你要删除的帐号
    print('要删除的帐号')
    account = input('请输入你要删除的帐号')
    #遍历
    #要一个计数器
    count = 0
    for dic in account_list:
        if dic['帐号'] == account:
            del account_list[count]
        else:
            count += 1
    print('此时账户还有%s'%account_list)
#退出
def exit():
    print('退出')
    print('~'*40)
#调用函数
longi()
register()
add_account()
cha_xun()
xiu_gai()
shan_chu()
exit()
print('亲，不打算再看看吗？')
name = int(input('不打算看看嘛 1为同意，2为拒绝'))
if name == 1:
    print('继续查找宝贝')
else:
    print('残忍拒绝')
