#简单if
age = 12
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
# if - esls
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#if-elif-else
if age < 4:
    price = 0;
elif age < 18:
    price = 5;
else:
    price = 10;
print("Your admission cost is $" + str(price) + ".")

#使用多个 elif 代码块
age = 60
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")