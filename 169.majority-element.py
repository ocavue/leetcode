"""
submits:
  - date: 2020-04-13
    cheating: false
comment: |
  这道题可以用「找出队列中数量最多的元素」的方式去做，比如说使用 hash_map 可以做到时间空间复杂度都为 O(n)。
  但是这道题特殊的地方在于「出现的元素数量大于 n/2」，那么可以使用「Boyer-Moore Voting Algorithm」。
  可以做到 space: O(1); time: O(n)
"""
#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (55.99%)
# Likes:    2640
# Dislikes: 206
# Total Accepted:    532K
# Total Submissions: 945.1K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#
#

# @lc code=start
class Solution:
    def majorityElement(self, items: list) -> int:
        candidate = 0
        count = 0
        for i in items:
            assert count >= 0
            if count == 0:
                candidate = i

            if candidate == i:
                count += 1
            else:
                count -= 1
        return candidate


# @lc code=end
