#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (25.75%)
# Likes:    5746
# Dislikes: 697
# Total Accepted:    792.6K
# Total Submissions: 3.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#

from typing import List


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = set()

        for a_idx in range(0, len(nums) - 2):
            a_num = nums[a_idx]

            if a_idx != 0 and (nums[a_idx] == nums[a_idx - 1]):
                continue

            b_idx = a_idx + 1
            c_idx = len(nums) - 1
            while b_idx < c_idx:
                if (a_num + nums[b_idx] + nums[c_idx]) > 0:
                    c_idx -= 1
                elif (a_num + nums[b_idx] + nums[c_idx]) < 0:
                    b_idx += 1
                else:
                    solutions.add((a_num, nums[b_idx], nums[c_idx]))
                    b_idx += 1

        return [list(solution) for solution in solutions]


# @lc code=end

if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([0] * 3000))
