"""
submits:
  - date: 2020-04-22
    cheating: false
"""

#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (35.39%)
# Likes:    2291
# Dislikes: 192
# Total Accepted:    293.1K
# Total Submissions: 816.6K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
#
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
#
# Note: Do not modify the linked list.
#
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
#
#
#
#
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
#
#
#
#
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
#
#
#
#
#
#
# Follow-up:
# Can you solve it without using extra space?
#
#


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "<Node {}>".format(self.val)


# @lc code=start

from typing import Union


def check_cycle(head: ListNode) -> Union[ListNode, None]:
    if not head.next:
        return None

    # Initial Nodes
    ni: ListNode = head
    nj: ListNode = head
    # Initial Steps
    si: int = 0
    sj: int = 0

    try:
        while True:
            ni = ni.next
            nj = nj.next.next
            si += 1
            sj += 2
            if ni == nj:
                # print(ni, nj, si, sj)
                return ni
    except AttributeError:
        return None


def detect_cycle(head: ListNode) -> Union[None, ListNode]:
    i = check_cycle(head)
    if i is None:
        return None
    j = i
    x = head

    # print(j)

    error = 0
    while True:
        # print(f"x: {x}; j: {j}")

        if x == j:
            return x
        x = x.next
        j = j.next

        if x == i:
            error += 1
            if error >= 2:
                raise Exception("loop error")


class Solution:
    def detectCycle(self, head: ListNode):
        if not head:
            return None
        return detect_cycle(head)


# @lc code=end
if __name__ == "__main__":
    # Input: head = [3,2,0,-4], pos = 1
    n0 = ListNode(3)
    n1 = ListNode(2)
    n2 = ListNode(0)
    n3 = ListNode(-4)

    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n1

    print(detect_cycle(n0))
    assert detect_cycle(n0) == n1
