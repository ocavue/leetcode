"""
submits
- date: 2020-01-06
  minutes: 3
  cheating: false

"""
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (41.60%)
# Likes:    2653
# Dislikes: 566
# Total Accepted:    557.5K
# Total Submissions: 1.3M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
#
#
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
#
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start


def has_path_sum(root: TreeNode, sum: int) -> bool:
    if not root:
        return False

    if not root.left and not root.right:
        return sum == root.val

    return has_path_sum(root.left, sum - root.val) or has_path_sum(root.right, sum - root.val)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return has_path_sum(root, sum)


# @lc code=end

