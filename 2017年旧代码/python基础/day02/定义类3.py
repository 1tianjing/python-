#汽车类
class Car:
    def _init_(self,newname):
        self.name = newname
        self.price = '50000000'
    def move(self):
        print(self.name,'移动')
    def toot(self):
        print('鸣叫...')
#创建对象
red_car = Car('玛莎拉蒂')
red_car.move()
red_car.color = 'red'
print('内存地址1:',id(red_car),red_car.color)
blue_car = Car('凯迪拉克')
blue_car.toot()
blue_car.color = 'blue'
print('内存地址2:',id(blue_car),blue_car.color)
yellow_car = Car('林肯')
yellow_car.move()
yellow_car.toot()
yellow_car.color = 'yellow'
print('内存地址3:',id(yellow_car),yellow_car.color)
