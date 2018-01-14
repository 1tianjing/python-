'''定义类'''
#class 类名
#    方法
class Dog:
    #方法
    def walk(self):
        print('走')
    def drink(self):
        print('喝水')
    def tian(self):
        print('舔')
#创建一个叫冰糖的狗狗
suger = Dog()
suger.name = '冰糖'
suger.walk()
suger.drink()
suger.tian()
print('*'*40)
diu_diu = Dog()
diu_diu.walk()
diu_diu.tian()
print('*'*40)
duo_duo = Dog()
duo_duo.drink()
