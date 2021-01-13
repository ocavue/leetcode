#
# @lc app=leetcode id=546 lang=python3
#
# [546] Remove Boxes
#
# https://leetcode.com/problems/remove-boxes/description/
#
# algorithms
# Hard (43.51%)
# Likes:    789
# Dislikes: 55
# Total Accepted:    17.6K
# Total Submissions: 39.9K
# Testcase Example:  '[1,3,2,2,2,3,4,3,1]\r'
#
# Given several boxes with different colors represented by different positive
# numbers.
# You may experience several rounds to remove boxes until there is no box left.
# Each time you can choose some continuous boxes with the same color (composed
# of k boxes, k >= 1), remove them and get k*k points.
# Find the maximum points you can get.
#
#
# Example 1:
#
#
# Input: boxes = [1,3,2,2,2,3,4,3,1]
# Output: 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
# ----> [1, 3, 3, 3, 1] (1*1=1 points)
# ----> [1, 1] (3*3=9 points)
# ----> [] (2*2=4 points)
#
#
#
# Constraints:
#
#
# 1 <= boxes.length <= 100
# 1 <= boxes[i] <= 100
#
#
#

from typing import List, Tuple

# @lc code=start

from functools import lru_cache


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache()
        def dfs(i: int, j: int, k: int) -> int:
            if j <= i:
                return 0

            v = boxes[i]

            while i + 1 < j and boxes[i + 1] == v:
                i += 1
                k += 1

            assert boxes[i] == v

            # case1: 删除 boxes[i] 以及之前 k 个 v（一共 k+1 个 v）
            res1 = (k + 1) ** 2 + dfs(i + 1, j, 0)

            # case2：不删除 boxes[i]。等到后面再利用 boxes[i] 以及之前 k 个 v（一共 k+1 个 v）
            res2 = 0
            for x in range(i + 1, j):
                if boxes[x] == v:
                    res2 = max(res2, dfs(i + 1, x, 0) + dfs(x, j, k + 1))

            return max(res1, res2)

        return dfs(0, len(boxes), 0)


# @lc code=end

