print('欢迎来到召唤师峡谷！')
name = "wangzherongyao"
print(name.title())#首字母大写
print(name.upper())#全部字母大写


first_name="郑"
last_name="开州"
full_name=first_name+" "+last_name
print(full_name)
print('尊敬的召唤师:'+full_name+',欢迎来到召唤师峡谷！')


print("欢迎来到召唤师峡谷！")
print("\t欢迎来到召唤师峡谷！")#文本后缩进一个单位
print("\n欢迎来到召唤师峡谷！")#文本换行
msg = "  努力有用的话还要天才干甚？  "#文本前后有空格
print(msg)
msg = msg.strip() #移除了变量msg两端的空格
print(msg)

num = 2
msg1 = ("尊敬的召唤师，您在这局对战中的综合评分位于第"+str(num)+"位!")         
print(msg1)  

#创建一个列表
heros = ["安琪拉","李白","妲己","孙悟空"]  
print(heros) 
#修改索引所在的值            
heros[0] = "大乔"  
print(heros)     
#在列表末尾增加新元素
heros.append("兰陵王")    
print(heros) 
#在列表指定位置插入元素
heros.insert(0,"兰陵王") 
print(heros)  
#在列表中删除元素
#可调用删除
tail = heros.pop()
print(heros) 
print(tail)
#概念删除
del heros[0] 
print(heros)            

#定值删除
heros.remove("大乔")
print(heros)

#列表排序
#概念排序
heros.sort()
print(heros)
#反向排序
heros.sort(reverse=True)
print(heros)
#临时排序
print(sorted(heros))
print(heros)

#反向排列列表元素
heros.reverse()
print(heros)


#计算列表中元素的计数项
heros1 = ["大乔","貂蝉","妲己","李白"]
len(heros1)

#遍历列表
heros = ["大乔","貂蝉","妲己","李白"]
for a in heros:
    print("您的队伍中有此英雄:"+a)

#在循环中加入一些废话
for a in heros:
    print(a+"是一个优秀的英雄！"+"\n")

#使用range函数
for a in range(1,5):
    print(a)

num = list(range(1,6))
print(num)



#从外部添加数字到数字列表(计算平方值)
pingfangzhi=[]
for shuzi in range(1,11):
    pingfang = shuzi**2
    pingfangzhi.append(pingfang) 
print(pingfangzhi)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
