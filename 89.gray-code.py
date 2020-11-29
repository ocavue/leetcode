"""
submits:
- date: 2020-11-29
  minutes: 9
  cheating: false
labels:
- bit-manipulation
"""
#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
# https://leetcode.com/problems/gray-code/description/
#
# algorithms
# Medium (49.57%)
# Likes:    724
# Dislikes: 1661
# Total Accepted:    170.7K
# Total Submissions: 342.8K
# Testcase Example:  '2'
#
# The gray code is a binary numeral system where two successive values differ
# in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the
# code, print the sequence of gray code. A gray code sequence must begin with
# 0.
#
# Example 1:
#
#
# Input: 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
# For a given n, a gray code sequence may not be uniquely defined.
# For example, [0,2,3,1] is also a valid gray code sequence.
#
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
#
#
# Example 2:
#
#
# Input: 0
# Output: [0]
# Explanation: We define the gray code sequence to begin with 0.
# A gray code sequence of n has size = 2^n, which for n = 0 the size is 2^0 =
# 1.
# Therefore, for n = 0 the gray code sequence is [0].
#
#
#

# @lc code=start
class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        if n == 2:
            return [0, 1, 3, 2]

        result = self.grayCode(n - 1)
        length = len(result)
        for i in range(length - 1, -1, -1):
            result.append((1 << (n - 1)) + result[i])
        return result


# @lc code=end
if __name__ == "__main__":
    from tool import t

    f = Solution().grayCode
    # fmt:off
    t(f(2), [int(i, 2) for i in [
        "00",
        "01",
        "11",
        "10",
    ]])
    t(f(3), [int(i, 2) for i in [
        '000',
        '001',
        '011',
        '010',
        '110',
        '111',
        '101',
        '100',
    ]])
