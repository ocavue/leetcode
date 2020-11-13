"""
submits:
- date: 2020-11-13
  minutes: 5
  cheating: false
"""
#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#
# https://leetcode.com/problems/reverse-bits/description/
#
# algorithms
# Easy (40.64%)
# Likes:    1391
# Dislikes: 476
# Total Accepted:    306.5K
# Total Submissions: 748K
# Testcase Example:  '00000010100101000001111010011100'
#
# Reverse bits of a given 32 bits unsigned integer.
#
# Note:
#
#
# Note that in some languages such as Java, there is no unsigned integer type.
# In this case, both input and output will be given as a signed integer type.
# They should not affect your implementation, as the integer's internal binary
# representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement
# notation. Therefore, in Example 2 above, the input represents the signed
# integer -3 and the output represents the signed integer -1073741825.
#
#
# Follow up:
#
# If this function is called many times, how would you optimize it?
#
#
# Example 1:
#
#
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100
# represents the unsigned integer 43261596, so return 964176192 which its
# binary representation is 00111001011110000010100101000000.
#
#
# Example 2:
#
#
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101
# represents the unsigned integer 4294967293, so return 3221225471 which its
# binary representation is 10111111111111111111111111111111.
#
#
#
# Constraints:
#
#
# The input must be a binary string of length 32
#
#
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = (res << 1) | bit
        return res


# @lc code=end
if __name__ == "__main__":
    from tool import test

    t = test()
    f = Solution().reverseBits
    t.assertEqual(f(0b11111111111111111111111111111101), 0b10111111111111111111111111111111)
    t.assertEqual(f(0b00000000000000000000000010010101), 0b10101001000000000000000000000000)
