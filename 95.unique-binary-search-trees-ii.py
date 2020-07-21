"""
submits:
  - date: 2020-04-08
    cheating: false
"""

#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (38.63%)
# Likes:    1835
# Dislikes: 146
# Total Accepted:    176.2K
# Total Submissions: 452.2K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
#
# Example:
#
#
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#

# Definition for a binary tree node.
from typing import List
from functools import lru_cache


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start


def ajust_right_tree(tree: TreeNode, start: int) -> TreeNode:
    new_tree = TreeNode(tree.val + start)
    new_tree.left = tree.left and ajust_right_tree(tree.left, start)
    new_tree.right = tree.right and ajust_right_tree(tree.right, start)
    return new_tree


def generate_trees_with_fixed_root(n, i) -> List[TreeNode]:
    assert 1 <= i <= n

    if n == 1:
        root = TreeNode(i)
        return [root]
    elif n == 2:
        root = TreeNode(i)
        if i == 1:
            root.right = TreeNode(2)
            return [root]
        else:
            root.left = TreeNode(1)
            return [root]
    elif i == 1:
        result = []
        for right_tree in generate_trees(n - 1):
            root = TreeNode(i)
            root.right = ajust_right_tree(right_tree, i)
            result.append(root)
        return result
    elif i == n:
        result = []
        for tree in generate_trees(n - 1):
            root = TreeNode(i)
            root.left = tree
            result.append(root)
        return result
    else:
        result = []
        left_trees = generate_trees(i - 1)
        right_trees = generate_trees(n - i)

        for right_tree in right_trees:
            right_tree = ajust_right_tree(right_tree, i)
            for left_tree in left_trees:
                root = TreeNode(i)
                root.left = left_tree
                root.right = right_tree
                result.append(root)
        return result


@lru_cache
def generate_trees(n) -> List[TreeNode]:
    if n == 0:
        return []

    assert 1 <= n

    result = []
    for root in range(1, n + 1):
        result += generate_trees_with_fixed_root(n, root)
    return result


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return generate_trees(n)


# @lc code=end
