name = input ("请输入你的姓名")
ID = input ("请输入你的帐号")
password = input ("请输入你的密码")
qukuan = input ("请输入你的取款金额")
yue = 50000000000
sum = int(yue) - int(qukuan)

print ("姓名:%s"%name)
print ("帐号:%s"%ID)
print ("密码:%s"%password)
print ("余额:%s"%yue)
print ("取款金额:%s"%qukuan)
print ("取款之后的余额:%s"%sum)
