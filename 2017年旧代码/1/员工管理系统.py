'''
阿里巴巴员工内部系统
1、新员工入职：姓名，公号，年龄，工作岗位，每月薪水，入职日期
2、查询：入职信息，该员工截止到目前为止所得工资（即金天的日期减去员工入职的日期），员工每月工资多少除以天数，那么员工工作了多少天就多少天的工资，如果员工走了，需要在系统中清除数据
'''
a = []
b = []
for dic in a:
    b.append(c['姓名'])
#添加
def tian_jia():
    c = {}
    name = input('请输入你的姓名')
    age = input('请输入你的年龄')
    sex = input('请输入你的性别')
    num = int(input('请输入你的工号'))
    gang_wei = input('请输入你的岗位')
    money = float(input('请输入你的薪水'))
    data = input('请输入你的入职日期')
    c['姓名'] = name
    c['年龄'] = age
    c['性别'] = sex
    c['工号'] = num
    c['岗位'] = gang_wei
    c['薪水'] = money
    c['入职日期'] = data
    b.append(name)
    a.append(c)
    print('添加成功')

    

