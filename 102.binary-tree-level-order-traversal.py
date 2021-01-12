"""
submits:
- date: 2021-01-12
  minutes: 10
  cheating: false
"""
#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (55.34%)
# Likes:    4007
# Dislikes: 95
# Total Accepted:    745.9K
# Total Submissions: 1.3M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
#
#
#

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.


def add(nodes):
    res = []
    children = []
    for node in nodes:
        res.append(node.val)
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)
    return res, children


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        nodes = [root]
        while nodes:
            row, nodes = add(nodes)
            res.append(row)
        return res


# @lc code=end

