age = 11
if age <= 12:
    print("尊敬的小玩家，你每日的游戏时间只有一个小时")


liucuihua = 18
wangergou = 22
if (liucuihua > 12 and wangergou > 12):
    print("恭喜刘翠花和王二狗能够组队玩一天")


heros = ["安琪拉","李白","大乔","貂蝉","后羿"]
hero = "后羿"
if hero in heros:
    print("队伍中有后羿，赶紧踢掉他")
else:
    print("后羿不在队伍，能赢")

libai = {"姓名":"李白","性别":"男"}
print(libai)

libai["名句"] = "努力有用的话还要天才干甚？"
print(libai)

libai["性别"] = "女"
print(libai)

del libai["性别"]
print(libai)

songfen = {
    "马化腾":"安琪拉",
    "天誉梁总":"孙悟空",
    "酸菜馆子刘翠花":"貂蝉",
    "村口铁匠王二狗":"吕布",
    "小菜鸡郑开州":"后羿"}
for key in songfen.keys():
    print(key)
for value in songfen.values():
    print(value)

  

