"""
submits:
- date: 2020-10-20
  minutes: 17
  cheating: false
labels: [dp]
"""
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#
# https://leetcode.com/problems/integer-break/description/
#
# algorithms
# Medium (50.67%)
# Likes:    1250
# Dislikes: 239
# Total Accepted:    116.8K
# Total Submissions: 230.3K
# Testcase Example:  '2'
#
# Given a positive integer n, break it into the sum of at least two positive
# integers and maximize the product of those integers. Return the maximum
# product you can get.
#
# Example 1:
#
#
#
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
#
#
# Example 2:
#
#
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
#
# Note: You may assume that n is not less than 2 and not larger than 58.
#
#
#

# @lc code=start

import functools


def break_int(n: int, min_parts: int) -> int:
    if min_parts == 2:
        best = n - 1
        for i in range(2, n - 1):
            a, b = i, n - i
            # assert a >= 2 and b >= 2
            best = max(best, a * break_int_with_cache(b, 1))
    else:
        # assert min_parts == 1
        best = n
        for i in range(2, n - 1):
            a, b = i, n - i
            # assert a >= 2 and b >= 2
            best = max(best, a * break_int_with_cache(b, 1))
    return best


@functools.lru_cache()
def break_int_with_cache(n: int, min_parts: int) -> int:
    return break_int(n, min_parts)


class Solution:
    def integerBreak(self, n: int) -> int:
        return break_int(n, 2)


# @lc code=end
if __name__ == "__main__":
    from tool import test

    t = test()
    f = Solution().integerBreak
    t.assertEqual(f(2), 1)
    t.assertEqual(f(3), 2)
    t.assertEqual(f(4), 4)
    t.assertEqual(f(10), 36)
