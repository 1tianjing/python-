#定义函数
def greet_user():
    '''显示简单的问候语'''
    print("hello!")
greet_user()
#向函数传递信息
def greet_user(username):
    '''显示简单的问候语'''
    print("hello,"+username.title()+"!")
greet_user('jesse')
#传递实参
def describe_pet(animal_type,pet_name):
    '''显示宠物的信息'''
    print("\n have a"+animal_type+".")
    print("My"+animal_type+"'s name is "+pet_name.title()+".")
describe_pet("hamster","harry")
#调用函数多次
def describe_pet(animal_type,pet_name):
    '''显示宠物的信息'''
    print("\n have a "+animal_type+".")
    print("My"+animal_type+"'s name is"+pet_name.title()+".")
describe_pet('hamster','harry')
describe_pet('dog','willie')

#关键字实参
def describe_pet(animal_type,pet_name):
    '''显示宠物的信息'''
    print("\n have a"+animal_type+".")
    print("My"+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(animal_type='hamster',pet_name='harry')


#默认值
def describe_pet(pet_name,animal_type='dog'):
    '''显示宠物的信息'''
    print("\n have a"+ animal_type+".")
    print("My "+animal_type+"'s name is"+pet_name.title()+".")
describe_pet(pet_name='willie')

#等效的函数调用
def describe_pet(pet_name,animal_type='dog'):
    pass
#一条名为willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')

#一只名为harry的仓鼠
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')

#返回值
def get_formatted_name(first_name,last_name):
    '''返回整洁的姓名'''
    full_name = first_name +'' +last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)


#让参数变成可选的
def get_formatted_name(first_name,middle_name,last_name):
    '''返回整洁的名字'''
    full_name = first_name +''+middle_name+''+last_name
    return full_name.title()
musician = get_formatted_name('john','lee','hooker')
print(musician)

#返回字典
def build_person(first_name,last_name):
    '''返回一个字典，其中包含有关一个人的信息'''
    person = {'first':first_name,'last':last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)


#结合使用函数和while循环
def get_formatted_name(first_name,last_name):
    '''返回整洁的姓名'''
    full_name = first_name+''+last_name
    return full_name.title()

#这是一个无限循环
#while True:
    #print("\nPlease tell me your name:")
    #f_name = input("First_name:")
    #l_name = input("Last_name:")
    #formatted_name = get_formatted_name(f_name,l_name)
    #print("\nHello,"+formatted_name+"!")


#def get_formatted_name(first_name,last_name):
    '''返回整洁的姓名'''
    #full_name = first_name+''+last_name
    #return full_name.title()
#while True:
    #print("\nPlease tell me your name:")
    #print("(enter 'q' at any time to quit)")
    #f_name = input("First name")
    #if f_name == 'q':
        #break
    #l_name = input("Last name:")
    #if l_name == 'q':
        #break
#formatted_name = get_formatted_name(f_name,l_name)
#print("\nHello,"+formatted_name+"!")


#传递列表
def greet_users(names):
    '''向列表中的每位用户都发出简单的问候'''
    for name in names:
        msg = "Hello,"+name.title()+"!"
        print(msg)
usernames = ["hannah","ty","margot"]
greet_users(usernames)

#在函数中修改列表
#首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone','robot pendant','dodecahedron']
completed_models = []
#模拟打印每个设计，知道没有未打印的设计为止
#打印每个设计后，都将其移动到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #模拟根据设计制作3D打印模型的过程
    print("Printing model:"+current_design)
#显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


def print_models(unprinted_designs,completed_models):
    """
    模拟打印每个设计，知道没有未打印的设计为止
    打印每个设计后，都将其移动法哦列表completed_modles中
    """
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        #模拟根据设计制作3D打印模型的过程
        print("Printing_model:"+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)


#传递任意数量的实参
def make_pizza(*toppings):
    '''概述要制作的批萨'''
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-"+topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#使用任意数量的关键字实参
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的所有有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['lastz_name'] = last
    for key,value in user_info.items():
        return profile
user_profile = build_profile('albert','einstein',
                             location = 'princeton',
                             field = 'physics')
print(user_profile)



