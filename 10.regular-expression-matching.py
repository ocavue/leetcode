#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (26.23%)
# Likes:    3652
# Dislikes: 638
# Total Accepted:    392K
# Total Submissions: 1.5M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
#
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
#
#
# Example 1:
#
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
#
#
# Example 3:
#
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
# Example 4:
#
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore,
# it matches "aab".
#
#
# Example 5:
#
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
#
#
#


# @lc code=start

from typing import List


def parse_pattern(p: str):
    """
    >>> parse_pattern('aaa')
    ['a', 'a', 'a']
    >>> parse_pattern('a.a')
    ['a', '.', 'a']
    >>> parse_pattern('a.*a*')
    ['a', '.*', 'a*']
    >>> parse_pattern('a.*a.*')
    ['a', '.*', 'a', '.*']
    >>> parse_pattern('....*....*')
    ['.', '.', '.', '.*', '.', '.', '.', '.*']
    >>> parse_pattern('a')
    ['a']
    >>> parse_pattern('')
    []
    >>> parse_pattern('a*')
    ['a*']
    >>> parse_pattern(".*a*aa*.*b*.c*.*a*")
    ['.*', 'a*', 'a', 'a*', '.*', 'b*', '.', 'c*', '.*', 'a*']
    """
    tokens = []

    i = 0
    while i < len(p):
        if i == len(p) - 1:
            tokens.append(p[-1])
            i += 1
        else:
            start, end = p[i], p[i + 1]
            if end == "*":
                tokens.append(start + end)
                i += 2
            else:
                tokens.append(start)
                i += 1

    return tokens


def merge_tokens(tokens):
    """
    >>> merge_tokens([])
    []
    >>> merge_tokens(['.*'])
    ['.*']
    >>> merge_tokens(['a', 'a'])
    ['a', 'a']
    >>> merge_tokens(['a', 'a*', 'a*', 'a*', 'a*', 'a*', 'b'])
    ['a', 'a*', 'b']
    """
    merged_tokens = []
    for token in tokens:
        if merged_tokens and merged_tokens[-1] == token and len(token) == 2:
            pass
        else:
            merged_tokens.append(token)

    return merged_tokens


def build_sm(tokens):
    class State:
        def __init__(self, token_index: int, previous_state: "State"):
            self._token_index = token_index
            self.previous_state = previous_state

        def match_char(self, char) -> List["State"]:
            if self.token_index >= len(tokens):
                return []
            token = tokens[self.token_index]

            if len(token) == 1:
                if token == ".":
                    return [State(self.token_index + 1, self)]
                else:
                    return [State(self.token_index + 1, self)] if token == char else []

            else:
                states = State(self.token_index + 1, self).match_char(char)
                is_match = (token == ".*") or (token[0] == char)
                if is_match:
                    states.append(State(self.token_index, self))
                return states

                # if token == ".*":
                #     return [State(self.token_index, self), State(self.token_index + 1, self)]
                # else:
                #     if token[0] == char:
                #         return [State(self.token_index, self), State(self.token_index + 1, self)]
                #     else:
                #         return [ ]

        def is_done(self) -> bool:
            if self.token_index >= len(tokens):
                return True

            reset_tokens = [tokens[i] for i in range(self.token_index, len(tokens))]
            if all(len(token) == 2 for token in reset_tokens):
                return True
            else:
                return False

        def __repr__(self):
            if self.token_index >= len(tokens):
                token = "OutOfIndex"
            else:
                token = tokens[self.token_index]
            return "<State index={} token={}> <= {}".format(
                repr(self.token_index), repr(token), self.previous_state
            )

        @property
        def token_index(self):
            return self._token_index

    class SM:
        def __init__(self):
            self.states = [State(0, None)]

        def scan_char(self, char):
            if self.states == []:
                return False

            states = [*self.states]
            self.states = []

            for state in states:
                # print("{}.match_char({}) => ".format(state, char), end="")
                new_states = state.match_char(char)
                self.states += new_states
                # print("{}".format(new_states))

            return bool(self.states)

        def is_done(self):
            for state in self.states:
                if state.is_done():
                    # print("done:", state)
                    return True
            return False

    return SM()


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        >>> Solution().isMatch("aa", "a")
        False
        >>> Solution().isMatch("aa", "a*")
        True
        >>> Solution().isMatch("ab", ".*")
        True
        >>> Solution().isMatch("b", "c*b")
        True
        >>> Solution().isMatch("ssi", "s*")
        False
        >>> Solution().isMatch("aaa", "aaaa")
        False
        >>> Solution().isMatch("aaa", ".*a")
        True
        >>> Solution().isMatch("aaa", "a*a")
        True
        >>> Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b")
        True
        >>> Solution().isMatch("c", ".x*y*z*")
        True
        """
        sm = build_sm(merge_tokens(parse_pattern(p)))
        for i, char in enumerate(s):
            match = sm.scan_char(char)
            if not match:
                return False
        return sm.is_done()


# @lc code=end
if __name__ == "__main__":
    import doctest

    doctest.testmod()
