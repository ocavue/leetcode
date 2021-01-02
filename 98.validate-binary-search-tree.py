"""
submits:
- date: 2021-01-02
  minutes: 9
  cheating: false
"""
#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (28.02%)
# Likes:    5185
# Dislikes: 618
# Total Accepted:    864.6K
# Total Submissions: 3M
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, determine if it is a valid binary search
# tree (BST).
#
# A valid BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
#
#
#

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"<Tree {self.val} {self.left} {self.right}>"


# @lc code=start


def is_valid_bst(tree: TreeNode, min: float, max: float) -> bool:
    if tree is None:
        return True

    if not (min < tree.val < max):
        return False

    return is_valid_bst(tree.left, min=min, max=tree.val) and is_valid_bst(tree.right, max=max, min=tree.val)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return is_valid_bst(root, float("-inf"), float("inf"))


# @lc code=end
if __name__ == "__main__":
    f = Solution().isValidBST
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert f(root) is True
