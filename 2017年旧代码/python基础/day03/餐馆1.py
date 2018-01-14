#创建一个类
class Restaurant():
    def __init__(self,newname,ktype):
        self.restaurant_name = newname
        self.cuisine_type = ktype
    def describe_restaurant(self):
        print('餐厅的名字是%s,餐厅的风格是%s'%(self.restaurant_name,self.cuisine_type))
    def open_restaurant(self):
        print('正在营业')
restaurant = Restaurant('翠花大饭店','川菜')
restaurant.describe_restaurant()
restaurant.open_restaurant()
