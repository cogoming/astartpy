#如何创建一个列表，其中包含前 10个整数（即1~10）的平方呢？在Python中，两个星号（**）表示乘方运算
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
#列表解析
squares = [value**2 for value in range(1,11)]
print(squares)
#对数字列表执行简单的统计计算
digits = [1,2,3,4,5,6,7,8,9,0]
#min 最小值 max 最大值 sum之和
print(min(digits));
print(max(digits));
print(sum(digits));
