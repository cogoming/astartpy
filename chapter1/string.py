#coding=utf-8 修改大小写
name = "ada lovelace";
print(name.title());
print(name.upper());
print(name.lower());

#coding=utf-8 合并（拼接）字符串
first_name = "alex"
last_name = "start"
full_name = first_name+" "+last_name
print(full_name)
print("Hello,"+full_name.title()+"!")
message = "Hello,"+full_name.title()+"!"
print(message)

#coding=utf-8 使用制表符或换行符来添加空白
print("python")
print("\tpython")
print("Languages:\npython\nc\nJavascript")
#coding=utf-8 删除空白
"""
rstrip() 删除后面的空白
lstrip() 删除前面的空白
"""
msg = " astart "
print(msg)
print(msg.rstrip())

msg = msg.rstrip().lstrip();
print(msg)


