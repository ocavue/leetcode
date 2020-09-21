"""
submits:
- date: 2020-09-21
  minutes: 37
  cheating: false
comment: |
  看了答案之后，发现 python 里面的内置函数 divmod 特别好用：divmod(a, b) == (a // b, a % b)
"""
#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (20.81%)
# Likes:    949
# Dislikes: 1975
# Total Accepted:    133.2K
# Total Submissions: 610.5K
# Testcase Example:  '1\n2'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
#
# If multiple answers are possible, return any of them.
#
#
# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:
# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
# Example 4:
# Input: numerator = 4, denominator = 333
# Output: "0.(012)"
# Example 5:
# Input: numerator = 1, denominator = 5
# Output: "0.2"
#
#
# Constraints:
#
#
# -2^31 <= numerator, denominator <= 2^31 - 1
# denominator != 0
#
#
#

# @lc code=start
from typing import Dict, Tuple, List

Cache = Dict[Tuple[int, int], int]


def fraction_to_decimal(n: int, d: int, index, cache: Cache, nums: List[str]) -> str:

    if (n, d) in cache:
        prev_index = cache[(n, d)]

        nums = nums[:prev_index] + ["("] + nums[prev_index:] + [")"]
        return "".join(nums)

    cache[(n, d)] = index

    # if index >= 500:
    #     return ""

    if n == 0:
        return "".join(nums)

    if n < d:
        nums[index : index + 1] = ["0"]
        # print("".join(nums))
        return fraction_to_decimal(10 * n, d, index + 1, cache, nums)
    if n > d:
        nums[index : index + 1] = [str(n // d)]
        # print("".join(nums))
        return fraction_to_decimal(10 * (n % d), d, index + 1, cache, nums)

    nums[index : index + 1] = ["1"]
    return "".join(nums)


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator * denominator < 0:
            return "-" + self.fractionToDecimal(abs(numerator), abs(denominator))

        numerator = abs(numerator)
        denominator = abs(denominator)

        int_part = str(numerator // denominator)
        cache: Cache = {}
        nums: List[str] = []

        if (numerator % denominator) == 0:
            return str(int_part)

        float_part = fraction_to_decimal(10 * (numerator % denominator), denominator, 0, cache, nums)
        return f"{int_part}.{float_part}"


# @lc code=end
if __name__ == "__main__":
    f = Solution().fractionToDecimal
    print(f(1, 2))
    print(f(2, 1))
    print(f(2, 3))
    print(f(4, 333))
    print(f(1, 5))
    print(f(-1, 5))
