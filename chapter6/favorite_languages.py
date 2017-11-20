#由类似对象组成的字典
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")
#遍历字典
for key, value in favorite_languages.items():
    print("\nKey: " + key)
    print("Value: " + value)

#循环中使用变量name和language，
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
#遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())
#按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
  print(name.title() + ", thank ou for takin the oll.")
#遍历字典中的所有值
for language in favorite_languages.values():
    print(language.title())

#字典存储列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
 }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
