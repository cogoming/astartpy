bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1])

bicycles.append('qiuming')
print(bicycles)
bicycles.insert(2,'qiuming')
print(bicycles)
#从列表中删除元素
del bicycles[2]
print(bicycles)
#使用方法pop()删除元素
popbicycles = bicycles.pop()
print(popbicycles)
print(bicycles)

pop1 = bicycles.pop(1)
print(pop1)
print(bicycles)
#根据值删除元素
bicycles.remove('redline')
print(bicycles)

"""
动手试一试
下面的练习比第 2 章的练习要复杂些，但让你有机会以前面介绍过的各种方式使用
列表。
3-4 嘉宾名单：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），
你会邀请哪些人？请创建一个列表，其中包含至少 3 个你想邀请的人；然后，使用这个
列表打印消息，邀请这些人来与你共进晚餐。
3-5 修改嘉宾名单：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
 以完成练习 3-4 时编写的程序为基础，在程序末尾添加一条 print 语句，指出哪
位嘉宾无法赴约。
 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
 再次打印一系列消息，向名单中的每位嘉宾发出邀请。
3-6 添加嘉宾：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀
请哪三位嘉宾。
 以完成练习 3-4 或练习 3-5 时编写的程序为基础，在程序末尾添加一条 print 语
句，指出你找到了一个更大的餐桌。
 使用 insert()
 使用 insert()将另一位新嘉宾添加到名单中间。
 使用 append()将最后一位新嘉宾添加到名单末尾。
 打印一系列消息，向名单中的每位嘉宾发出邀请。
3-7 缩减名单：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
 以完成练习 3-6 时编写的程序为基础，在程序末尾添加一行代码，打印一条你只
能邀请两位嘉宾共进晚餐的消息。
 使用 pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹
出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进
晚餐。
 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
 使用 del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程
序结束时名单确实是空的
"""
guests = ['王剑平','樊凯','兰舒芳'];
print(guests);
print('临时有事无法来参加的是:'+guests[2])
guests[2] = '黄燕洪';
print(guests);
guests.insert(1,'张宇栋')
guests.insert(3,'刘玉')
guests.append('黄东旭')
print("我找到了更大的一张桌子，以下是新邀请名单:")
print(guests)

flag = True
name = ''
tempguests = [guests.pop(0),]
tempname = guests[2];
while(flag):
    flag = guests.pop();
    print(name+"很抱歉，无法邀请他来共进晚餐");
    if (tempname==flag):
        break;

print(guests[0]+"依然在受邀人之列");
print(guests[1]+"依然在受邀人之列");
del guests[1]
del guests[0]
print("看看是不是空的")
print(guests)










