"""
submits:
  - date: 2020-08-06
    minutes: 180
    cheating: false
comment: '这道题的边界条件处理太麻烦了'
labels:
  - max/min elements in sliding window
"""
#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (33.53%)
# Likes:    3846
# Dislikes: 88
# Total Accepted:    269.9K
# Total Submissions: 770K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
#
#
#
#
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
#
#
#
#
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
#
#
#
# Example:
#
#
# Input: [2,1,5,6,2,3]
# Output: 10
#
#
#

from typing import List

# @lc code=start


TESTING = False

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]

        # lefts[i] 表示紧贴着 i 的左边，有多少个数字的高度大于等于 i 的高度（不包含 i 自己）
        lefts = [0] * len(heights)
        # rights[i] 表示紧贴着 i 的右边，有多少个数字的高度大于等于 i 的高度（不包含 i 自己）
        rights = [0] * len(heights)
        # 高度为 heights[i]，且包含 i 的最大的矩形的面积大小就是 heights[i] * (rights[i] + lefts[i] + 1)

        lefts[0] = 0
        for i in range(1, len(heights)):

            if heights[i] == heights[i - 1]:
                lefts[i] = lefts[i - 1] + 1
            elif heights[i] > heights[i - 1]:
                lefts[i] = 0
            elif heights[i] < heights[i - 1]:
                count = 1
                while True:
                    assert heights[i - count] >= heights[i]

                    if i - count == 0:
                        break
                    if heights[i - count - 1] < heights[i]:
                        break
                    count += max(lefts[i - count], 1)

                    assert heights[i - count] >= heights[i]

                lefts[i] = count

                if TESTING:
                    for x in range(i - count, i):
                        assert heights[x] >= heights[i]
                    assert i - count == 0 or heights[i - count - 1] < heights[i], f"heights: {heights}; i: {i}, lefts: {lefts}"

        rights[len(heights) - 1] = 0
        for i in range(len(heights) - 2, -1, -1):

            if heights[i] == heights[i + 1]:
                rights[i] = rights[i + 1] + 1
            elif heights[i] > heights[i + 1]:
                rights[i] = 0
            elif heights[i] < heights[i + 1]:
                count = 1
                while True:
                    assert heights[i + count] >= heights[i]

                    if i + count + 1 == len(heights):
                        break
                    if heights[i + count + 1] < heights[i]:
                        break
                    count += max(rights[i + count], 1)

                    assert heights[i + count] >= heights[i]


                rights[i] = count

                if TESTING:
                    for x in range(i + 1, i + count + 1):
                        assert heights[x] >= heights[i]
                    assert i + count + 1 == len(heights) or heights[i + count + 1] < heights[i], f"heights: {heights}; i: {i}, lefts: {lefts}"


        print("lefts:  ", lefts)
        print("rights: ", rights)

        best_area = 0
        for i in range(len(heights)):
            area = heights[i] * (rights[i] + lefts[i] + 1)
            best_area = max(best_area, area)

        return best_area


# @lc code=end
if __name__ == "__main__":
    TESTING = True
    f = Solution().largestRectangleArea

    import unittest

    t = unittest.TestCase("__init__")
    t.assertEqual(f([2, 1, 5, 6, 2, 3]), 10)
    t.assertEqual(f([10, 11, 12, 13]), 40)
    t.assertEqual(f([13, 12, 11, 10]), 40)
    t.assertEqual(f([10, 10, 10, 10]), 40)
