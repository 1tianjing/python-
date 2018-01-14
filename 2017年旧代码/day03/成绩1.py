python_score = int(input("请输入你的成绩"))
c_score = int(input("请输入你的成绩"))
if python_score > 60:
    print("合格")
    if c_score > 60:
        print("合格")
    else:
        print("不合格")
else:
    print("不合格")
