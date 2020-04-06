#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (34.80%)
# Likes:    856
# Dislikes: 433
# Total Accepted:    209.7K
# Total Submissions: 598.1K
# Testcase Example:  '["2", "1", "+", "3", "*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
#
# Note:
#
#
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would
# always evaluate to a result and there won't be any divide by zero
# operation.
#
#
# Example 1:
#
#
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
#
# Example 2:
#
#
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
#
# Example 3:
#
#
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation:
# ⁠  ((10 * (6 // ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 // (12 * -11))) + 17) + 5
# = ((10 * (6 // -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#
#
#

# @lc code=start
from typing import List, Union


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


def eval_rpm(tokens: List[Union[str, int]]) -> int:
    """
    >>> eval_rpm([1, 1, '+'])
    2
    >>> eval_rpm([1, 1, '+'])
    2
    >>> eval_rpm(["2", "1", "+", "3", "*"])
    9
    >>> eval_rpm(["4", "13", "5", "/", "+"])
    6
    >>> eval_rpm(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    22
    """
    tokens = [
        token if token in ["+", "-", "*", "/"] else int(token) for token in tokens
    ]

    num_stack = []

    for token in tokens:

        if isinstance(token, int):
            num_stack.append(token)
        else:
            n1 = num_stack.pop()
            n2 = num_stack.pop()
            result = eval_operator(n2, n1, token)
            num_stack.append(result)

    assert len(num_stack) == 1
    return num_stack[0]


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return eval_rpm(tokens)


# @lc code=end

if __name__ == "__main__":
    import doctest

    doctest.testmod()
