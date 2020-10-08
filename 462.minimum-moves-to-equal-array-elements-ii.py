"""
submits:
- date: 2020-10-08
  minutes: 20
  cheating: true

"""
#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
#
# algorithms
# Medium (53.23%)
# Likes:    563
# Dislikes: 46
# Total Accepted:    47.4K
# Total Submissions: 87.9K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty integer array, find the minimum number of moves required to
# make all array elements equal, where a move is incrementing a selected
# element by 1 or decrementing a selected element by 1.
#
# You may assume the array's length is at most 10,000.
#
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 2
#
# Explanation:
# Only two moves are needed (remember each move increments or decrements one
# element):
#
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
#
#
#

# @lc code=start
class Solution:
    def minMoves2(self, nums) -> int:
        nums.sort()
        median = nums[len(nums) / 2]
        return sum(abs(num - median) for num in nums)


# @lc code=end

