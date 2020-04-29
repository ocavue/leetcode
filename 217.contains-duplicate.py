#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (54.94%)
# Likes:    695
# Dislikes: 674
# Total Accepted:    500.6K
# Total Submissions: 907.4K
# Testcase Example:  '[1,2,3,1]'
#
# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the
# array, and it should return false if every element is distinct.
#
# Example 1:
#
#
# Input: [1,2,3,1]
# Output: true
#
# Example 2:
#
#
# Input: [1,2,3,4]
# Output: false
#
# Example 3:
#
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            else:
                s.add(n)
        return False


# @lc code=end
