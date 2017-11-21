#函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后， Python将其存储在一个变量中，以方便你使用。
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

#使用标志
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

#使用 break 退出循环
while active:
    message = input(prompt)
    if message == 'quit':
        break;
    print(message)
#在循环中使用 continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
