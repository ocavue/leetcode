#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.72%)
# Likes:    1677
# Dislikes: 120
# Total Accepted:    428.1K
# Total Submissions: 936.5K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
#
# Example:
#
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
#


from typing import List


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        best = nums[0] + nums[1] + nums[2]

        for a_idx in range(0, len(nums) - 2):
            a_num = nums[a_idx]

            if a_idx != 0 and (nums[a_idx] == nums[a_idx - 1]):
                continue

            b_idx = a_idx + 1
            c_idx = len(nums) - 1
            while b_idx < c_idx:
                result = a_num + nums[b_idx] + nums[c_idx]

                if result > target:
                    # result is too big
                    c_idx -= 1
                elif result < target:
                    # result is too small
                    b_idx += 1
                else:
                    return result

                if abs(result - target) < abs(best - target):
                    best = result

        return best


# @lc code=end

if __name__ == "__main__":
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
