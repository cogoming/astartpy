#每当你使用函数input()时，都应指定清晰而易于明白的提示，准确地指出你希望用户提供什么样的信息——指出用户该输入任何信息
# 的提示都行，如下所示：
name = input("Please enter your name: ")
print("Hello, " + name + "!")

#有时候，提示可能超过一行，例如，你可能需要指出获取特定输入的原因。在这种情况下，可将提示存储在一个变量中，再将该变量传
# 递给函数input()。这样，即便提示超过一行， input()语句也非常清晰。
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")
