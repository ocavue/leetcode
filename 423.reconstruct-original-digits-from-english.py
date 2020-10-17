"""
submits:
- date: 2020-10-17
  minute: 20
  cheating: false
comment: 答案中有一种稍微更快一些的方法，可以不需要 for loop
"""
#
# @lc app=leetcode id=423 lang=python3
#
# [423] Reconstruct Original Digits from English
#
# https://leetcode.com/problems/reconstruct-original-digits-from-english/description/
#
# algorithms
# Medium (47.09%)
# Likes:    180
# Dislikes: 599
# Total Accepted:    24.9K
# Total Submissions: 52.9K
# Testcase Example:  '"owoztneoer"'
#
# Given a non-empty string containing an out-of-order English representation of
# digits 0-9, output the digits in ascending order.
#
# Note:
#
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original
# digits. That means invalid inputs such as "abc" or "zerone" are not
# permitted.
# Input length is less than 50,000.
#
#
#
# Example 1:
#
# Input: "owoztneoer"
#
# Output: "012"
#
#
#
# Example 2:
#
# Input: "fviefuro"
#
# Output: "45"
#
#
#


map = {
    1: "one",
    9: "nine",
}

# chars = set()
# for v in map.values():
#     for c in v:
#         chars.add(c)
# print(chars)

# @lc code=start


from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        output = [0] * 10
        counter = Counter(s)

        print(counter)

        output[0] = counter["z"]
        for char in "zero":
            counter[char] -= output[0]

        output[2] = counter["w"]
        for char in "two":
            counter[char] -= output[2]

        output[6] = counter["x"]
        for char in "six":
            counter[char] -= output[6]

        output[8] = counter["g"]
        for char in "eight":
            counter[char] -= output[8]

        # 以上几个操作可以乱序，以下不行

        output[3] = counter["t"]  # 除了 two 和 eight 之外，只有 three 有 t
        for char in "three":
            counter[char] -= output[3]

        output[4] = counter["r"]
        for char in "four":
            counter[char] -= output[4]

        output[5] = counter["f"]
        for char in "five":
            counter[char] -= output[5]

        output[7] = counter["v"]
        for char in "seven":
            counter[char] -= output[7]

        output[1] = counter["o"]
        for char in "one":
            counter[char] -= output[1]

        output[9] = counter["i"]
        for char in "nine":
            counter[char] -= output[9]

        print(counter)
        result = ""
        for num, count in enumerate(output):
            result = result + str(num) * count
        return result

# @lc code=end
if __name__ == "__main__":
    f = Solution().originalDigits
    f("owoztneoer")