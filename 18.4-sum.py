#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (32.59%)
# Likes:    1553
# Dislikes: 291
# Total Accepted:    299.6K
# Total Submissions: 919.5K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#
#
#
from typing import List

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        solutions = set()

        for a_idx in range(0, len(nums) - 3):
            if a_idx > 0 and nums[a_idx - 1] == nums[a_idx]:
                continue
            for b_idx in range(a_idx + 1, len(nums) - 2):
                if b_idx > a_idx + 1 and nums[b_idx - 1] == nums[b_idx]:
                    continue

                c_idx = b_idx + 1
                d_idx = len(nums) - 1

                while c_idx < d_idx:
                    four_nums = (nums[a_idx], nums[b_idx], nums[c_idx], nums[d_idx])
                    result = sum(four_nums)
                    if result > target:  # d_idx is too large
                        d_idx -= 1
                    elif result < target:  # c_idx is too small
                        c_idx += 1
                    else:
                        d_idx -= 1
                        solutions.add(four_nums)

        return [list(i) for i in solutions]


# @lc code=end

if __name__ == "__main__":
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    print(Solution().fourSum([0, 0, 0, 0], 0))
