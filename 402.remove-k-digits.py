"""
submits:
- date: 2020-10-03
  minutes: 25
  cheating: false
labels:
- stack
"""
#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#
# https://leetcode.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (27.50%)
# Likes:    2516
# Dislikes: 108
# Total Accepted:    151.7K
# Total Submissions: 533.7K
# Testcase Example:  '"1432219"\n3'
#
# Given a non-negative integer num represented as a string, remove k digits
# from the number so that the new number is the smallest possible.
#
#
# Note:
#
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
#
#
#
#
# Example 1:
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
# which is the smallest.
#
#
#
# Example 2:
#
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output
# must not contain leading zeroes.
#
#
#
# Example 3:
#
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with
# nothing which is 0.
#
#
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k > 0 and len(stack) > 0 and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)
        if k > 0:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"

        # while k > 0:
        #     while num.startswith("0"):
        #         num = num[1:]

        #     if k >= len(num):
        #         return "0"

        #     # # 优先减少更多位数
        #     # if "0" in num:
        #     #     first_zero_index = num.index("0")
        #     #     if k >= first_zero_index:
        #     #         num = num[first_zero_index:]
        #     #         k = k - first_zero_index
        #     #         continue

        #     best = num[1:]
        #     for i in range(len(num)):
        #         best = min(best, num[:i] + num[i + 1 :])
        #     num = best
        #     k = k - 1
        #     continue

        # while num.startswith("0"):
        #     num = num[1:]

        # return num or "0"


# @lc code=end

if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().removeKdigits
    t.assertEqual(f("1230123", 3), "123")
    t.assertEqual(f("123", 1), "12")
    t.assertEqual(f("10200", 1), "200")
    t.assertEqual(f("1432219", 1), "132219")
    t.assertEqual(f("1432219", 3), "1219")
    t.assertEqual(f("10", 1), "0")
