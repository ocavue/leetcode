"""
submits:
  - date: 2020-04-15
    cheating: false
"""

#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#
# https://leetcode.com/problems/delete-node-in-a-linked-list/description/
#
# algorithms
# Easy (58.46%)
# Likes:    1235
# Dislikes: 5826
# Total Accepted:    374.6K
# Total Submissions: 634.2K
# Testcase Example:  '[4,5,1,9]\n5'
#
# Write a function to delete a node (except the tail) in a singly linked list,
# given only access to that node.
#
# Given linked list -- head = [4,5,1,9], which looks like following:
#
#
#
#
#
# Example 1:
#
#
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list
# should become 4 -> 1 -> 9 after calling your function.
#
#
# Example 2:
#
#
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list
# should become 4 -> 5 -> 9 after calling your function.
#
#
#
#
# Note:
#
#
# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node of the
# linked list.
# Do not return anything from your function.
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        assert node.next
        node.val = node.next.val
        node.next = node.next.next


# @lc code=end
