"""
submits:
  - date: 2020-04-12
    cheating: false
"""

#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (39.71%)
# Likes:    2452
# Dislikes: 376
# Total Accepted:    569.6K
# Total Submissions: 1.4M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
#
#
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
#
#
#
#
#
#
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
#
#
#
#
#
#
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
#
#
#
#
#
# Follow up:
#
# Can you solve it using O(1) (i.e. constant) memory?
#
#


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
# Definition for singly-linked list.


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        i = head
        j = head.next

        try:
            while True:
                i = i.next
                j = j.next
                if i == j:
                    return True
                j = j.next
                if i == j:
                    return True
        except AttributeError:
            return False


# @lc code=end
