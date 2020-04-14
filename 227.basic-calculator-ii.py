#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (35.78%)
# Likes:    1167
# Dislikes: 208
# Total Accepted:    161.2K
# Total Submissions: 448K
# Testcase Example:  '"3+2*2"'
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces  . The integer division should truncate toward
# zero.
#
# Example 1:
#
#
# Input: "3+2*2"
# Output: 7
#
#
# Example 2:
#
#
# Input: " 3/2 "
# Output: 1
#
# Example 3:
#
#
# Input: " 3+5 / 2 "
# Output: 5
#
#
# Note:
#
#
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
#
#
#

# @lc code=start

from typing import List, Union
import re

Token = Union[str, int]


def eval_operator(a: int, b: int, operator: str):
    """
    >>> eval_operator(1, 1, '+')
    2
    >>> eval_operator(10, -1, '*')
    -10
    >>> eval_operator(15, 5, '/')
    3
    >>> eval_operator(14, 5, '/')
    2
    >>> eval_operator(11, 5, '/')
    2
    >>> eval_operator(10, 5, '/')
    2
    >>> eval_operator(11, -5, '/')
    -2
    >>> eval_operator(14, -5, '/')
    -2
    >>> eval_operator(15, -5, '/')
    -3
    >>> eval_operator(-11, 5, '/')
    -2
    >>> eval_operator(-14, 5, '/')
    -2
    >>> eval_operator(-15, 5, '/')
    -3
    >>> eval_operator(-5, 5, '/')
    -1
    >>> eval_operator(-6, 5, '/')
    -1
    >>> eval_operator(-4, 5, '/')
    0
    >>> eval_operator(-1, 5, '/')
    0
    >>> eval_operator(6, 5, '/')
    1
    >>> eval_operator(5, 5, '/')
    1
    >>> eval_operator(4, 5, '/')
    0
    >>> eval_operator(1, 5, '/')
    0
    >>> eval_operator(0, -1, '/')
    0
    >>> eval_operator(0, 1, '/')
    0
    >>> eval_operator(0, 10, '/')
    0
    """
    if operator == "/":
        if a % b == 0:
            return a // b
        elif a // b >= 0:
            return a // b
        else:
            return a // b + 1
    else:
        return eval("{} {} {}".format(a, operator, b))


def is_operator(token: Token):
    return token in ("+", "-", "*", "/")


def parse(s: str) -> List[Token]:
    tokens = re.findall(r"(\d+|[\+\-\*\/])", s)
    return [(i if is_operator(i) else int(i)) for i in tokens]


def calculate(s: str) -> int:
    """
    >>> calculate("3+2*2")
    7
    >>> calculate(" 3+5 / 2 ")
    5
    >>> calculate('1-1+1')
    1
    """
    int_stack = []
    op_stack = []

    for t in parse(s):
        if is_operator(t):
            op_stack.append(t)
        else:
            if op_stack and op_stack[-1] in "*/":
                op = op_stack.pop()
                j = int_stack.pop()
                int_stack.append(eval_operator(j, t, op))
            else:
                int_stack.append(t)

    assert all([isinstance(i, int) for i in int_stack])
    assert all([isinstance(o, str) for o in op_stack])
    assert all([o in "+-" for o in op_stack])
    assert len(int_stack) == len(op_stack) + 1

    for i, op in enumerate(op_stack):
        if op == "-":
            int_stack[i + 1] *= -1

    return sum(int_stack)


class Solution:
    def calculate(self, s: str) -> int:
        return calculate(s)


# @lc code=end

if __name__ == "__main__":
    import doctest

    doctest.testmod()
