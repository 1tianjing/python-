import random
i = 0
while i < 10:
    player5tr = input('请输入[0剪刀 1石头 2布]')
    player = int(player5tr)
    mac = random.randint(0,2)
    if (player == 0 and mac == 2) or (player == 1 and mac == 0) or (player == 2 and mac == 1):
        print('你赢了')
    elif player == mac:
        print('平局，要不要再来一局')
    else:
        print('你输了')
    i += 1

