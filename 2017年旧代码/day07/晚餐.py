#创建一个列表，邀请三个人
yaos = ['康俊','陈怀勇','翠花']
#请他们来共进晚餐
for name in yaos:
    print('你好，来我家吧%s,我家没人'%name)
print('%s不能来赴约了'%yaos[2])
print('----------------------------')
yaos[2] = input('请输入你想邀请的嘉宾')
i = 0
while i < len(yaos):
    print('请来我家与我共进晚餐吧%s'%yaos[i])
    i += 1
print('我找到了更大的餐桌，因此我可以再邀请三位嘉宾')
print('----------------------------')
#列表添加元素
yaos.insert(0,'王润泽')
#定义一个变量
center = int(len(yaos)/2)
#待定
yaos.insert(center,'·庞源松')
yaos.append('李文浩')
print(yaos)
#把列表转化为字符串
#把字符串进行增删改查的操作（根据某一个符号分隔进行提取'）
#print('最终的名单是:%s%yaos')
#只能邀请两位
print('抱歉，现在只能邀请两位了')
print('到底现在是多少人%s'%yaos)
i = 1
count = len(yaos) - 1
print('')
