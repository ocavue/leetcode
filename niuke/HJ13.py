"""
submits:
- date: 2020-09-08
  minutes: 3
  cheating: false
"""

"""

将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符

接口说明

/**
 * 反转句子
 *
 * @param sentence 原句子
 * @return 反转后的句子
 */
public String reverse(String sentence);


输入描述:
将一个英文语句以单词为单位逆序排放。

输出描述:
得到逆序的句子

示例1
输入    I am a boy
输出    boy a am I
"""

def reverse(string):
    words = string.split(" ")
    reversed_words = reversed(words)
    return " ".join(reversed_words)

print(reverse(input()))