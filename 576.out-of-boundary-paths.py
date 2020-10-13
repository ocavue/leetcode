"""
submits:
- cheating: true
  minutes: 58
  date: 2020-10-13
labels:
- dp
comment: |
  这道题中体现了一种「逆向」的 dp 思想。

  首先这道题有三个在 dp 过程中变化的变量: 坐标 x, y 和步数 i。所以我一开始的想法就是构造出一个三维数组，表达「走到第 i 步时，位置在 x, y 的
  路径有多少个」，但是内存过多。优化方案是减少 step 的数量：因为步数为 N 的 dp 只会和步数为 N-1 的 dp 相关，所以只需要两个二维数组就可以了

  还看到另外一个有意思的解法：不将 xy 视为在 xy 结束的点，而是将 xy 视为在 xy 开始的点。换句话说，不是从起始点出发向外走，而是从边缘出发向内走。代码结构其实和上一种类似，但是这个思路很有意思


"""
#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#
# https://leetcode.com/problems/out-of-boundary-paths/description/
#
# algorithms
# Medium (35.45%)
# Likes:    620
# Dislikes: 139
# Total Accepted:    31.1K
# Total Submissions: 87.6K
# Testcase Example:  '2\n2\n2\n0\n0'
#
# There is an m by n grid with a ball. Given the start coordinate (i,j) of the
# ball, you can move the ball to adjacent cell or cross the grid boundary in
# four directions (up, down, left, right). However, you can at most move N
# times. Find out the number of paths to move the ball out of grid boundary.
# The answer may be very large, return it after mod 10^9 + 7.
#
#
#
# Example 1:
#
#
# Input: m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:
#
#
#
# Example 2:
#
#
# Input: m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:
#
#
#
#
#
# Note:
#
#
# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].
#
#
#

# @lc code=start

MOD = 10 ** 9 + 7


class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:

        # dp[i][j] 表示在走了若干步骤后，有几种路径会在 [i,j] 点结束。
        # 使用两个二维数组表示走了 i 步和走了 i-1 步时候的结果。
        old_dp = []
        for _ in range(m):
            old_dp.append([0] * n)

        new_dp = []
        for _ in range(m):
            new_dp.append([0] * n)

        old_dp[i][j] = 1

        out_paths = 0

        # 走 N  步
        for _ in range(N):

            for i in range(m):
                for j in range(n):
                    new_dp[i][j] = 0

            for i in range(m):
                for j in range(n):
                    curr = old_dp[i][j]

                    # 当前 在[i, j]，下一步向四个方向走

                    if i > 0:
                        new_dp[i - 1][j] += curr
                    else:
                        out_paths += curr  # 提前出去了，拜拜了您恁

                    if i < m - 1:
                        new_dp[i + 1][j] += curr
                    else:
                        out_paths += curr

                    if j > 0:
                        new_dp[i][j - 1] += curr
                    else:
                        out_paths += curr

                    if j < n - 1:
                        new_dp[i][j + 1] += curr
                    else:
                        out_paths += curr

                    # new_dp[i][j] = paths
            old_dp, new_dp = new_dp, old_dp
        # print(dp)

        return out_paths % MOD


# @lc code=end
if __name__ == "__main__":
    f = Solution().findPaths
    print(f(m=2, n=2, N=2, i=0, j=0))
    print(f(m=1, n=3, N=3, i=0, j=1))
