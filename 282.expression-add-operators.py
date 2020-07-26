"""
submits:
  - cheating: false
    date: 2020-07-26
    minutes: 53
comment: |
  这道题我的做法不是最优的。正确的做法应该是使用 DFS 去做，避免重复的计算。关于 * 和 - 这种不符合交换律/结合率的操作符，可以保留之前计算的最后一个数字，方便计算。以后再做一遍
labels: []
"""

#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#
# https://leetcode.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (34.75%)
# Likes:    1251
# Dislikes: 202
# Total Accepted:    103.8K
# Total Submissions: 293.2K
# Testcase Example:  '"123"\n6'
#
# Given a string that contains only digits 0-9 and a target value, return all
# possibilities to add binary operators (not unary) +, -, or * between the
# digits so they evaluate to the target value.
#
# Example 1:
#
#
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"]
#
#
# Example 2:
#
#
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
#
# Example 3:
#
#
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
#
# Example 4:
#
#
# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
#
#
# Example 5:
#
#
# Input: num = "3456237490", target = 9191
# Output: []
#
#
#
# Constraints:
#
#
# 0 <= num.length <= 10
# num only contain digits.
#
#
#


# @lc code=start

from typing import List, Generator


def is_valid_num(num: str) -> bool:
    return len(num) >= 1 and (not num.startswith("0") or num == "0")


def split_seq(num: str) -> Generator[List[str], None, None]:
    if is_valid_num(num):
        yield [num]

    for i in range(1, len(num)):
        union, atom = num[0:i], num[i:]
        if is_valid_num(atom):
            for nums in split_seq(union):
                nums.append(atom)
                yield nums


def add_operators(nums: List[str]) -> Generator[str, None, None]:
    # assert all([is_valid_num(num) for num in nums]), 'nums has invalid number: {}'.format(nums)

    assert len(nums) >= 1

    if len(nums) == 1:
        yield nums[0]
    else:
        for rest_exp in add_operators(nums[1:]):
            yield f"{nums[0]}+{rest_exp}"
            yield f"{nums[0]}-{rest_exp}"
            yield f"{nums[0]}*{rest_exp}"


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if len(num) == 1:
            return [num] if num == str(target) else []

        exps: List[str] = []
        for seq in split_seq(num):
            for exp in add_operators(seq):
                if eval(exp) == target:
                    exps.append(exp)

        return exps


# @lc code=end
if __name__ == "__main__":

    f = Solution().addOperators

    import unittest

    t = unittest.TestCase("__init__")

    def test(num, target, expected):
        result = f(num, target)
        result.sort()
        expected.sort()
        t.assertEqual(result, expected)

    test(num="123", target=6, expected=["1+2+3", "1*2*3"])
    test(num="232", target=8, expected=["2*3+2", "2+3*2"])
    test(num="105", target=5, expected=["1*0+5", "10-5"])
    test(num="00", target=0, expected=["0+0", "0-0", "0*0"])
    test(num="3456237490", target=9191, expected=[])
