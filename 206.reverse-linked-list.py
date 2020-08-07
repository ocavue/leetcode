"""
submits:
  - date: 2020-04-30
    cheating: false
  - date: 2020-08-08
    cheating: false
    minutes: 19
labels:
  - reverse-linked-list
comment: |
  遇到这类「反转链表」的题目，性能最好的办法就是使用三个指针，分别指向相邻的前中后
  三个节点，从而保证在切断连接的过程中可以知道不失去接下来的节点。这样在整个迭代
  过程中只需要常数级别的内存
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

# recursively
def reverse_list(head: ListNode) -> ListNode:
    def reverse(head: ListNode):
        assert head
        if head.next is None:
            return head, head
        else:
            new_head, prev_tail = reverse(head.next)
            prev_tail.next = head
            head.next = None
            return new_head, head

    if not head:
        return head
    else:
        new_head, _ = reverse(head)
        return new_head


# iteratively
def reverse_list_v2(head: ListNode) -> ListNode:
    if not head:
        return head
    if not head.next:
        return head
    if not head.next.next:
        tail = head.next
        head.next = None
        tail.next = head
        return tail

    a = head
    b = head.next
    a.next = None
    while True:
        c = b.next
        b.next = a

        if not c:
            return b

        a, b = b, c


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return reverse_list_v2(head)


# @lc code=end
