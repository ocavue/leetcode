"""
submits:
- date: 2021-01-19
  minutes: 27
  cheating: false
"""
#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (55.99%)
# Likes:    1994
# Dislikes: 105
# Total Accepted:    115.6K
# Total Submissions: 202.8K
# Testcase Example:  '"2-1-1"'
#
# Given a string of numbers and operators, return all possible results from
# computing all the different possible ways to group numbers and operators. The
# valid operators are +, - and *.
#
# Example 1:
#
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
#
# Example 2:
#
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
#
#


from typing import List

# @lc code=start

import re


def run(e):
    assert len(e) % 2 == 1
    if len(e) == 1:
        return [int(e[0])]
    if len(e) == 3:
        return [eval(f"{e[0]}{e[1]}{e[2]}")]

    result = []
    for i in range(len(e) // 2):
        op = 2 * i + 1
        for left in run(e[:op]):
            for right in run(e[op + 1 :]):
                result.append(eval(f"{left}{e[op]}{right}"))

    return result


class Solution:
    def diffWaysToCompute(self, input):
        elements = re.findall(r"([0-9]+|\+|\-|\*)", input)
        return run(elements)


# @lc code=end
if __name__ == "__main__":
    from tool import tt

    t = tt(Solution().diffWaysToCompute)
    t(["2-1-1"], [2, 0])
    t(["2*3-4*5"], [-34, -10, -14, -10, 10])

