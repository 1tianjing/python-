#定义起始行
row = 0
#最大打印9行
while row <= 9:
    #定义起始行
    col = 1
    #最大打印row列
    while col <= row:
        #end = "",表示输出结束后，不换行
        #"\t"可以在控制台输出一个制表符，协助在输出文本时对齐
        print("%d*%d =%d"%(col,row,row*col),end="\t")
        #列数 + 1
        col += 1
    #一行打印完成的换行
    print('')
    #行数 + 1
    row += 1

