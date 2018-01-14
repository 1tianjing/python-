'''
王者荣耀正式版v1.0
1、功能提示，提示你这个系统有哪些功能
2、开始业务逻辑
3、退出
'''
wzry_gnts = '王者荣耀功能提示'
print(wzry_gnts.center(30))
print('*'*40)
print('功能1:%s\n功能2:%s\n'%('注册','登录'))
print('*'*40)

#需要一个数组，来存储用户要输入的账号和密码
#account_list
account_list = []

#写两个按钮，这个两个按钮就是两个函数

def longi(account='libai',passwd='123456'):
    '''登录'''
    print('登录')
    for dic in account_list:
        if account == dic['name']:
            # 进入这里，说明帐号正确，现在需要判断密码对不对
            if dic['passwd'] == passwd:
                print('登录成功')
            else:
                print('密码错误')
        else:
            print('帐号输入错误')
def register(zhanghao = '何志国',mima = '123456'):
    '''注册'''
    print('注册')
    for dic in account_list:
        if dic['name'] == zhanghao:
            print('帐号已经被占用')
        else:
        #创建一个临时字典
            tempDic = {}
            tempDic['name'] = zhanghao
            tempDic['passwd']= mima
            account_list.append(tempDic)
            print('帐号创建成功')
            break
print('-'*40)
account = input('请输入帐号')
passwd = input('请输入密码')


print('-'*40)
