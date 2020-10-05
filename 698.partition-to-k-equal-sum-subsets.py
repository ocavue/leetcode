"""
submits:
- date: 2020-10-05
  minute: 20
  cheating: true
commnet: |
  这道题很暴力
"""
#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (44.51%)
# Likes:    2201
# Dislikes: 132
# Total Accepted:    97.4K
# Total Submissions: 216.5K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into k non-empty subsets whose sums are all
# equal.
#
#
#
# Example 1:
#
#
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
#
#
#
#
# Note:
#
#
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.
#
#
#

# @lc code=start


class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        target = sum(nums) // k
        groups = [0] * k

        nums.sort(reverse=True)  # 可以加快速度

        if nums[0] > target:
            return False

        # 尝试把 nums[i] 放到 groups[j:] 中的每一个位置
        def search(i: int, j: int):
            if i == len(nums):
                return True

            for k in range(j, len(groups)):
                groups[k] += nums[i]

                if groups[k] > target:
                    pass
                elif groups[k] == target:
                    if search(i + 1, j + 1):
                        return True
                else:
                    if search(i + 1, j):
                        return True
                groups[k] -= nums[i]
            return False

        return search(0, 0)


# @lc code=end

if __name__ == "__main__":
    from tool import test

    t = test()
    f = Solution().canPartitionKSubsets
    t.assertEqual(f([4, 3, 2, 3, 5, 2, 1], 4), True)

