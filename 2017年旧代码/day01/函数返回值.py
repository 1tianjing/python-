'''
#定义一个函数，叫asum，返回一个值
定义一个函数叫bsum,返回值是两个参数，其中一个参数为用户，另一个参数为asum
'''
def asum(a,b):
    a1 = a
    a2 = b
    a3 = a+b
    return a3
def bsum(a):
    a1 = a
    a2 = asum(1,2)
    return {'name1':a1,'name2':a2}
kj = bsum(2)
print('用户输入完的内容是%s最终的和为%s'%(kj['name1'],kj['name2']))
