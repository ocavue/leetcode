#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (61.21%)
# Likes:    764
# Dislikes: 1050
# Total Accepted:    298.1K
# Total Submissions: 485.2K
# Testcase Example:  '1'
#
# Write a program that outputs the string representation of numbers from 1 to
# n.
#
# But for multiples of three it should output “Fizz” instead of the number and
# for the multiples of five output “Buzz”. For numbers which are multiples of
# both three and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
# ⁠   '1',
# ⁠   '2',
# ⁠   'Fizz',
# ⁠   '4',
# ⁠   'Buzz',
# ⁠   'Fizz',
# ⁠   '7',
# ⁠   '8',
# ⁠   'Fizz',
# ⁠   'Buzz',
# ⁠   '11',
# ⁠   'Fizz',
# ⁠   '13',
# ⁠   '14',
# ⁠   'FizzBuzz'
# ]
#
#
#

from typing import List

# @lc code=start


def single_fizz_buzz(num: int):
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return str(num)


def fizz_buzz(n: int):
    """
    >>> fizz_buzz(15)
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    """
    return [single_fizz_buzz(i) for i in range(1, n + 1)]


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return fizz_buzz(n)


# @lc code=end
if __name__ == "__main__":
    import doctest

    doctest.testmod()
