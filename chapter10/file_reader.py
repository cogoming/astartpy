#逐行读取
"""
with open('../chapter9/pi_digits.txt') as  file_object:
    contents = file_object.read()
print(contents.rstrip())
"""
#创建一个包含文件各行内容的列表
"""
with open('../chapter9/pi_digits.txt') as  file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
"""
#使用文件的内容
fileName = 'pi_million_digits.txt';
with open(fileName) as file_object:
    lines = file_object.readlines();
pi_string = '';
for line in lines:
    pi_string += line.rstrip().lstrip();
print(pi_string)
print(len(pi_string))
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print("Your birthday does not appear in the first million digits of pi.")
pi_string = pi_string.replace('19716939','888888888')
print(pi_string)
