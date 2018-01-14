#类别，单价，重量，总额，收款，应付，找零
typei = input ("请输入商品类型")
price = int (input("请输入单价")) 
weight = int (input("请输入重量"))
shifu = int (input ("请输入实付金额"))
yingfu = float(price)* float(weight)
zhaoling = float(shifu) - float(yingfu)
a = ("欢迎光临")
b = ("祝你购物愉快")
c = ("欢迎下次光临")
print("%s \n类别:%s \n单价:%s \n重量:%s \n应付金额:%s \n实付金额:%s \n找零:%s \n%s \n%s"%(a,typei,str(price),str(weight),str(yingfu),str(shifu),str(zhaoling),b,c))


