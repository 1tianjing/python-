'''
学生管理系统
必须使用函数，完成对称需的模块化
学员信息至少包括：姓名，年龄，学号
功能有 添加，删除，修改，查询，退出
'''
#要一个容器来装所有的信息
he_zi = []
#定义一个函数，这个函数只是为了输出横线
def printLine():
    #输出一条横线
    print('*'*40)
#添加
#addStudent
def tian_jia():
    name = input('请输入姓名')
    age = input('请输入年龄')
    num = input('请输入学号')
#需要把用户的信息包装起来存到列表里面
#创建一个字典
    xin_xi = {'姓名':name,'年龄':age,'学号':num}
#要把这一行信息存到名单里，就是把这个字典存到列表里面
    he_zi.append(xin_xi)
    printLine()
    print('现在的学生有%s'%he_zi)
    printLine()
#删除
#delete
def shan_chu():
    name = input('请输入你要删除的名字')
#遍历
#需要一个计数器
    count = 0
    for dic in he_zi:
        if dic['姓名'] == name:
            del he_zi[count]
        else:
        #print('查无此人')
            count += 1
    print('此时还有%s'%he_zi)
    printLine()
#修改
#change
def xiu_gai():
    #先输入要修改的内容
    name = input('请输入要修改的学员名字')
    count = 0
    for dic in he_zi:
        if dic['姓名'] == name:
            he_zi[count]['姓名']=input('请输入姓名')
            he_zi[count]['年龄']=input('请输入年龄')
            he_zi[count]['学号']=input('请输入学号')
        else:
            count += 1
    printLine()
    print('现在有哪些%s'%he_zi)
    printLine()

#查询
def cha_xun():
    for dic in he_zi:
        print('姓名%s\t年龄%s\t学号%s\t'%(dic['姓名'],dic['年龄'],dic['学号']))

#退出
def tui_chu():
    pass
tian_jia()
tian_jia()
shan_chu()
xiu_gai()
cha_xun()

