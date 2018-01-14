'''
1、函数的定义
del 函数名()
    函数体-->可以理解为你要执行的代码片段
'''
#printInfo()--->函数的调用一定要放到声明定义后面
#demo 代码实例 例子
def printInfo():
    print('-'*30)
    print('人生苦短，我用python')
    print('-'*30)
   

def addsum(a,b):
    print(a+b)
   

while True:
    a = int(input('请输入数字1'))
    b = int(input('请输入数字2'))
    addsum(a,b)

