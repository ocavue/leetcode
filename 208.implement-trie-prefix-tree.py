"""
submits:
  - date: 2020-08-01
    cheating: false
    minutes: 9
labels: []
comment:
"""

#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (44.03%)
# Likes:    3269
# Dislikes: 50
# Total Accepted:    328.4K
# Total Submissions: 670.4K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
#
#
# Note:
#
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
#
#
#

# @lc code=start
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.search_set = set()
        self.prefix_set = set()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        assert len(word) >= 1

        self.search_set.add(word)
        for i in range(1, len(word) + 1):
            self.prefix_set.add(word[0:i])
        self.prefix_set.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.search_set

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return prefix in self.prefix_set


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
if __name__ == "__main__":

    trie = Trie()

    # fmt:off
    assert trie.insert("apple")     is None
    assert trie.search("apple")     is True
    assert trie.search("app")       is False
    assert trie.startsWith("app")   is True
    assert trie.insert("app")       is None
    assert trie.search("app")       is True
    assert trie.startsWith("a")     is True
    assert trie.insert("a")         is None
    assert trie.search("a")         is True
