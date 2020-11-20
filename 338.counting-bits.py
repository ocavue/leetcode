"""
submits:
- date: 2020-11-20
  minutes: 16
  cheating: false
labels:
- bit-manipulation
"""
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Medium (69.87%)
# Likes:    3161
# Dislikes: 180
# Total Accepted:    312.6K
# Total Submissions: 447.1K
# Testcase Example:  '2'
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤
# i ≤ num calculate the number of 1's in their binary representation and return
# them as an array.
#
# Example 1:
#
#
# Input: 2
# Output: [0,1,1]
#
# Example 2:
#
#
# Input: 5
# Output: [0,1,1,2,1,2]
#
#
# Follow up:
#
#
# It is very easy to come up with a solution with run time
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
# single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like
# __builtin_popcount in c++ or in any other language.
#
#

# @lc code=start
class Solution:
    def countBits(self, num):
        if num == 0:
            return [0]

        result = [0]

        while True:
            loop_size = len(result)
            for i in range(loop_size):
                result.append(result[i] + 1)
                if len(result) > num:
                    break
            if len(result) > num:
                break

        return result


# @lc code=end

if __name__ == "__main__":
    from tool import t

    f = Solution().countBits

    t(f(0), [0])
    t(f(1), [0, 1])
    t(f(2), [0, 1, 1])
    t(f(3), [0, 1, 1, 2])
