"""
labels:
- bit-manipulation
submits:
- date: 2020-11-10
  minutes: 55
  cheating: true
comment: |
  这道题需要找到一种运算操作（姑且叫做 @@ ），使得
  A @@ A @@ A == 0。这种运算可以在 0～31 中的每一个
  bit 上相加然后 mod 3 去实现。
"""
#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (52.92%)
# Likes:    2128
# Dislikes: 381
# Total Accepted:    264.1K
# Total Submissions: 497.4K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,3,2]
# Output: 3
#
#
# Example 2:
#
#
# Input: [0,1,0,1,0,1,99]
# Output: 99
#
#

# @lc code=start
class Solution:

    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        result = 0
        for i in range(32):
            sum = 0
            for n in nums:
                if n & (1 << i) == (1 << i):
                    sum += 1
            result |= (sum % 3) << i
        return result if result < (1 << 31) else result - (1 << 32)


# @lc code=end
