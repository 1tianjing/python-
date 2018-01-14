#定义'玉米'类
class SweetPotato:
    '''这是地瓜类'''
    def __init__(self):
        #0~3表示还是生的，超过3表示半生不熟，超过5表示烤熟
        self.cookedLever = 0
        self.cookedStr = '生的'
        #这是烤地瓜的配置列表
        self.condliments = []
       #添加烤地瓜的方法
    def cook(self,time):
        self.cookedLever += time
        if self.cookedLever >8:
            self.cookedStr = '烧成炭了'
        elif self.cookedLever>5:
            self.cookedStr = '烤好了'
        elif self.cookedLever >3:
            self.cookedStr = '半生不熟'
        else:
            self.cookedStr = '生的'
    def __str__(self):
        msg = self.cookedStr = '地瓜'
        if len(self.condliments) > 0:
            msg = msg+'('
            for temp in self.condliments:
                msg = msg + temp+','
            msg = msg.strip(',')
            msg = msg + ')'
        return msg
    def addCondiments(self,condliments):
        self.condliments.append(condliments)
mySweetPotato = SweetPotato()
print('-----有了一个地瓜，还没有烤地瓜-----')
print(mySweetPotato.cookedLever)
print(mySweetPotato.cookedStr)
print(mySweetPotato.condliments)
print('-----接下来进行烤地瓜了-----')
print('-----地瓜已经烤了四分钟了')
mySweetPotato.cook(4)#烤了四分钟
print(mySweetPotato)
print('-----地瓜又烤了3分钟')
mySweetPotato.cook(3)
print(mySweetPotato)
print('-----接下来添加番茄酱-----')
mySweetPotato.addCondiments('番茄酱')
print(mySweetPotato)
print('-----地瓜又烤了5分钟-----')
mySweetPotato.cook(5)
print(mySweetPotato)
print('-----地瓜接下来添加芥末-----')

