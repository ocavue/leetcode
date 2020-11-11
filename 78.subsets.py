"""
submits:
- date: 2020-11-11
  minutes: 12
  cheating: true
labels:
- bit-manipulation
comment: |
  这道题本身不难，但是如果要使用 bit manipulation 去做的话的确有点难想到。长度为 n 的数组一共有 2^n 个 subsets，可以分别用
  0 0 ... 0
  0 0 ... 1
  ....
  1 1 ... 1
  这样 2^n 个二进制数去表示。其中 1 表示这个位置的元素存在与 subset 中，0 则表示不存在。
"""
#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (63.12%)
# Likes:    4694
# Dislikes: 94
# Total Accepted:    662.9K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#

from typing import List

# @lc code=start

# # 从 nums[i:j] 中挑选 k 个数字，一共有多少中可能的 subsets
# def get_subsets(nums: List[int], i: int, j: int, k: int) -> List[List[int]]:
#     if k == 0:
#         return [[]]
#     if k == 1:
#         return [[n] for n in nums[i:j]]
#     if j - i < k:
#         return []
#     if j - i == k:
#         return [list(nums[i:j])]

#     subsets: List[List[int]] = []
#     # 包含 result[j-1]
#     for subset in get_subsets(nums, i, j - 1, k - 1):
#         subset.append(nums[j - 1])
#         subsets.append(subset)
#     # 不包含 result[j-1]
#     for subset in get_subsets(nums, i, j - 1, k):
#         subsets.append(subset)
#     return subsets


class Solution:
    def subsets(self, nums):
        subsets = []
        for mask in range(0, 2 ** len(nums)):
            subset = []
            for i in range(len(nums)):
                if (mask >> i) & 1:
                    subset.append(nums[i])
            subsets.append(subset)
        return subsets


# @lc code=end
if __name__ == "__main__":
    from tool import test

    t = test()
    f = Solution().subsets

    t.assertEqual(
        sorted(f([1, 2, 3])),
        sorted(
            [
                [3],
                [1],
                [2],
                [1, 2, 3],
                [1, 3],
                [2, 3],
                [1, 2],
                [],
            ]
        ),
    )
