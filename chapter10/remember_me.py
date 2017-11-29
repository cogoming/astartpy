import json

"""
username = input("你叫什么名字")
filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("我们将记录您的名称当您退出时"+username)
"""
def get_stored_username():
    filename = 'username.json';
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
       return None;
    else:
        return username
def get_new_username():
    username = input("What is your name")
    filename = 'username.json';
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username;
def greet_user():
    username = get_stored_username();
    if username:
        print("welcome back,"+username+"!")
    else:
        username = get_new_username();
        print("We'll remember you when you come back, " + username + "!")
"""
def greet_user():
    #问候用户，并指出其名字
    filename = 'username.json';
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name")
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
    else:
        print("welcome back,"+username+"!")
"""
greet_user();
