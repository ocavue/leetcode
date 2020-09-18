"""
submits:
  - date: 2020-07-21
    cheating: true
  - date: 2020-09-18
    cheating: true
    minutes: 50
labels:
  - dp
comment: |
  这道题使用动态规划去做。
  状态：一个 map，表示对于所有的 m 和 n 的组合，最多能组成多少个字符串
  初始状态：当有 0 个字符串时，对于每个 m 和 n 的组合，map[(m,n)] = 0
  中间状态：当有 x 个字符串时，对于每个 m 和 n 的组合，map[(m,n)] = ?
  状态转移：当有 x+1 个字符串时候，对于每个 m 和 n 的组合，map[(m,n)] = max( map[(m,n)], map[(m - curr_m, n - curr_n)] )。其中 curr_m 和 curr_n 表示当前的字符串的字符数量

  第二次做，新的感受：
  状态：当有 m 个零，n 个壹，那么对于 strings 的前 i 个数字，最多可以组成多少个数字
       dp(m, n, i) = ?
  所以这其实是一个三维的 dp，只不过因为 i 这个变量我们每次迭代只需要知道 i-1 的状态。所以一个二维数组就可以了。
"""

#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#
# https://leetcode.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (41.87%)
# Likes:    969
# Dislikes: 230
# Total Accepted:    47.6K
# Total Submissions: 112K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# Given an array, strs, with strings consisting of only 0s and 1s. Also two
# integers m and n.
#
# Now your task is to find the maximum number of strings that you can form with
# given m 0s and n 1s. Each 0 and 1 can be used at most once.
#
#
# Example 1:
#
#
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: This are totally 4 strings can be formed by the using of 5 0s
# and 3 1s, which are "10","0001","1","0".
#
#
# Example 2:
#
#
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: You could form "10", but then you'd have nothing left. Better
# form "0" and "1".
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] consists only of digits '0' and '1'.
# 1 <= m, n <= 100
#
#
#

# @lc code=start


from typing import List

from pprint import pprint
from collections import namedtuple
from functools import lru_cache

Pair = namedtuple("Pair", ["ones", "zeros"])


class Solution:
    def findMaxForm(self, strings: List[str], target_zeros: int, target_ones: int) -> int:
        pairs: List[Pair] = []
        for s in strings:
            ones, zeros = 0, 0
            for c in s:
                if c == "0":
                    zeros += 1
                else:
                    ones += 1
            pairs.append(Pair(zeros=zeros, ones=ones))

        dp: List[List[int]] = []
        for z in range(target_zeros + 1):
            dp.append([0] * (target_ones + 1))

        for i, last in enumerate(pairs):
            for z in range(target_zeros, -1,-1):
                for o in range(target_ones, -1,-1):
                    # 不包含 last
                    case1 = dp[z][o]

                    # 包含 last
                    if z >= last.zeros and o >= last.ones:
                        case2 = dp[z - last.zeros][o - last.ones] + 1
                    else:
                        case2 = 0
                    dp[z][o] = max(case1, case2)

                    # if dp[z][o] > 4:
                    #     import pdb;pdb.set_trace()
            # max_val = 0
            # for z in range(target_zeros + 1):
            #     for o in range(target_ones + 1):
            #         max_val = max(max_val, dp[z][o])
            # if max_val > i+1:
            #     import pdb;pdb.set_trace()

        return dp[target_zeros][target_ones]


# @lc code=end

if __name__ == "__main__":
    f = Solution().findMaxForm

    import unittest

    test = unittest.TestCase("__init__")

    test.assertEqual(f(["10", "0001", "111001", "1", "0"], 5, 3), 4)
    test.assertEqual(f(["10", "0", "1"], 1, 1), 2)
    test.assertEqual(f(["0000", "000000"], 1, 1), 0)
    test.assertEqual(f(["10", "0001", "111001", "1", "0"], 3, 4), 3)
    test.assertEqual(f(["0", "1", "00001111"], 4, 4), 2)
