'''
王者荣耀
'''
wzry_list = [{'name' : '123','passwd' : '456'}]
while True:
    print('1是登录，2是注册， 3是退出')
    denglu_zhuce =int(input('请输入你要选择的序号'))
    def zhuce():
        name = input('请输入你要注册的帐号名')
        list_zhanghao = []
        for dice in wzry_list:
            list_zhanghao.append(dice['name'])
        if name in list_zhanghao:
            print('帐号已存在，请登录')
        elif name not in list_zhanghao:
            passwd = input('请输入密码')
            dice = {}
            dice['name'] = name
            dice['passwd'] = passwd
            wzry_list.append(dice)
            print('注册成功')
    def denglu():
        name = input('请输入你的帐号')
        for dice in wzry_list:
            list_zhanghao = []
            list_zhanghao.append(dice['name'])
        if dice not in list_zhanghao:
            print('帐号不存在，请先注册')
        elif name in list_zhanghao:
            mima = int(input('请输入密码'))
            i = 0
            length = len(wzry_list)
            dic = {}
            while i <= length -1:
                dic = wzry_list[i]
                if dic['name'] == name:
                    zmima = int(dic['passwd'])
                    break
                else:
                    i += 1
                    dic = {}
                if mima == zmima:
                    print('登录成功')
        else:
            print('密码错误')
    if denglu_zhuce == 1:
        denglu()
    elif denglu_zhuce == 2:
        zhuce()
    elif denglu_zhuce ==3:
        print('..')
        break
