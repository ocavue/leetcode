"""
submits:
- date: 2020-09-08
  minutes: 5
  cheating: false
"""

"""
题目描述
写出一个程序，接受一个字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）

输入描述:
输入N个字符

输出描述:
输出该字符串反转后的字符串

示例1
输入
    abcd
输出
    dcba
"""

input_str = ""

while 1:
    try:
        input_str = input_str + input()
    except:
        break
print("".join(reversed(input_str)))