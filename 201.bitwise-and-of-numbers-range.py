"""
submits:
- date: 2020-11-13
  minute: 12
  cheating: false
labels:
- bit-manipulation
"""
#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (39.49%)
# Likes:    1181
# Dislikes: 131
# Total Accepted:    162.6K
# Total Submissions: 411.3K
# Testcase Example:  '5\n7'
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
# of all numbers in this range, inclusive.
#
# Example 1:
#
#
# Input: [5,7]
# Output: 4
#
#
# Example 2:
#
#
# Input: [0,1]
# Output: 0
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = 0
        for i in range(31, -1, -1):
            mbit = (m >> i) & 1
            nbit = (n >> i) & 1
            if mbit == nbit == 1:
                res |= 1 << i
            elif mbit == nbit == 0:
                pass
            else:
                break
        return res


# @lc code=end
if __name__ == "__main__":
    from tool import test

    t = test()
    f = Solution().rangeBitwiseAnd
    t.assertEqual(f(5, 7), 4)
    t.assertEqual(f(0, 1), 0)
