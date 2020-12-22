"""
submits:
- date: 2020-12-22
  cheating: false
  minutes: 29
labels:
- hash_table
"""
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (17.06%)
# Likes:    1028
# Dislikes: 2218
# Total Accepted:    166.7K
# Total Submissions: 969.3K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
#
# Example 1:
#
#
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o
# +------------->
# 0  1  2  3  4
#
#
# Example 2:
#
#
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
#
#
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
#
#

# @lc code=start
from collections import defaultdict
from typing import List, Dict


def cal_km(x1, y1, x2, y2):
    if x1 == x2:
        k = float("inf")
        m = x1
    else:
        k = (y1 - y2) / (x1 - x2)
        m = y1 - k * x1
    return k, m


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        # line = (x) => k*x + m

        counter = defaultdict(int)
        for x, y in points:
            counter[(x, y)] += 1

        ps: List[tuple] = []
        max_weight = 0
        for point, weight in counter.items():
            ps.append((point[0], point[1], weight))
            max_weight = max(max_weight, weight)

        all_km: Dict[tuple, int] = {}
        while ps:
            x1, y1, w1 = ps.pop()
            curr_km: Dict[tuple, int] = defaultdict(int)
            for x2, y2, w2 in ps:
                k, m = cal_km(x1, y1, x2, y2)
                if (k, m) not in all_km:
                    curr_km[(k, m)] += w2
            assert len(curr_km.keys() & all_km.keys()) == 0
            for km, point_num in curr_km.items():
                all_km[(km)] = point_num + w1
        return max(all_km.values()) if all_km else max_weight


# @lc code=end
if __name__ == "__main__":
    from tool import t

    f = Solution().maxPoints
    t(f([[1, 1], [2, 2], [3, 3]]), 3)
    t(f([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]), 4)
    t(f([[0, 0]]), 1)

