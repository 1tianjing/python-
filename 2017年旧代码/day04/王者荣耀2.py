#王者荣耀 当我们开始杀敌的时候，第一杀，第二杀都正常进行，到了第三杀得时候，班主任来了
#首先要有一个东西 记录我是到了第几杀
i = 0
#监视器：耳报神  1表示班主任来了 0表示班主任在场
banzhu = 0
#判断有没有五杀，如果没有五杀，继续杀，直到5杀为止
while i<=5:
    print('目前是第%d杀'%i)
    banzhu = int(input('班主任来了没'))
    #班主任来了，我就要停止游戏了
    #所以这时候我要进行一个判断  判断班主任有没有来
    if banzhu == 1:
        break #完全停止，跳出循环
#假设班主任一直没有来
    i = i+1 #i+=1
if i>=5:
    print('游戏结束了')
else:
    print('手机被没收了')
