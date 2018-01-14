class Restaurant(object):
    def __init__(self,restaurant_name,cuisine_type,number_served='0'):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number = number_served
    def describe_restaurant(self):
        print('%s'%self.name,'是一家%s'%self.type,'环境好，服务一流')
    def open_restaurant(self):
        print('正在营业')
    def set_number_served(self):
        print('有%s人来就餐'%self.number)
class Ice_cream(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,number_served='0'):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number = number_served
        self.chengdu = 0
        self.chengdu_str = '粉'
        self.flavors = ['香草','草莓']
    def kouwei(self):
        print('有%s几种口味'%self.flavors)
    def zuo(self,times):
        self.chengdu += times
        if self.chengdu > 15:
            self.chengdu_str = '冻成冰块了'
        elif self.chengdu > 8:
            self.chengdu_str = '正好，可以吃了'
        elif self.chengdu > 5:
            self.chengdu_str = '还是水'
        else:
            self.chengdu_str = '粉'
bjl = Ice_cream('nn','dd','6')
bjl.describe_restaurant()
bjl.open_restaurant()
bjl.kouwei()
bjl.set_number_served()
bjl.zuo(4)
print(bjl.chengdu)
print(bjl.chengdu_str)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_open_number_served()
print('-'*40)
modu = Restaurant('魔都','西餐厅','20')
modu.describe_restaurant()
modu.open_restaurant()
modu.set_number_served()
print('-'*40)
love = Restaurant('爱','主题餐厅','6')
love.describe_restaurant()
love.open_restaurant()
love.set_number_served()
print('-'*40)
class User(object):
    def __init__(self,first_name,list_name,login_attempts,add):
        self.first_name = first_name
        self.list_name = list_name
        self.login_attempts = login_attempts
        self.login_appempts = 8
        self.add = add
    def describe_user(self):
        print('你的姓是%s\n你的名是%s\n第三人称是%s'%(self.first_name,self.list_name,self.add,self.login_attempts))
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)
    def resrt_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)
    def greer_user(self):
        print('您好')
class Privileages():
    def __init__(self):
        self.privileages = ['can add post','can delete post','can bin user']
    def show_privileages(self):
        print(self.privileages)
class Admin(User):
    def __init__(self,first_name,list_name,login_attempts,add):
        self.pricileages = ['can add post','can delste post','can bin user']
    def show_pvivileages(self):
        print(self.privileages)
admin = Admin('tian','jing','ssxs','sssa')
admin.show_privileages()
man = User('田','静','田静','山西晋城')
man.describe_user()
man.greer_user()
man.increment_login_attempts()
man.increment_login_attempts()
man.increment_login_attempts()
man.resrt_login_attempts()
man.inceement_login_attempts()
man.inceement_login_attempts()
man.resrt_login_attempts()
  
