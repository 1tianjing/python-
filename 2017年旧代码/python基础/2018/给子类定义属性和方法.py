class Car():
    pass
class ElectricCar(Car):
    """Represent aspects of a car,specific to electric vehicles."""
    def __init__(self,make,model,year):
        """
        电动车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make,model,year)
        self.battery_size = 70
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a" + str(self.battory_size)+"-kwh battery.")
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
