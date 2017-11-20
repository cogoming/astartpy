#复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('雪梨')
friend_foods.append('苹果')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#以下这种方式二边的值会变成一样
friend_foods = my_foods
my_foods.append('雪梨')
friend_foods.append('苹果')
print(my_foods)
print(friend_foods)