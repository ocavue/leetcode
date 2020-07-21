"""
submits:
  - date: 2020-04-14
    cheating: false
"""

"""
重点：BST 的前序遍历是有序的

这个题目的回答特别不错，推荐去看
"""
#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (56.08%)
# Likes:    1941
# Dislikes: 53
# Total Accepted:    319.7K
# Total Submissions: 564.9K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
#
#
# Input: root = [3,1,4,null,2], k = 1
# ⁠  3
# ⁠ / \
# ⁠1   4
# ⁠ \
#   2
# Output: 1
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# ⁠      5
# ⁠     / \
# ⁠    3   6
# ⁠   / \
# ⁠  2   4
# ⁠ /
# ⁠1
# Output: 3
#
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to
# find the kth smallest frequently? How would you optimize the kthSmallest
# routine?
#
#

# @lc code=start


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder_traversal(root):
    if not root:
        return
    else:
        yield from inorder_traversal(root.left)
        yield root.val
        yield from inorder_traversal(root.right)


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        for i, val in enumerate(inorder_traversal(root)):
            if i + 1 == k:
                return val


# @lc code=end
