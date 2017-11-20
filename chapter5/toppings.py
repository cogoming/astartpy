#检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
#数字对比
"""
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False
"""
#检查多个条件
"""
 1.使用and检查多个条件
 要检查是否两个条件都为True，可使用关键字and将两个条件测试合而为一；如果每个测试
图灵社区会员 江子涛Tesla(jiangzitao201314@foxmail.com) 专享 尊重版权
本文档由Linux公社 www.linuxidc.com 整理
68 第 5 章 if 语句
都通过了，整个表达式就为True；如果至少有一个测试没有通过，整个表达式就为False。
例如，要检查是否两个人都不小于21岁，可使用下面的测试：
 >>> age_0 = 22
>>> age_1 = 18
 >>> age_0 >= 21 and age_1 >= 21
False
 >>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
"""
"""
2. 使用or检查多个条件
关键字or也能够让你检查多个条件，但只要至少有一个条件满足，就能通过整个测试。仅当
两个测试都没有通过时，使用or的表达式才为False。
下面再次检查两个人的年龄，但检查的条件是至少有一个人的年龄不小于21岁：
 >>> age_0 = 22
>>> age_1 = 18
 >>> age_0 >= 21 or age_1 >= 21
True
 >>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
"""
#检查特定值是否包含在列表中
"""
 要判断特定的值是否已包含在列表中，可使用关键字in。
 >>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
 >>> 'mushrooms' in requested_toppings
True
 >>> 'pepperoni' in requested_toppings
False
"""

#检查特定值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

#练习
"""
5-1 条件测试：编写一系列条件测试；将每个测试以及你对其结果的预测和实际结
果都打印出来。你编写的代码应类似于下面这样：
"""
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping =='green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

#使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")