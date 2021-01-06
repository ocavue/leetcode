"""
submits:
- date: 2020-01-06
  minutes: 7
  cheating: false
"""
#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (47.62%)
# Likes:    2408
# Dislikes: 85
# Total Accepted:    380.8K
# Total Submissions: 784.8K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \    / \
# 7    2  5   1
#
#
# Return:
#
#
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
#
#
#

from typing import List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start


def path_sum(root: TreeNode, sum: int) -> List[List[int]]:
    if not root:
        return []
    if not root.left and not root.right and root.val == sum:
        return [[root.val]]

    result: List[List[int]] = []
    for path in path_sum(root.left, sum - root.val):
        p = [root.val] + path
        result.append(p)
    for path in path_sum(root.right, sum - root.val):
        p = [root.val] + path
        result.append(p)
    return result


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        return path_sum(root, sum)


# @lc code=end
if __name__ == "__main__":
    pass
