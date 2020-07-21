"""
submits:
  - date: 2020-04-08
    cheating: false
"""

#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (49.77%)
# Likes:    2702
# Dislikes: 102
# Total Accepted:    258.6K
# Total Submissions: 516.1K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#

# @lc code=start

from functools import lru_cache


@lru_cache()
def num_trees(n: int) -> int:
    """
    the number of unique BST for a sequence of length n.
    """
    assert 1 <= n

    result = 0
    for i in range(1, n + 1):
        result += num_trees_with_fixed_root(n, i)
    return result


def num_trees_with_fixed_root(n: int, i: int) -> int:
    """
    the number of unique BST for a sequence of length n with i as the root
    """
    assert 1 <= i <= n

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif i == 1:
        return num_trees(n - 1)
    elif i == n:
        return num_trees(n - 1)
    else:
        left = i - 1
        right = n - i
        return num_trees(left) * num_trees(right)


class Solution:
    def numTrees(self, n: int) -> int:
        return num_trees(n)


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")

    t.assertEqual(num_trees_with_fixed_root(1, 1), 1)
    t.assertEqual(num_trees_with_fixed_root(2, 1), 1)
    t.assertEqual(num_trees_with_fixed_root(2, 2), 1)
    t.assertEqual(num_trees_with_fixed_root(3, 1), 2)
    t.assertEqual(num_trees_with_fixed_root(3, 2), 1)
    t.assertEqual(num_trees_with_fixed_root(3, 3), 2)

    t.assertEqual(num_trees(1), 1)
    t.assertEqual(num_trees(2), 2)
    t.assertEqual(num_trees(3), 5)

    num_trees(19)
