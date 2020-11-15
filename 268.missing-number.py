"""
submits:
- date: 2020-11-15
  minutes: 7
  cheating: false
labels:
- bit-manipulation
"""
#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (52.20%)
# Likes:    2249
# Dislikes: 2352
# Total Accepted:    532.1K
# Total Submissions: 1M
# Testcase Example:  '[3,0,1]'
#
# Given an array nums containing n distinct numbers in the range [0, n], return
# the only number in the range that is missing from the array.
#
# Follow up: Could you implement a solution using only O(1) extra space
# complexity and O(n) runtime complexity?
#
#
# Example 1:
#
#
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range
# [0,3]. 2 is the missing number in the range since it does not appear in
# nums.
#
#
# Example 2:
#
#
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range
# [0,2]. 2 is the missing number in the range since it does not appear in
# nums.
#
#
# Example 3:
#
#
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range
# [0,9]. 8 is the missing number in the range since it does not appear in
# nums.
#
#
# Example 4:
#
#
# Input: nums = [0]
# Output: 1
# Explanation: n = 1 since there is 1 number, so all numbers are in the range
# [0,1]. 1 is the missing number in the range since it does not appear in
# nums.
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^4
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
#
#
#

# @lc code=start
class Solution:
    def missingNumber(self, nums) -> int:
        xor = 0
        for i, num in enumerate(nums):
            xor ^= num
            xor ^= i
        xor ^= len(nums)
        return xor


# @lc code=end
if __name__ == "__main__":
    from tool import test

    t = test()
    f = Solution().missingNumber
    t.assertEqual(f([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
