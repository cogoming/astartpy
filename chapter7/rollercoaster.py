# Python将这个数字解读为字符串，但随后int()将这个字符串转换成了数值
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

