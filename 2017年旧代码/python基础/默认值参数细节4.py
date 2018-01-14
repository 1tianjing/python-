#多次调用函数并且不为默认值参数传递值时，默认值参数只在第一次调用时进行解释，对于列表、字典这样的可变类型的默认值参数，这一代你可能会导致很严重的逻辑错误，而这种错误会耗费大量的时间和精力再排错上
def demo(newitem,old_list=[]):
    old_list.append(newitem)
    return old_list
def printLine():
    print('~'*30)
print(demo('5',[1,2,3,4]))
printLine()
print(demo('aaa',['a','b']))
printLine()
print(demo('a'))
printLine()
print(demo('b'))
  

print('~'*30)
#上面函数使用列表作为默认参数，由于其可记忆性，连续多次调用该函数而不给该函数传值时，再次调用时将保留上次调用结果，导致很难发现错误，下面代码可以解决这个问题
def demo2(newitem,oldd_list=None):
    if old_list is None:
        old_list=[]
    old_list.append(newitem)
    return old_list
