"""
submit:
- date: 2020-10-14
  cheating: false
  minutes: 24
labels:
- hash-map
"""
#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (43.04%)
# Likes:    2421
# Dislikes: 129
# Total Accepted:    171.6K
# Total Submissions: 398.7K
# Testcase Example:  '[0,1]'
#
# Given a binary array, find the maximum length of a contiguous subarray with
# equal number of 0 and 1.
#
#
# Example 1:
#
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
# and 1.
#
#
#
# Example 2:
#
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
#
#
#
# Note:
# The length of the given binary array will not exceed 50,000.
#
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums) -> int:
        count = 0

        map = {0: -1}  # 第一次出现 count 的 index 是多少：map[count] = index
        max_len = 0
        for index, num in enumerate(nums):

            if num == 1:
                count += 1
            else:
                count -= 1
            # 如果 count 相同，则表示两个 index 之间出现的 1 和 0 的数量相同

            if count in map:
                max_len = max(max_len, index - map[count])
            else:
                map[count] = index
        return max_len


# @lc code=end
