#之前说到函数内部操作行参的值，不会影响实参，在某些情况下是可以修改实参的
def modify(v):#修改列表的元素值
    v[0] = v[0]+1
    return v
a = [2]
print(modify(a))
print(a)

print('~'*30)
   
def modify2(v,item):#为列表增加元素
    v.append(item)
    return v
 
b = [4]
print(modify2(b,5))
print(b)

print('~'*30)

def mofidy3(c):#修改字典元素值为或者为字典添加元素
    c['age']=38

d = {'name':'李文浩','age':'18'}
print(d)











