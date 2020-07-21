"""
submits:
  - date: 2020-04-30
    cheating: false
"""

#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
# https://leetcode.com/problems/4sum-ii/description/
#
# algorithms
# Medium (52.39%)
# Likes:    985
# Dislikes: 70
# Total Accepted:    97.2K
# Total Submissions: 185.1K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j,
# k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
#
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤
# N ≤ 500. All integers are in the range of -2^28 to 2^28 - 1 and the result is
# guaranteed to be at most 2^31 - 1.
#
# Example:
#
#
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# Output:
# 2
#
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
#
#
#
#
#
# @lc code=start

from typing import List
from collections import Counter


def four_sum_count_v1(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    layer1: List[List[int]] = []
    for sum in sorted([a + b for a in A for b in B]):
        if layer1 and (layer1[-1][0] == sum):
            layer1[-1][1] += 1
        else:
            layer1.append([sum, 1])

    layer2: List[List[int]] = []
    for sum in sorted([c + d for c in C for d in D]):
        if layer2 and (layer2[-1][0] == sum):
            layer2[-1][1] += 1
        else:
            layer2.append([sum, 1])

    i, j = 0, len(layer2) - 1
    count = 0
    while i < len(layer1) and j >= 0:
        sum = layer1[i][0] + layer2[j][0]
        if sum > 0:
            j -= 1
        elif sum < 0:
            i += 1
        else:
            count += layer1[i][1] * layer2[j][1]
            j -= 1
            i += 1

    return count


def four_sum_count_v2(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    # AB = Counter(a + b for a in A for b in B)
    # CD = Counter(c + d for c in C for d in D)
    # count = 0
    # for ab, ab_count in AB.items():
    #     count += CD[-ab] * ab_count
    # return count
    AB = Counter(a + b for a in A for b in B)
    return sum(AB[-c - d] for c in C for d in D)


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        return four_sum_count_v2(A, B, C, D)


# @lc code=end
if __name__ == "__main__":
    four_sum_count = four_sum_count_v2
    print(four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2)
    print(four_sum_count([-1, -1], [-1, 1], [-1, 1], [1, -1]) == 6)
