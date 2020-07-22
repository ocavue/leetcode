"""
submits:
  - date: 2020-07-22
    cheating: true
labels:
  - dp
comment: |
  这道题的关键是寻找动态规划的状态
  中间状态：截止到某个位置 x，s[0:x] 能不能用 word_dict 拼出来
  状态变化：s[O:y] 能不能用 word_dict 拼出来可以根据之前的状态配合 word 的长度得出
"""
#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (38.35%)
# Likes:    4360
# Dislikes: 232
# Total Accepted:    557.1K
# Total Submissions: 1.4M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
#
# Note:
#
#
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
#
#
#

from typing import List

# @lc code=start


class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        """
        >>> f = Solution().wordBreak
        >>> f(s = "leetcode", word_dict = ["leet", "code"])
        True
        >>> f(s = "applepenapple", word_dict = ["apple", "pen"])
        True
        >>> f(s = "catsandog", word_dict = ["cats", "dog", "sand", "and", "cat"])
        False
        >>> f("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
        False
        >>> f("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"])
        False
        """

        # dp 是一个 map，表示截止到 s 的某一个位置为止，是不是可以成功地使用 word_dict 组合出来
        # dp[1] 表示 s[0:1] 能不能使用 word_dict 组合出来
        # dp[x] 表示 s[0:x] 能不能使用 word_dict 组合出来
        # dp[len(s)] 表示 s[0:len(s)] 能不能使用 word_dict 组合出来。这也就是我们要最终返回的结果
        # dp[0] 没有含义，这里为了方便计算设置为 0
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for curr in range(1, len(dp)):
            for word in word_dict:
                prev = curr - len(word)
                if s[prev:curr] == word and dp[prev] is True:
                    dp[curr] = True
                    break
        return dp[len(s)]


# @lc code=end
if __name__ == "__main__":
    import doctest

    doctest.testmod()
