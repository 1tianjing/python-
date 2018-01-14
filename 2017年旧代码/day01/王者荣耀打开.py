'''
王者荣耀
'''
#你要打开游戏，要先下载，手机上面要先有存在这个游戏的开关
zhang_hao_and_mi_ma = {}
#登录按钮
def wzry_deng_lu(zh,mm):
    for zh_1,mm_1 in zhang_hao_and_mi_ma.items():
        if zh == zh_1:
            if mm ==mm_1:
                print('登录成功') 
            else:
                print('密码错误')
        else:
            print('帐号错误')  
    print('3、登录成功')
def wzry():
    print('1、打开王者荣耀')
#假设你打开游戏后，有一个注册按钮
def wzry_zhu_ce():
    zhanghao = input('请输入帐号')
    mima = input('请输入密码')
    if zhanghao in zhang_hao_and_mi_ma.values():
        print('对不起，帐号已被占用')
    else:
        zhang_hao_and_mi_ma['zhang_hao'] = zhanghao
        zhang_hao_and_mi_ma['mi_ma'] = mima
        print('帐号注册成功，请登录')
        wzry_deng_lu(zhanghao,mima)
    print('2、注册按钮')
#1、打开王者荣耀
wzry()
#2、注册王者荣耀
wzry_zhu_ce()
#3、登录王者荣耀
#wzry_deng_lu
