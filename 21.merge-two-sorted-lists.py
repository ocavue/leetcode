"""
submits:
- date: 2021-01-15
  minutes: 7
  cheating: false
"""
#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (54.39%)
# Likes:    5870
# Dislikes: 704
# Total Accepted:    1.3M
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a sorted list. The list should
# be made by splicing together the nodes of the first two lists.
#
#
# Example 1:
#
#
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
# Example 2:
#
#
# Input: l1 = [], l2 = []
# Output: []
#
#
# Example 3:
#
#
# Input: l1 = [], l2 = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.
#
#
#


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 and l2):
            return l1 or l2

        head, tail = None, None
        if l1.val < l2.val:
            head = tail = l1
            l1 = l1.next
        else:
            head = tail = l2
            l2 = l2.next

        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    l = l1
                    l1 = l1.next
                else:
                    l = l2
                    l2 = l2.next
                tail.next = l
                l.next = None
                tail = l
            else:
                tail.next = (l1 or l2)
                l1 = None
                l2 = None
        return head


# @lc code=end

