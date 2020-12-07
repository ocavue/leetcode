"""
submits:
- date: 2020-12-07
  minutes: 10
  cheating: true
labels:
- bit-manipulation
"""
#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Medium (50.63%)
# Likes:    1435
# Dislikes: 2452
# Total Accepted:    203.7K
# Total Submissions: 402.4K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
#
#
# Example 1:
#
#
# Input: a = 1, b = 2
# Output: 3
#
#
#
# Example 2:
#
#
# Input: a = -2, b = 3
# Output: 1
#
#
#
#
#

# @lc code=start
MAX = 0x7FFFFFFF
MASK = 0xFFFFFFFF


class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a > MAX:
            a = ~(a ^ MASK)

        if b == 0:
            return a
        else:
            return self.getSum((a ^ b) & MASK, ((a & b) << 1) & MASK)


# @lc code=end
if __name__ == "__main__":
    assert (Solution().getSum(-1, 1)) == 0

