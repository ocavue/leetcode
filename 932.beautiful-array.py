"""
submits:
- date: 2020-10-18
  minutes: 20
  cheating: true
labels:
- 分而治之
comment: |
  这道题感觉没什么意思，主要是数学部分很难想出来。不过背后的数学思路还算是简单吧（如果能想出来的话）。
  首先，如果一个数组是美的，那么给数组中的每个数字都加上一个常量 K，生成的新数组也是美的。
  其次，只要能保证 A[i] 和 A[j] 的奇偶性不同，那么就能保证 A[k] * 2 = A[i] + A[j] 永远不成立。
  所以，我们的方案是，将数组拆分成左右两部分，左边全是偶数，右边全是奇数。两部分数组都是美的，那么容易证明，组成而成的新数组也是美的。
"""
# @lc app=leetcode id=932 lang=python3
#
# [932] Beautiful Array
#
# https://leetcode.com/problems/beautiful-array/description/
#
# algorithms
# Medium (59.27%)
# Likes:    384
# Dislikes: 493
# Total Accepted:    13.6K
# Total Submissions: 22.4K
# Testcase Example:  '4'
#
# For some fixed N, an array A is beautiful if it is a permutation of the
# integers 1, 2, ..., N, such that:
#
# For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] +
# A[j].
#
# Given N, return any beautiful array A.  (It is guaranteed that one
# exists.)
#
#
#
# Example 1:
#
#
# Input: 4
# Output: [2,1,4,3]
#
#
#
# Example 2:
#
#
# Input: 5
# Output: [3,1,2,5,4]
#
#
#
#
# Note:
#
#
# 1 <= N <= 1000
#
#
#
#
#
#

List = list

# @lc code=start


class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        if N == 0:
            return []
        if N == 1:
            return [1]
        if N == 2:
            return [1, 2]

        # range(1, N+1) 由 N//2 和偶数和 N//2 + N%2 个奇数 组成

        odd_part = self.beautifulArray((N // 2) + (N % 2))
        even_part = self.beautifulArray(N // 2)

        result: List[int] = []
        for num in odd_part:
            result.append(2 * num - 1)
        for num in even_part:
            result.append(2 * num)
        return result


# @lc code=end
