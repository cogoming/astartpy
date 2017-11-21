#import pets
#import pizza
# pizza.make_pizza(16, 'pepperoni')
#pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#pets.describe_pet('willie')();
"""
#引入模块中的指定funcgion
from pizza import make_pizza
make_pizza(16, 'pepperoni')
"""
"""
#使用 as 给函数指定别名
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
"""
"""
8.6.5 导入模块中的所有函数
使用星号（*）运算符可让Python导入模块中的所有函数：
"""
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
