"""
submits:
- date: 2020-12-25
  minutes: 21
  cheating: false
"""
#
# @lc app=leetcode id=842 lang=python3
#
# [842] Split Array into Fibonacci Sequence
#
# https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/
#
# algorithms
# Medium (36.36%)
# Likes:    557
# Dislikes: 188
# Total Accepted:    22.9K
# Total Submissions: 62.5K
# Testcase Example:  '"123456579"'
#
# Given a string S of digits, such as S = "123456579", we can split it into a
# Fibonacci-like sequence [123, 456, 579].
#
# Formally, a Fibonacci-like sequence is a list F of non-negative integers such
# that:
#
#
# 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer
# type);
# F.length >= 3;
# and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
#
#
# Also, note that when splitting the string into pieces, each piece must not
# have extra leading zeroes, except if the piece is the number 0 itself.
#
# Return any Fibonacci-like sequence split from S, or return [] if it cannot be
# done.
#
# Example 1:
#
#
# Input: "123456579"
# Output: [123,456,579]
#
#
# Example 2:
#
#
# Input: "11235813"
# Output: [1,1,2,3,5,8,13]
#
#
# Example 3:
#
#
# Input: "112358130"
# Output: []
# Explanation: The task is impossible.
#
#
# Example 4:
#
#
# Input: "0123"
# Output: []
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not
# valid.
#
#
# Example 5:
#
#
# Input: "1101111"
# Output: [110, 1, 111]
# Explanation: The output [11, 0, 11, 11] would also be accepted.
#
#
# Note:
#
#
# 1 <= S.length <= 200
# S contains only digits.
#
#
#

# @lc code=start


def fibonacci(a: int, b: int):
    assert a >= 0
    assert b >= 0

    while True:
        c = a + b
        yield c
        a, b = b, c


def is_fibonacci(a: int, b: int, s: str):
    if not s:
        return False

    result = []

    for n in fibonacci(a, b):

        if not s:
            return result

        if not s.startswith(str(n)):
            return False
        else:
            result.append(n)
            s = s[len(str(n)) :]


MAX = 2 ** 31


class Solution:
    def splitIntoFibonacci(self, s: str):
        if not s:
            return []

        # int(S[0:i]) + int(S[i:j]) = int(S[j:k])
        for i in range(1, len(s)):
            n1 = int(s[0:i])
            if str(n1) != s[0:i] or n1 > MAX:
                continue

            for j in range(i + 1, len(s) - 1):
                n2 = int(s[i:j])
                if str(n2) != s[i:j] or n2 > MAX:
                    continue

                fib = is_fibonacci(n1, n2, s[j:])
                if fib and all(f <= MAX for f in fib):
                    return [n1, n2, *fib]
        return []


# @lc code=end
if __name__ == "__main__":
    from tool import t

    f = Solution().splitIntoFibonacci
    t(f("123456579"), [123, 456, 579])
    t(f("11235813"), [1, 1, 2, 3, 5, 8, 13])
    t(f("112358130"), [])
    t(f("0123"), [])
    # t(f("1101111"), [110, 1, 111])
    t(f("1101111"), [11, 0, 11, 11])
