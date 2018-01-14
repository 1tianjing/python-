f = lambda a,b,c:a+b+c
print(f(1,2,3))
r = lambda a,b,c:a*b*c
print(r(1,2,3))
e = lambda a,b,:(a+b)/2
print(e(2,3))
sum = lambda arg1,arg2:arg1+arg2
#调用sum函数
print"Value of total :", sum(10,20)
print"Value of total :", sum(20,20)
