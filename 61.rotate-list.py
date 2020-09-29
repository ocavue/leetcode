"""
submits:
- date: 2020-09-29
  minutes: 15
  cheating: false
labels:
- linked-list
"""
#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (28.96%)
# Likes:    1496
# Dislikes: 1048
# Total Accepted:    295.3K
# Total Submissions: 973.6K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, rotate the list to the right by k places, where k is
# non-negative.
#
# Example 1:
#
#
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
#
#
# Example 2:
#
#
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
#
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
def get_len(head: ListNode) -> int:
    # if not head:
    #     return 0
    length = 0
    node = head
    while node:
        length += 1
        node = node.next
    return length


def get_tail(head: ListNode) -> ListNode:
    node = head
    while node.next:
        node = node.next
    return node


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        length = get_len(head)
        k = k % length
        if k == 0:
            return head

        tail = get_tail(head)

        new_head, new_tail = head, tail
        for _, in range(length - k):
            new_tail = new_head
            new_head = new_head.next

        tail.next = head
        new_tail.next = None

        return new_head



# @lc code=end

