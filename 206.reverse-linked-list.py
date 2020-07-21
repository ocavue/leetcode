"""
submits:
  - date: 2020-04-30
    cheating: false
"""

#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (59.86%)
# Likes:    3801
# Dislikes: 82
# Total Accepted:    877.7K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
#
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
#
#


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start


def reverse_list(head: ListNode) -> ListNode:
    def reverse(prev: ListNode, node: ListNode):
        origin_next = node.next
        node.next = prev
        if origin_next:
            return reverse(node, origin_next)
        else:
            return node

    if not head:
        return head
    if not head.next:
        return head

    head_next = head.next
    head.next = None
    return reverse(head, head_next)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return reverse_list(head)


# @lc code=end
