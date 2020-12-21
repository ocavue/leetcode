"""
submits:
- date: 2020-12-21
  minutes: 64
  cheating: true
"""
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#
# https://leetcode.com/problems/132-pattern/description/
#
# algorithms
# Medium (28.89%)
# Likes:    1942
# Dislikes: 123
# Total Accepted:    77.4K
# Total Submissions: 254.4K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array of n integers nums, a 132 pattern is a subsequence of three
# integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] <
# nums[k] < nums[j].
#
# Return true if there is a 132 pattern in nums, otherwise, return false.
#
# Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the
# O(n) solution?
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
#
#
# Example 2:
#
#
# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
#
#
# Example 3:
#
#
# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1,
# 3, 0] and [-1, 2, 0].
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#

# @lc code=start

from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        smallest = float('inf')
        stack = []
        for i in nums:
            while stack and i >= stack[-1][-1]:
                stack.pop()
            if stack and i > stack[-1][0]:
                return True
            stack.append((smallest,i))
            smallest = min(smallest,i)
        return False

# @lc code=end
if __name__ == "__main__":
    f = Solution().find132pattern
    from tool import t

    # t(f([1, 2, 3, 4]), False)
    # t(f([3, 1, 4, 2]), True)
    # t(f([-1, 3, 2, 0]), True)
    # t(f([1, 3, 2, 4, 5, 6, 7, 8, 9, 10]), True)
    # t(f([-2, 1, 1, -2, 1, 2]), False)
    t(f([10, 12, 6, 8, 3, 11]), True)

