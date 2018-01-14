#偷玩王者荣耀升级版 1.老师来了，就藏手机，老师走了，继续玩
#首先我要确定我是目前在第几杀 
count = 0
#还要一个报耳神  告诉我班主任有没有来
banzhu = 0#表示班主任有没有来1表示来了
#首先要判断 我的游戏有没有正在进行（你如果没有输或者没有赢）
while count<=5 and banzhu !=1:
    print('目前在第%d杀'%count)
    #判断班主任来了没有
    banzhu = int(input('班主任来了没'))
    if banzhu == 1:
        print('挡在第%d杀的时候，班主任来了'%count)
        banzhu = 0
        continue#中断一次循环
 #    banzhu = 0
 #    每一次循环我都要增加一杀
    count += 1
if count>=5:
    print('游戏胜利')
else:
    print('游戏结束')

