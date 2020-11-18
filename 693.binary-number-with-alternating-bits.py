"""
submits:
- date: 2020-11-18
  minutes: 8
  cheating: false
labels:
- bit-manipulation
"""
#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (59.48%)
# Likes:    531
# Dislikes: 91
# Total Accepted:    67.2K
# Total Submissions: 112.9K
# Testcase Example:  '5'
#
# Given a positive integer, check whether it has alternating bits: namely, if
# two adjacent bits will always have different values.
#
#
# Example 1:
#
#
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
#
#
# Example 2:
#
#
# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
#
# Example 3:
#
#
# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
#
# Example 4:
#
#
# Input: n = 10
# Output: true
# Explanation: The binary representation of 10 is: 1010.
#
# Example 5:
#
#
# Input: n = 3
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        started = False
        expect_next = 0

        for i in range(31, -1, -1):
            val = (n >> i) & 1
            if val == 1 and not started:
                expect_next = 0
                started = True
                continue

            if started:
                if expect_next == val:
                    expect_next = 1 if expect_next == 0 else 0
                else:
                    return False
        return True


# @lc code=end

if __name__ == "__main__":
    f = Solution().hasAlternatingBits
    assert f(7) is False
