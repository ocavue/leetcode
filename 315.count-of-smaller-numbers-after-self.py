"""
submits:
- date: 2020-09-13
  cheating: true
  minutes: 50
lables:
- merge-sort
comment: |
  这道题需要使用 Merge sort 去解。merge sort 的特点就是所有小于当前数的数字会移动到当前数字的左边，
  这样的话（从另外一个方向的话就是所有大于当前数字的数会移动到当前数字的右边）。这样在每次移动的时候我们
  就有机会去增加数字的计数。
  另外一个有趣的地方是这道题从后向前处理mergesort，这样可以加快算法复杂度
"""
#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (40.71%)
# Likes:    1926
# Dislikes: 72
# Total Accepted:    114.7K
# Total Submissions: 280.6K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
#
# Example:
#
#
# Input: [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
#

# @lc code=start
from typing import List, Tuple


class Solution:
    def countSmaller(self, input_nums: List[int]) -> List[int]:
        result = [0] * len(input_nums)

        nums = [(value, index) for index, value in enumerate(input_nums)]

        def merge_sort(nums: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if len(nums) <= 1:
                return nums
            half = len(nums) // 2

            left, right = merge_sort(nums[:half]), merge_sort(nums[half:])
            # left 和 right 分别都是递增的

            for i in range(len(nums))[::-1]:  # 按照从尾部到头部遍历
                if right and left:
                    if right[-1] > left[-1]:
                        # 这说明 right[-1] 大于 left 中的每一个值。右边的数字比较大的话，result 就不需要变。
                        nums[i] = right.pop()
                    else:
                        # 这说明 left[-1] 大于 right 中的每一个值。那么 result 中要增加 len(right) 个数字
                        nums[i] = left.pop()
                        index = nums[i][1]
                        result[index] += len(right)
                elif left:
                    nums[i] = left.pop()
                elif right:
                    nums[i] = right.pop()
            return nums

        merge_sort(nums)
        return result


# @lc code=end
if __name__ == "__main__":
    for input, expected in [[[5, 2, 6, 1], [2, 1, 1, 0]]]:
        result = Solution().countSmaller(input)
        assert result == expected, f"expect: {expected}, result: {result}"
