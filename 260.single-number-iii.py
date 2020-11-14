"""
submits:
- date: 2020-10-28
  cheating: false
  minutes: 4
- date: 2020-11-14
  cheating: true
  minutes: 40
labels:
- bit-manipulation
"""
#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (64.81%)
# Likes:    1910
# Dislikes: 119
# Total Accepted:    175.5K
# Total Submissions: 270.3K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an integer array nums, in which exactly two elements appear only once
# and all the other elements appear exactly twice. Find the two elements that
# appear only once. You can return the answer in any order.
#
# Follow up: Your algorithm should run in linear runtime complexity. Could you
# implement it using only constant space complexity?
#
#
# Example 1:
#
#
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
#
#
# Example 2:
#
#
# Input: nums = [-1,0]
# Output: [-1,0]
#
#
# Example 3:
#
#
# Input: nums = [0,1]
# Output: [1,0]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 30000
# Each integer in nums will appear twice, only two integers will appear once.
#
#
#

# @lc code=start
class Solution:
    def singleNumber(self, nums):
        xor = 0
        for n in nums:
            xor ^= n

        # 此时 xor == num1 ^ num2
        # 而且由于 ^ 运算的特性，xor 中的所有 1 要么属于 num1 要么属于 num2
        # 现在我们只要找到 xor 中的任意一个 bit

        bit = xor & -xor  # 方法一
        # bit = xor & ~(xor - 1)  # 方法二
        # 这两种方法我都不是很理解

        num1, num2 = 0, 0
        for n in nums:
            if bit & n == 0:
                num1 ^= n
            else:
                num2 ^= n
        return [num1, num2]


# @lc code=end
