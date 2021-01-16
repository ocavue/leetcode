"""
submits:
- date: 2021-01-16
  minutes: 87
  cheating: true
labels:
- dp
comment: |
  这道题蛮不错的。
  状态 dp(n,k)  表示使用 1~n 一共 n 个数字，组成 k 个 inverse pairs 的所有 array 的数量。
  那么我们可以考虑状态的转换关系：

  我们先准备一个长度为 n-1 的数组，
  如果我们把数字 n 放在最后面，那么所有的 inverse pairs 都由之前的 n-1 个数字组成
  如果我们把数字 n 放在倒数第二位，那么新增加的数字 n 可以提供一个 inverse pairs，剩下的 inverse pairs 都由之前的 n-1 个数字组成
  。。。
  如果我们把数字 n 放在第一位，那么新增加的数字 n 可以提供 n-1 个 inverse pairs，剩下的 inverse pairs 都由之前的 n-1 个数字组成

  dp(n,k) = dp(n-1, k) + dp(n-1,k-1) + ... + dp(n-1,k-(n-1))

  现在有意思的来了。如果我们计算 dp(n,k) - dp(n,k-1)，我们就能得出 dp(n, k) = dp(n, k - 1) + dp(n - 1, k) - dp(n - 1, k - n)





"""
#
# @lc app=leetcode id=629 lang=python3
#
# [629] K Inverse Pairs Array
#
# https://leetcode.com/problems/k-inverse-pairs-array/description/
#
# algorithms
# Hard (31.32%)
# Likes:    369
# Dislikes: 77
# Total Accepted:    12.3K
# Total Submissions: 39.1K
# Testcase Example:  '3\n0'
#
# Given two integers n and k, find how many different arrays consist of numbers
# from 1 to n such that there are exactly k inverse pairs.
#
# We define an inverse pair as following: For ith and jth element in the array,
# if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.
#
# Since the answer may be very large, the answer should be modulo 10^9 + 7.
#
# Example 1:
#
#
# Input: n = 3, k = 0
# Output: 1
# Explanation:
# Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0
# inverse pair.
#
#
#
#
# Example 2:
#
#
# Input: n = 3, k = 1
# Output: 2
# Explanation:
# The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
#
#
#
#
# Note:
#
#
# The integer n is in the range [1, 1000] and k is in the range [0, 1000].
#
#
#
#
#

# @lc code=start

MOD = (10 ** 9) + 7


class Solution:
    def kInversePairs(self, n, k):
        mem = []
        for i in range(n + 1):
            mem.append([-1] * (k + 1))

        def dp(n, k):
            if n == 1:
                if k == 0:
                    return 1
                else:
                    return 0

            if k < 0:
                return 0
            # if  k > (n - 1) * n / 2:
            #     return 0

            if mem[n][k] == -1:
                res = dp(n, k - 1) + dp(n - 1, k) - dp(n - 1, k - n)
                mem[n][k] = res
            return mem[n][k]

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp(i, j)

        return dp(n, k) % MOD


# @lc code=end
if __name__ == "__main__":
    from tool import tt

    t = tt(Solution().kInversePairs)
    t([1, 0], 1)
    t([1, 1], 0)
    t([1, 2], 0)
    t([1, 3], 0)

    t([2, 0], 1)
    t([2, 1], 1)
    t([2, 2], 0)
    t([2, 3], 0)
    t([2, 4], 0)

    t([3, 0], 1)
    t([3, 1], 2)
    t([3, 2], 2)
    t([3, 3], 1)
    t([3, 4], 0)
    t([3, 5], 0)

    t([100, 100], 959322173)
    t([1000, 1000], 663677020)
