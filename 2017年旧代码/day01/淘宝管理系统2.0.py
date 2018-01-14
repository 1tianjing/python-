'''
淘宝管理系统
先进入淘宝app
'''
print('淘宝')
tao_bao = [{'account':'123','passrd':'456'}]
while True:
    print('淘宝')
    print('-'*40)
    print('淘宝系统功能')
    print('1、注册帐号')
    print('2、登录帐号')
    print('3、退出淘宝')
    print('-'*40)
    tao_bao = int(input('请输入你要选择的功能序号'))
    #定义一个函数
    def zhu_ce():
        account = input('请输入你要注册的帐号：')
        list_account = []
        #注册的用户不能一样
        for dic in tao_bao:
            list_account.append(dic['account'])
        if account in list_account:
            print('帐号已存在，请你直接登录')
        elif account not in list_account:
            passrd = input('请输入你要注册的密码')
            #创建的帐号信息保存到一个字典里面
            dic = {}
            dic['帐号'] = account
            dic['密码'] = passrd
            tao_bao.append(dic)
            print('注册成功')
    def deng_lu():
        account = input('请输入帐号')
        #要先判断是否存在
        for dic in tao_bao:
            list_account = []
            list_account.append(dic['account'])
        if account not in tao_bao:
            print('你输入的帐号不存在，请重新输入')
        elif account in tao_bao:
            passrd = int(input('请输入密码'))
            i = 0
            length = len(tao_bao)
            dic = {}
            while i <= lendth -1:
                dic = tao_bao[i]
                if dic['account'] == account:
                    passrd = int(dic['passrd'])
                    break
                else:
                    i += 1
                    dic = {}
            if passrd == passrd:
                print('进入淘宝')
                print('-'*40)
                while True:
                    print('1、设置昵称') 
                    print('2、设置年龄')
                    print('3、设置收货地址')
                    print('4、添加收货地址')
                    print('-'*40)
                
                
                    #功能选项
                    
                    she_zhi = int(input('请输入你选择的选项'))
                    #设置昵称
                    if she_zhi == 1:
                        ni_cheng = int(input('请输入你的昵称'))
                        print('昵称')
                    #设置年龄
                    elif she_zhi == 2:
                        age = int(input('请输入你的年龄'))
                        print('age')
                    #设置收货地址
                    elif she_zhi == 3:
                        addr = str(input('请输入收货地址'))
                        print('addr')
                    #添加收货地址
                    elif she_zhi == 4:
                        add_addr = str(input('请输入添加的收货地址'))
                        print('add_addr')
                    else:
                        print('退出')
                        break
                else:
                    print('密码错误')
    if tao_bao == 1:
        zhu_ce()
    elif tao_bao == 2:
        deng_lu()
    elif tao_bao == 3:
        print('退出')
        break
















