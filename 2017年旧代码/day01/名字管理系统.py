'''
#名字管理系统v1.0
1、添加一个新的名字
2、删除名字
3、修改名字
4、查询名字
'''
print('*'*25)
print('名字关系关系系统v1.0')
print('1、添加一个新的名字')
print('2、删除一个名字')
print('3、修改一个名字')
print('4、查询一个名字')
print('5、退出系统')
print('*'*25)
#2、要一个值来记录，记录用户输了什么 1 2 3 4 来决定我们后面的代码
name = []
while True:
    num = int(input('请在此输入你需要的功能'))
    print('num = %d'%num)
    if num == 1:
        name = input('请输入要添加的用户名')
        name.append(name)
        print('添加成功，当前的名字一共有%s'%names)
    elif num == 2:     
        name = input('请输入要删除的用户')
        names.remove(name)
        print('删除成功，当前还有%s'%names)
    elif num == 3:
        name = input('请输入要修改的用户')
        print('name = %s'%name)
        if name in names:
            nameIndex = names.index(name)
            name[nameindex] = input('请输入要修改的内容')
            print('修改之后的内容%s'%names)
    elif num == 4:
        find_name = input('请输入查询名字')
        if find_nmae in names:
            print('查到你要的人')
        else:
            print('查无此人')
    elif num == 5:
        break
    else:
        print('输入错误请重新输入')
