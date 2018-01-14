#默认值参数可以使用函数名__defaults__,随时查看函数所有默认值参数的当前值，其返回值为一个元组，其中元素依次表示所有默认值参数的当前值
def say(message,times=1):
    print((message+'')*times)
#可以使用default来查看函数参数的默认值，前提是该函数有默认值参数

#say.__defaults__

say.__defaults__#会返回一个元组
print('~'*30)
#调用该函数的时候，如只为message传递值，times的默认值还是2  如果message都传值，则默认值不再是1  而是使用调用的显示传递值
say('hello')
print('~'*30)
say('world\n',7)

