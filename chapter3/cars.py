#使用方法 sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True);
print(cars)
#使用函数 sorted()对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)
#倒着打印列表
cars.reverse();
print(cars)
# 确定列表的长度
carsLen = len(cars)
print(carsLen)
#使用列表时避免索引错误
cars = ['bmw', 'audi', 'toyota', 'subaru']
#print(cars[4])
#执行上面的代码会报如下错误
"""
Traceback (most recent call last):
  File "E:/workpy/astartpy/chapter3/cars.py", line 20, in <module>
['toyota', 'subaru', 'bmw', 'audi']
    print(cars[4])
IndexError: list index out of range
"""
#用负数取后几元素，-1 表示最后一个，-2表示倒数第2个，不建议如此表示
print(cars[-1])
print(cars[-2])

