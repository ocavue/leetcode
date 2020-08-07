"""
submits:
  - date: 2020-08-08
    minutes: 38
    cheating: false
labels:
  - reverse-linked-list
comment: |
  这道题的关键在于「如何使用 O(1) 的内存和 O(n) 的时间去反转一个单项链表」，这部分可以看 leetcode 206。
  剩下的部分就是简单的代码设计而已了。
"""
#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (39.72%)
# Likes:    2367
# Dislikes: 360
# Total Accepted:    276.3K
# Total Submissions: 657.5K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
#
#
#
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
#
#
#

# @lc code=start

from typing import List, Tuple

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}->{self.next}"


def get_linked_list_length(head: ListNode) -> int:
    length = 0
    while head:
        length += 1
        head = head.next

        # assert length < 100000, "found infinite loop"
    return length


def reverse_first_k_group(head: ListNode, k: int, length: int) -> Tuple[ListNode, ListNode]:
    """
    将一个链表的前 k 项反转，并返回反转后的前 k 项以及未反转的部分

    reverse_first_k_group(1->2->3->4->5->6->7, 3, 7) => (3->2->1, 4->5->6->7)
    """

    # assert get_linked_list_length(head) == length, f"{head} != {length}"
    # assert length >= k >= 2

    a = head
    b = head.next
    a.next = None
    for _ in range(k - 1):
        c = b.next
        b.next = a
        a, b = b, c

    return a, b


def reverse_k_group(origin_head: ListNode, k: int):
    origin_length = get_linked_list_length(origin_head)
    loop_times = origin_length // k

    if loop_times == 0:
        return origin_head

    reversed_head = None
    reversed_tail = None
    unreverse_head = origin_head

    for i in range(loop_times):
        iter_revertsed_tail = unreverse_head
        iter_revertsed_head, unreverse_head = reverse_first_k_group(unreverse_head, k, origin_length - k * i)
        # print('iter_revertsed_head:', iter_revertsed_head)
        # print('unreverse_head:', unreverse_head)

        if reversed_head is None:
            reversed_head = iter_revertsed_head
            reversed_tail = iter_revertsed_tail
        else:
            reversed_tail.next = iter_revertsed_head
            reversed_tail = iter_revertsed_tail

    assert reversed_head
    assert reversed_tail
    reversed_tail.next = unreverse_head
    return reversed_head


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        if k == 1:
            return head
        return reverse_k_group(head, k)


# @lc code=end
if __name__ == "__main__":
    def parpare():
        nodes = [
            ListNode(1),
            ListNode(2),
            ListNode(3),
            ListNode(4),
            ListNode(5),
        ]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]
    print(parpare())
    print(reverse_k_group(parpare(), 2))
    print(reverse_k_group(parpare(), 3))
