"""
submits:
- date: 2020-10-27
  minutes: 38
  cheating: false
labels: [dp]
"""
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/
#
# algorithms
# Medium (47.91%)
# Likes:    834
# Dislikes: 35
# Total Accepted:    33.4K
# Total Submissions: 69.6K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# A sequence X_1, X_2, ..., X_n is fibonacci-like if:
#
#
# n >= 3
# X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
#
#
# Given a strictly increasing array A of positive integers forming a sequence,
# find the length of the longest fibonacci-like subsequence of A.  If one does
# not exist, return 0.
#
# (Recall that a subsequence is derived from another sequence A by deleting any
# number of elements (including none) from A, without changing the order of the
# remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6,
# 7, 8].)
#
#
#
#
#
#
# Example 1:
#
#
# Input: [1,2,3,4,5,6,7,8]
# Output: 5
# Explanation:
# The longest subsequence that is fibonacci-like: [1,2,3,5,8].
#
#
# Example 2:
#
#
# Input: [1,3,7,11,12,14,18]
# Output: 3
# Explanation:
# The longest subsequence that is fibonacci-like:
# [1,11,12], [3,11,14] or [7,11,18].
#
#
#
#
# Note:
#
#
# 3 <= A.length <= 1000
# 1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
# (The time limit has been reduced by 50% for submissions in Java, C, and
# C++.)
#
#
#


# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        nums = {num: index for index, num in enumerate(A)}

        # dp [j][i] 表示 以 A[j] 作为最后一项，A[i] 作为倒数第二项的 fibonacci-like subsequence 的长度是多少。
        # 其中 0 <= i < j < len(A)
        # dp: List[List[int]] = []
        # for _ in range(len(A)):
        #     dp.append([0] * len(A))
        dp = defaultdict(int)

        max_len = 0
        for j in range(1, len(A)):
            for i in range(0, j):
                assert 0 <= i < j < len(A)
                assert A[i] < A[j]

                x = A[j] - A[i]
                if x in nums and x < A[i]:
                    dp[(j,i)] = dp[(i, nums[x])] + 1
                else:
                    dp[(j,i)] = 2
                max_len = max(max_len, dp[(j,i)])
        # print(dp)
        return max_len if max_len >= 3 else 0


# @lc code=end
if __name__ == "__main__":
    from tool import test

    t = test()
    f = Solution().lenLongestFibSubseq
    t.assertEqual(f([1, 2, 3, 4, 5, 6, 7, 8]), 5)
    # t.assertEqual(f([1, 3, 7, 11, 12, 14, 18]), 3)
