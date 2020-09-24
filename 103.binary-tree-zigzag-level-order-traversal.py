"""
submits:
- date: 2020-09-24
  minutes: 6
  cheating: false

"""
#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (45.35%)
# Likes:    2531
# Dislikes: 106
# Total Accepted:    414.9K
# Total Submissions: 850.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result: List[List[int]] = []

        left_to_right = True
        curr_nodes: List[TreeNode] = [root]

        while curr_nodes:
            if left_to_right:
                row = [node.val for node in curr_nodes]
            else:
                row = [node.val for node in curr_nodes[::-1]]
            result.append(row)

            left_to_right = not left_to_right
            next_nodes: List[TreeNode] = []
            for node in curr_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            curr_nodes = next_nodes

        return result


# @lc code=end

