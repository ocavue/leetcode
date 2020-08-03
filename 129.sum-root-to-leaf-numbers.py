"""
submits:
  - date: 2020-08-03
    cheating: false
    minutes: 15x
"""
# 12:13 12:28
#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (45.57%)
# Likes:    1575
# Dislikes: 43
# Total Accepted:    279K
# Total Submissions: 570.1K
# Testcase Example:  '[1,2,3]'
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path
# could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input: [1,2,3]
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
#
# Example 2:
#
#
# Input: [4,9,0,5,1]
#  ⁠   4
#  ⁠  / \
#  ⁠ 9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#
#

# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start


def get_represent_numbers(node: TreeNode) -> List[str]:
    children = []
    if node.left is not None:
        children += get_represent_numbers(node.left)
    if node.right is not None:
        children += get_represent_numbers(node.right)

    if not children:
        return [str(node.val)]
    else:
        return [str(node.val) + child for child in children]


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        nums = get_represent_numbers(root)
        return sum([int(n) for n in nums])


# @lc code=end
if __name__ == "__main__":
    f = Solution().sumNumbers

    tree4 = TreeNode(4)
    tree9 = TreeNode(9)
    tree0 = TreeNode(0)
    tree5 = TreeNode(5)
    tree1 = TreeNode(1)

    tree4.left = tree9
    tree4.right = tree0
    tree9.left = tree5
    tree9.right = tree1

    import unittest

    t = unittest.TestCase("__init__")

    t.assertEqual(f(tree4), 1026)

