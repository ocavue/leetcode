"""
submits:
  - date: 2020-08-12
    minutes: 40
    cheating: false
"""

# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (29.84%)
# Likes:    2262
# Dislikes: 399
# Total Accepted:    257.4K
# Total Submissions: 789.6K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
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
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
#
#
# Example 2:
#
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
#
#

# @lc code=start

from typing import List, Optional
from collections import defaultdict
from functools import lru_cache


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_lens = set()

    def add_word(self, word: str):
        node: TrieNode = self.root
        for char in word:
            node = node.children[char]
        node.is_word = True

        self.word_lens.add(len(word))

    def search(self, prefix: str) -> Optional[TrieNode]:
        node: TrieNode = self.root
        for char in prefix:
            node = node.children.get(char)
            if not node:
                return None
        return node


@lru_cache()
def word_break(s: str, trie: Trie, i: int) -> List[str]:
    """
    获得 s[i:] 的 word_break
    """
    if not s:
        return []

    result: List[str] = []

    for word_len in trie.word_lens:

        if len(s) - i == word_len:
            node = trie.search(s[i:])
            if node and node.is_word:
                result.append(s[i:])
        else:
            prefix = s[i : i + word_len]
            node = trie.search(prefix)
            if node and node.is_word:
                for suffixes in word_break(s, trie, i + word_len):
                    result.append(prefix + " " + suffixes)

    print(f"result for {repr(s)} {i} is {result}")
    return result


class Solution:
    def wordBreak(self, s: str, words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add_word(word)

        return word_break(s, trie, 0)


# @lc code=end

if __name__ == "__main__":
    for s, words, expected in [
        ["catsanddog", ["cat", "cats", "and", "sand", "dog"], ["cats and dog", "cat sand dog"]],
        [
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"],
            ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
        ],
        ["catsandog", ["cats", "dog", "sand", "and", "cat"], []],
    ]:
        expected = set(expected)
        received = set(Solution().wordBreak(s, words))
        assert expected == received, "wrong result\nexpected: {}\nreceived: {}".format(expected, received)

# Example 1:
#
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
#
#
# Example 2:
#
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
#
#
