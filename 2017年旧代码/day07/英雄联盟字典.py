#分类：法师：火女 冰女  战士：德玛西亚 诺克萨斯  坦克：猪妹 雷霆咆哮
#法师
fa_shi = ['火女','冰女']
#战士
zhan_shi = ['德玛西亚','诺克萨斯']
#坦克
tan_ke = ['猪妹','雷霆咆哮']
#英雄谱
hero = {'法师':fa_shi,'战士':zhan_shi,'坦克':tan_ke}
#print(hero.get('战士'))
test = input('请输入你要查找的类型')
print(hero.get(test))
