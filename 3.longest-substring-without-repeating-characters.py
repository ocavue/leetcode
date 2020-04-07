#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (29.63%)
# Likes:    8252
# Dislikes: 500
# Total Accepted:    1.4M
# Total Submissions: 4.7M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
#
# Example 2:
#
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
#
# Example 3:
#
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
#
#
#
#
#
#

# @lc code=start


def length_of_longest_substring(s: str) -> int:
    """
    >>> length_of_longest_substring('abcabcbb')
    3
    >>> length_of_longest_substring('bbbbb')
    1
    >>> length_of_longest_substring('pwwkew')
    3
    """
    if len(s) == 0:
        return 0

    i, j = 0, 0
    chars = set([s[0]])
    max_len = 1
    while j <= len(s) - 2:
        # assert 0 <= j <= len(s) - 2
        j += 1
        # assert 0 <= j <= len(s) - 1
        char_j = s[j]
        if char_j in chars:
            while i <= j and char_j in chars:
                char_i = s[i]
                assert char_i in chars
                chars.remove(char_i)
                i += 1

        # assert char_j not in chars
        chars.add(char_j)

        # assert s[i] in chars
        # assert s[j] in chars
        # assert len(chars) == j - i + 1
        max_len = max(len(chars), max_len)
    return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return length_of_longest_substring(s)


# @lc code=end
if __name__ == "__main__":
    import doctest

    doctest.testmod()
