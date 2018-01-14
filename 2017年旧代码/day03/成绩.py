#一共两门课程，第一门课程60分以上，则通过，不及格则不通过，第一门课程及格而第二门不及格，则补考
name = input("请输入你的姓名")
one = int(input("请输入第一门课程的成绩"))
if one >= 60:
    print("通过")
    two = int(input("请输入第二门课程的成绩"))
    if two >= 60:
        print("通过")
    else:
        print("补考")
else:
    print("不通过")
