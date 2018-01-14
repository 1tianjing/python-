'''
王者荣耀终极版v2.0
1、功能提示，提示你这个系统有哪些功能
2、开始业务逻辑
3、退出
'''
wzry_gnts = '王者荣耀系统功能提示'
print(wzry_gnts.center(30))
print('*'*30)
print('功能1：%s\n功能2：%s\n'%('注册','登录'))
print('*'*30)
#需要一个列表来存储用户输入的帐号和密码
account_list = []
#要写两个按钮，这两个按钮就是两个函数
def login(account = 'libai',passwd = '123456'):
    '''登录'''
    #print('登录')
    for dic in account_list:
        if account == dic['name']:
            if dic['passwd'] == passwd:
                print('登录成功')
            else:
                print('密码错误')
        else:
            print('帐号输入错误')
def register(zhanghao = '小王',mima = '123456'):
    '''注册'''
    for dic in account_list:
        if dic['name'] == zhanghao:
            print('您的账号已被占用')
        else:
            #创建一个临时字典
            tempDic = {}
            #把用户输入的帐号存储到字典
            tempDic['name'] = zhanghao
            #把用户输入的密码存储到字典
            tempDic['passwd'] = mima
            print('帐号创建成功')
            break
print('-'*40)
account = input('请输入帐号')
passwd = input('请输入密码')


print('-'*40)
