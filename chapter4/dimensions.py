#元组 不可变的列表被称为元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#因为给元组变量赋值是合法的
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)