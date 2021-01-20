"""
submits:
- date: 2021-01-20
  minutes: 1
  cheating: false
- date: 2021-01-20
  minutes: 2
  cheating: true
labels:
- dp

"""
#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (45.80%)
# Likes:    1127
# Dislikes: 1255
# Total Accepted:    234.9K
# Total Submissions: 499.5K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n' +  '[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
#
# Implement the NumArray class:
#
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int i, int j) Return the sum of the elements of the nums array
# in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... ,
# nums[j]))
#
#
#
# Example 1:
#
#
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]
#
# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
# numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
# numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 0 <= i <= j < nums.length
# At most 10^4 calls will be made to sumRange.
#
#
#

# @lc code=start
class NumArray:
    def __init__(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        self.nums = nums

    def sumRange(self, i, j):
        if i == 0:
            return self.nums[j]
        else:
            return self.nums[j] - self.nums[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


# @lc code=end

