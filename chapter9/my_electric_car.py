#导入单个类 from cartwo import ElectricCar
#导入多个类 from cartwo import Car,ElectricCar
#导入模板中所有类  from cartwo import *
from cartwo import Car,ElectricCar

my_beetle = Car('volkswagen', 'beetle', 20)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
