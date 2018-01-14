import random
num = random.randint(1,100)
i = 0
while 1 == 1 and i <= 10:
    player = input('请输入数字')
    guess = int(player)
    if guess == num:
        print('恭喜你猜对了')
        break
    else:
        if guess > num:
            print('sorry,数值大了')
        else:
            print('sorry,数值小了')
print('over')
