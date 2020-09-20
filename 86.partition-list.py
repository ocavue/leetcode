"""
submits:
- date: 2020-09-20
  minutes: 13
  cheating: false
labels:
- linked-list
"""
#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (39.85%)
# Likes:    1495
# Dislikes: 324
# Total Accepted:    227.6K
# Total Submissions: 541.5K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
# Example:
#
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
#
#
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start


def partition(head: ListNode, x: int):
    if not head:
        return None, None, None
    if not head.next:
        if head.val < x:
            return head, head, None
        else:
            return None, None, head

    less_head, less_tail, more = partition(head.next, x)
    if head.val < x:
        head.next = less_head
        return head, less_tail or head, more
    else:
        head.next = more
        return less_head, less_tail, head


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None

        less_head, less_tail, more = partition(head, x)
        if less_head:
            less_tail.next = more
        return less_head or more


# @lc code=end

