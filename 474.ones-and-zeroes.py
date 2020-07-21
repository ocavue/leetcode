"""
submits:
  - date: 2020-07-21
    cheating: true
labels:
  - dp
comment: |
  这道题使用动态规划去做。
  状态：一个 map，表示对于所有的 m 和 n 的组合，最多能组成多少个字符串
  初始状态：当有 0 个字符串时，对于每个 m 和 n 的组合，map[(m,n)] = 0
  中间状态：当有 x 个字符串时，对于每个 m 和 n 的组合，map[(m,n)] = ?
  状态转移：当有 x+1 个字符串时候，对于每个 m 和 n 的组合，map[(m,n)] = max( map[(m,n)], map[(m - curr_m, n - curr_n)] )。其中 curr_m 和 curr_n 表示当前的字符串的字符数量
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

from typing import List

from pprint import pprint

# @lc code=start
class Solution:
    def findMaxForm(self, strings: List[str], target_zeros: int, target_ones: int) -> int:
        # map[zeros][ones] = the max number of strings that can be formed with zeros 0's and ones 1's
        map = []
        for i in range(0, target_zeros + 1):
            row = [0] * (target_ones + 1)
            map.append(row)

        # assert len(map) == target_zeros + 1
        # for row in map:
        #     assert len(row) == target_ones + 1

        for string in strings:
            # print("[debug] string", string)
            zeros, ones = 0, 0
            for char in string:
                if char == "0":
                    zeros += 1
                else:
                    ones += 1

            for o in range(target_ones, -1, -1):
                for z in range(target_zeros, -1, -1):
                    # print(f"z: {z} o: {o}")

                    prev_zeros = z - zeros
                    prev_ones = o - ones
                    if 0 <= prev_zeros <= target_zeros and 0 <= prev_ones <= target_ones:
                        prev_num = map[prev_zeros][prev_ones]
                        curr_num = map[z][o]

                        map[z][o] = max(prev_num + 1, curr_num)
            # pprint(map)

        # pprint(map)
        return map[target_zeros][target_ones] or 0


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
