#去阿里面试，要求：年龄为18岁以上，学历为初中以上，如果同时满足两个条件，直接入职，如果满足其中一个，进行第二轮面试，如果一项都不满足，拒绝
name = input("请输入你的姓名")
age = int(input("请输入你的年龄"))
education = int(input("如果是初中以上学历输入1,如果是初中以下学历输入2"))
if age > 18 and education == 1:
    print("恭喜你进入本公司！")
elif age > 18 and education == 2:
    print("进入第二轮面试")
else:
    print("拒绝")
