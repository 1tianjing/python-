# 先判断是男的还是女的，如果是男的，就是高富帅，如果是女的，那就是白富美
sex = input("你是男的还是女的还是其他的")
if sex == "男":
    height = input("你高吗")
    money = input("你富吗") 
    handsome =input("你帅吗")  
    if height !='矮'and money !='穷' and  handsome !='挫':
        print("你就是高富帅")
    else:
        print("你就是矮挫穷")
elif sex == "女":
    color = input("你白吗")
    money = input("你富吗")
    mei = input("你美吗")
    if color == '白'or mei == '美':
        print("你是一个大美女")
else:
    die = input("是死是活")
    if not die == "活":
        print("你就是死人妖")
    else:
        print("你就是活人妖")
