#coding=utf-8 使用字符串时避免语法错误

#coding=utf-8 撇号位于两个双引号之间，因此Python解释器能够正确地理解这个字符串：
message = "One of Python's strengths is its diverse community."
print(message)

#coding=utf-8 撇号位于两个单引号之间，因此Python不能正确解释：
"""
message = 'One of Python's strengths is its diverse community.'
print(message)
执行会出这个错误
 File "apostrophe.py", line 1
 message = 'One of Python's strengths is its diverse community.'
 ^
SyntaxError: invalid syntax
"""
