"""
submits:
- date: 2020-01-07
  cheating: true
  minutes: 24
comment: |
  这道题需要理解的是，屏幕中显示的字符数是剪贴板中的字符数的整数倍。
"""
#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#
# https://leetcode.com/problems/2-keys-keyboard/description/
#
# algorithms
# Medium (49.46%)
# Likes:    1531
# Dislikes: 113
# Total Accepted:    68.1K
# Total Submissions: 136.7K
# Testcase Example:  '3'
#
# Initially on a notepad only one character 'A' is present. You can perform two
# operations on this notepad for each step:
#
#
# Copy All: You can copy all the characters present on the notepad (partial
# copy is not allowed).
# Paste: You can paste the characters which are copied last time.
#
#
#
#
# Given a number n. You have to get exactly n 'A' on the notepad by performing
# the minimum number of steps permitted. Output the minimum number of steps to
# get n 'A'.
#
# Example 1:
#
#
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
#
#
#
#
# Note:
#
#
# The n will be in the range [1, 1000].
#
#
#
#
#

# @lc code=start
from functools import lru_cache


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        s = 0

        for d in range(2, n + 1):
            while n % d == 0:
                s += d
                n //= d
        return s

    # def minSteps(self, n: int) -> int:
    #     if n == 1:
    #         return 0

    #     @lru_cache
    #     def run(screen: int, pasted: int) -> int:
    #         assert screen + pasted <= n
    #         if screen + pasted == n:
    #             return 1
    #         elif screen + pasted < n:
    #             # Paste
    #             case1 = 1 + run(screen + pasted, pasted)
    #             # Copy and Paste
    #             case2 = 2 + run(2 * screen, screen)
    #             return min(case1, case2)
    #         else:
    #             return 1001

    #     return run(1, 1) + 1


# @lc code=end
if __name__ == "__main__":
    from tool import t

    f = Solution().minSteps
    t(f(3), 3)
    t(f(4), 4)
