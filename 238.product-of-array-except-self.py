#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (58.71%)
# Likes:    3927
# Dislikes: 334
# Total Accepted:    415.7K
# Total Submissions: 703.4K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
#
# Example:
#
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#
#
# Constraint: It's guaranteed that the product of the elements of any prefix or
# suffix of the array (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
#
#

# @lc code=start
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    product_all = 1
    zero_count = 0
    for i in nums:
        if i != 0:
            product_all *= i
        else:
            zero_count += 1
            if zero_count >= 2:
                break

    if zero_count >= 2:
        return [0] * len(nums)
    elif zero_count == 1:
        return [product_all if i == 0 else 0 for i in nums]
    else:
        return [int(product_all / i) for i in nums]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return product_except_self(nums)


# @lc code=end
if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([0, 1, 2, 3, 4]) == [24, 0, 0, 0, 0]
    assert product_except_self([0, 0, 1, 1]) == [0, 0, 0, 0]
