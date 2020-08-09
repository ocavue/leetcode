"""
submits:
  - date: 2020-08-09
    minutes: 15
    cheating: false
labels: [dfs, dp]
comment: |
  我觉得这道题非常好地展示了递归和动态规划之间的相互转化。
  我一开始使用了递归去完成这道题（更确切的说，是 DFS）。但是如果我每一轮迭代中不使用
  子字符串 s1,s2,s3，而是使用 index i1,i2,i3（其中 i3 = i1+i2），我就得到了一个
  用两个数字作为参数的递归函数，紧接着我就可以把它转化为一个动态规划问题。也就是通过
  一个二维矩阵去描述「当使用 s1 的前 x 个字符以及 s2 的前 y 个字符，是否能拼出来 s3 的
  前 x+y 个字符」。
"""
#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (30.17%)
# Likes:    1470
# Dislikes: 88
# Total Accepted:    156.2K
# Total Submissions: 496.5K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#
#
#

# @lc code=start

from functools import lru_cache


@lru_cache()
def is_interleave(s1: str, s2: str, s3: str) -> bool:
    if not s1:
        return s2 == s3
    if not s2:
        return s1 == s3

    if s1[0] == s2[0] == s3[0]:
        return is_interleave(s1[1:], s2, s3[1:]) or is_interleave(s1, s2[1:], s3[1:])
    if s1[0] == s3[0]:
        return is_interleave(s1[1:], s2, s3[1:])
    if s2[0] == s3[0]:
        return is_interleave(s1, s2[1:], s3[1:])
    return False


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        return is_interleave(s1, s2, s3)


# @lc code=end
if __name__ == "__main__":
    f = Solution().isInterleave

    assert f("aabcc", "dbbca", "aadbbcbcac",) is True
    assert f("aabcc", "dbbca", "aadbbbaccc",) is False
