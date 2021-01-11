"""

submits:
- date: 2021-01-11
  minutes: 16
  cheating: false
labels:
- dp
"""
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (24.62%)
# Likes:    1740
# Dislikes: 2414
# Total Accepted:    167.9K
# Total Submissions: 679.7K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# Given a list of non-negative numbers and a target integer k, write a function
# to check if the array has a continuous subarray of size at least 2 that sums
# up to a multiple of k, that is, sums up to n*k where n is also an
# integer.
#
#
#
# Example 1:
#
#
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to
# 6.
#
#
# Example 2:
#
#
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and
# sums up to 42.
#
#
#
# Constraints:
#
#
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit
# integer.
#
#
#

# @lc code=start


class Solution:
    def checkSubarraySum(self, nums, k):
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1] == 0:
                    return True
            return False
        else:
            # mods[x] = v 表示 sum(nums[0:x]) % k == v
            mods = {0: 0}  # magic!
            mod = 0
            for index, num in enumerate(nums):
                mod = (mod + num) % k
                if mod in mods:
                    if index + 1 - mods[mod] >= 2:
                        return True
                else:
                    mods[mod] = index + 1
            return False


# @lc code=end

if __name__ == "__main__":
    from tool import t

    f = Solution().checkSubarraySum

    t(f([23, 2, 4, 6, 7], 6), True)
    t(f([1, 1], 2), True)
    t(f([1, 0], 2), False)

