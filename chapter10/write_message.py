#写入空文件
fileName = 'programming.txt';
"""
with open(fileName,'r+') as file_object:
    file_object.write('I love programming\n')
    file_object.write("I love creating new games.\n")
"""
#附加
with open(fileName,'a') as file_object:
    file_object.write('I love programming\n')
    file_object.write("I love creating new games.\n")

