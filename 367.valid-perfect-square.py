#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (40.91%)
# Likes:    898
# Dislikes: 169
# Total Accepted:    226.5K
# Total Submissions: 544.1K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
#
# Follow up: Do not use any built-in library function such as sqrt.
#
#
# Example 1:
# Input: num = 16
# Output: true
# Example 2:
# Input: num = 14
# Output: false
#
#
# Constraints:
#
#
# 1 <= num <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return True
        if num == 1:
            return True

        lo, hi = 1, num
        while True:
            if hi - lo <= 1:
                return num == hi * hi or num == lo * lo

            mi = (hi + lo) // 2
            # assert lo <= mi <= hi
            # assert lo * lo <= num <= hi * hi
            if mi * mi <= num:
                lo = mi
            else:
                hi = mi


# @lc code=end
if __name__ == "__main__":
    f = Solution().isPerfectSquare
    assert f(0) is True
    assert f(1) is True
    assert f(2) is False
    assert f(3) is False
    assert f(4) is True
    assert f(5) is False
    assert f(16) is True
    assert f(18) is False
    assert f(20) is False
    assert f(1024) is True
