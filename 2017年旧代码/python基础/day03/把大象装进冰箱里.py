#把指定物体放进冰箱
class Play_hf:
    #1、写一个构造函数
    def __init__(self,newName,animal):
        self.animal = animal
        self.name = newName
    #2、韩芳要去买大象
    def buyAnimal(self):
        print('%s'%self.name,'准备了一只%s'%self.animal)
    #3、打开冰箱
    def open_BinXiang(self):
        print('打开冰箱')
    #装进冰箱
    def zhuang_jin(self):
        print('把%s装进冰箱里面'%self.animal)
    #关闭冰箱
    def close_binXiang(self):
        print('关闭冰箱')
game = Play_hf('九妹','老鼠')
game.buyAnimal()
game.open_BinXiang()
game.zhuang_jin()

