#打印1～5000  能同时被5和7整除的整数
count = 0
while count <= 5001:
    if count%5 == 0  and count%7 == 0:
        print('%d'%count)
    count += 1

