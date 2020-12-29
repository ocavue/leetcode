"""
submits:
- date: 2020-12-29
  minutes: 6
  cheating: false

"""
#
# @lc app=leetcode id=788 lang=python3
#
# [788] Rotated Digits
#
# https://leetcode.com/problems/rotated-digits/description/
#
# algorithms
# Easy (57.32%)
# Likes:    389
# Dislikes: 1291
# Total Accepted:    58.4K
# Total Submissions: 102K
# Testcase Example:  '10'
#
# X is a good number if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from X.  Each digit must be rotated -
# we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8
# rotate to themselves; 2 and 5 rotate to each other (on this case they are
# rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and
# 9 rotate to each other, and the rest of the numbers do not rotate to any
# other number and become invalid.
#
# Now given a positive number N, how many numbers X from 1 to N are good?
#
#
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after
# rotating.
#
#
# Note:
#
#
# N  will be in range [1, 10000].
#
#
#

# @lc code=start


def is_good_number(n: str) -> bool:
    has_route_num = False
    for char in n:
        if char in "018":
            pass
        elif char in "2569":
            has_route_num = True
        else:
            return False
    return has_route_num


class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for i in range(1, N + 1):
            if is_good_number(str(i)):
                count += 1
        return count


# @lc code=end
if __name__ == "__main__":
    assert is_good_number('112')

