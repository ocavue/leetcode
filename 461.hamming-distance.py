"""
submits:
- date: 2020-11-21
  minutes: 1
  cheating: false
labels:
- bit-manipulation
"""
#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (72.96%)
# Likes:    1988
# Dislikes: 170
# Total Accepted:    372K
# Total Submissions: 509.5K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 2^31.
#
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
#
# The above arrows point to positions where the corresponding bits are
# different.
#
#
#

# @lc code=start
class Solution:
    def hammingDistance(self, x, y) :
        xor = x ^ y
        onns = 0
        for i in range(31, -1, -1):
            if (xor >> i) & 1:
                onns += 1
        return onns


# @lc code=end

