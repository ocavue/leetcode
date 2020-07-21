"""
submits:
  - date: 2020-04-08
    cheating: false
"""

#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (30.88%)
# Likes:    3412
# Dislikes: 141
# Total Accepted:    299.8K
# Total Submissions: 966.5K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
#
# Example 1:
#
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#


from typing import List

# @lc code=start


def max_product(nums: List[int]) -> int:
    # The maximum product for number in nums[i,k] where 0 <= i <= k
    max_product_until_k = [None for i in range(len(nums))]
    # The minimum product for number in nums[i,k] where 0 <= i <= k
    min_product_until_k = [None for i in range(len(nums))]
    # I don't have to save the FULL list of max_product_until_k, which take O(n) space.

    for k, num in enumerate(nums):
        if k == 0:
            max_product_until_k[k] = num
            min_product_until_k[k] = num
        else:
            possibles = [
                num,
                num * max_product_until_k[k - 1],
                num * min_product_until_k[k - 1],
            ]
            max_product_until_k[k] = max(possibles)
            min_product_until_k[k] = min(possibles)

    return max(max_product_until_k)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return max_product(nums)


# @lc code=end
if __name__ == "__main__":
    assert (max_product([2, 3, -2, 4])) == 6
    assert (max_product([-2])) == -2
