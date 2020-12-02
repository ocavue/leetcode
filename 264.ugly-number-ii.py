"""
submits:
- date: 2020-12-02
  minutes: 9
  cheating: false
labels:
- dp
"""
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (42.35%)
# Likes:    2188
# Dislikes: 133
# Total Accepted:    189.5K
# Total Submissions: 446.5K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example:
#
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
#
# Note:
#
#
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
#
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 0:
            return []

        seq = [1]
        i2, i3, i5 = 0, 0, 0

        while len(seq) < n:
            n2, n3, n5 = seq[i2] * 2, seq[i3] * 3, seq[i5] * 5
            if n2 <= n3 and n2 <= n5:
                i2 += 1
                if n2 > seq[-1]:
                    seq.append(n2)
            if n3 <= n2 and n3 <= n5:
                i3 += 1
                if n3 > seq[-1]:
                    seq.append(n3)
            if n5 <= n2 and n5 <= n3:
                i5 += 1
                if n5 > seq[-1]:
                    seq.append(n5)
        return seq[-1]


# @lc code=end
if __name__ == "__main__":
    from tool import t

    f = Solution().nthUglyNumber
    t(f(10), 12)
