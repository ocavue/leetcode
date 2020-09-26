"""
labels:
- gcd/lcm
submits:
- date: 2020-09-26
  minutes: 60
  cheating: true
comment: |
  这道题有意思。有这么几个关键点：
  1. 如何求最小公倍数和最大公约数
  2. 在一个最小公倍数区间范围内，不存在能同时被 A B 整除的数

"""
#
# @lc app=leetcode id=878 lang=python3
#
# [878] Nth Magical Number
#
# https://leetcode.com/problems/nth-magical-number/description/
#
# algorithms
# Hard (27.59%)
# Likes:    221
# Dislikes: 63
# Total Accepted:    10.1K
# Total Submissions: 35.2K
# Testcase Example:  '1\n2\n3'
#
# A positive integer is magical if it is divisible by either A or B.
#
# Return the N-th magical number.  Since the answer may be very large, return
# it modulo 10^9 + 7.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: N = 1, A = 2, B = 3
# Output: 2
#
#
#
# Example 2:
#
#
# Input: N = 4, A = 2, B = 3
# Output: 6
#
#
#
# Example 3:
#
#
# Input: N = 5, A = 2, B = 4
# Output: 10
#
#
#
# Example 4:
#
#
# Input: N = 3, A = 6, B = 4
# Output: 8
#
#
#
#
# Note:
#
#
# 1 <= N <= 10^9
# 2 <= A <= 40000
# 2 <= B <= 40000
#
#
#
#
#
#
#

# @lc code=start


MOB = (10 ** 9) + 7


# greatest common divisor 最大公约数
def get_gcd(A, B):
    a, b = A, B
    while b > 0:
        a, b = b, (a % b)
    return a


# least common multiple 最小公倍数
def get_lcm(A, B):
    return A * B / get_gcd(A, B)


class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        lcm = get_lcm(A, B)

        # 在一个最小公倍数区间内，除了最小公倍数自己，不存在同时被 A 和 B 整除的数
        count_pre_lcm = (lcm // A) + (lcm // B) - 1

        # 从 1 ～ N，有 lcm_count 个最小公倍数区间
        lcm_count, remain = divmod(N, count_pre_lcm)

        # 求第 remain 个 magical 数是什么
        # 这里可以使用二分法加快搜索速度
        assert remain < count_pre_lcm
        i, j, magical_count, magical_number = 1, 1, 0, 0
        while magical_count < remain:
            a, b = A * i, B * j
            if a < b:
                i += 1
                magical_count += 1
                if magical_count == remain:
                    magical_number = a
                    break
            elif b < a:
                j += 1
                magical_count += 1
                if magical_count == remain:
                    magical_number = b
                    break
            else:
                raise Exception("remain < count_pre_lcm, so this is impossible")

        print(
            lcm_count, count_pre_lcm, magical_number,
        )
        return int(lcm_count * lcm + magical_number) % MOB


# @lc code=end

if __name__ == "__main__":
    f = Solution().nthMagicalNumber
    import unittest

    t = unittest.TestCase("__init__")
    t.assertEqual(f(N=1, A=2, B=3), 2)
    t.assertEqual(f(N=4, A=2, B=3), 6)
    t.assertEqual(f(N=5, A=2, B=4), 10)
    t.assertEqual(f(N=3, A=6, B=4), 8)
    t.assertEqual(f(N=2, A=7, B=3), 6)
    t.assertEqual(f(N=1000000, A=40000, B=40000), 999999727)

