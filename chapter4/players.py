#使用列表中的一部分
#切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
#从0到3 不包含下标为3的元素
print(players[0:3])
#从1到4 不包含下标为4的元素
print(players[1:4])
#从0到4 不包含下标为4的元素
print(players[:4])
#从第2到最后
print(players[2:])
#最后2个元素
print(players[-2:])

#遍历切片
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())