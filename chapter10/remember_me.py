import json

username = input("你叫什么名字")
filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("我们将记录您的名称当您退出时"+username)
