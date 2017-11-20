#使用函数 range() range 从第一个数据开始，第二个数结束，但不包含后面的值
for value in range(1,5):
    print(value)
#使用 range()创建数字列表
numbers = list(range(1,6))
print(numbers)
#指定步长、下面的代码打印1~10内的偶数：
even_numbers = list(range(2,11,2))
print(even_numbers)

#下面的代码打印1~10内的奇数
even_numbers = list(range(1,10,2))
print(even_numbers)