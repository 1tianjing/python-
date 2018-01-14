class Xrk:
    """docstring for xrk"""
    def __init__(self):
        #super(xrk,self)._init_()
        #self.arg = arg
        self.color = '红色'
    def act(self):
        print('放阳光')
xrk = Xrk()
xrk.name = '向日葵'
xrk.color = '绿色'
xrk.height = 150
print('%s颜色是%s,身高是%d'%(xrk.name,xrk.color,xrk.height))
xrk.act()
print('*'*40)
class Wd:
    def __init__(self):
        self.color = '绿色'
        self.heir = '杀马特'
        self.blood = 100
    def pao(self):
        print('发炮')
    def head(self):
        print('摇头')
wd = Wd()
wd.name = '豌豆'
wd.height = 160
print('%s的颜色是%s,发型是%s,血量是%d,身高为%d'%(wd.name,wd.color,wd.heir,wd.blood,wd.height))
wd.pao()
wd.head()
print('*'*40)
class Jg:
    def __init__(self):
        self.blood = 500
        self.type = '肉盾'
    def pro(sef):
        print('阻挡')
jg = Jg()
jg.name = '坚果'
jg.height = 150
print('%s的血量是%d,类型是%s,身高为%d'%(jg.name,jg.blood,jg.type,jg.height))
jg.pro()
print('*'*40)
class Js:
    def __init__(self):
        self.color = '灰色'
        self.blood = 300
        self.type = '变异人'
        self.speed = 100
    def walk(self):
        print('走')
    def runjump(self):
        print('跑跳') 
    def eat(self):
        print('吃')
    def die(self):
        print('死')
js = Js()
js.name = '僵尸'
js.height = 160
print('%s的颜色是%s,血量是%s,类型是%s,速度为%d,高度是%d'%(js.name,js.color,js.blood,js.type,js.speed,js.height))
