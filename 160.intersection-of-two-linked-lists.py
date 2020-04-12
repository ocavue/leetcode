#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (38.04%)
# Likes:    3106
# Dislikes: 345
# Total Accepted:    419.7K
# Total Submissions: 1.1M
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,0,1,8,4,5]\n2\n3'
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
#
# For example, the following two linked lists:
#
#
# begin to intersect at node c1.
#
#
#
# Example 1:
#
#
#
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA =
# 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not
# be 0 if the two lists intersect). From the head of A, it reads as
# [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes
# before the intersected node in A; There are 3 nodes before the intersected
# node in B.
#
#
#
# Example 2:
#
#
#
# Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3,
# skipB = 1
# Output: Reference of the node with value = 2
# Input Explanation: The intersected node's value is 2 (note that this must not
# be 0 if the two lists intersect). From the head of A, it reads as
# [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes
# before the intersected node in A; There are 1 node before the intersected
# node in B.
#
#
#
#
# Example 3:
#
#
#
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: null
# Input Explanation: From the head of A, it reads as [2,6,4]. From the head of
# B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must
# be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
#
#
#
#
# Notes:
#
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function
# returns.
# You may assume there are no cycles anywhere in the entire linked
# structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
#
#
#


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "<Node {} next={}>".format(self.val, self.next)


# @lc code=start


def get_list_len(head: ListNode) -> int:
    length = 0
    node = head
    while node is not None:
        length += 1
        node = node.next
    return length


_DEBUG = False


def get_intersection_node(head_a: ListNode, head_b: ListNode) -> ListNode:
    list_a_len = get_list_len(head_a)
    list_b_len = get_list_len(head_b)
    min_len = min([list_a_len, list_b_len])

    if list_a_len > min_len:
        for _ in range(list_a_len - min_len):
            head_a = head_a.next
    elif list_b_len > min_len:
        for _ in range(list_b_len - min_len):
            head_b = head_b.next

    if _DEBUG:
        assert get_list_len(head_a) == get_list_len(head_b)

    for _ in range(min_len):
        if head_a == head_b:
            return head_a
        else:
            head_a = head_a.next
            head_b = head_b.next

    return None


class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> ListNode:
        return get_intersection_node(head_a, head_b)


# @lc code=end
if __name__ == "__main__":
    _DEBUG = True
    # Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3,
    list_inter = [
        ListNode(2),
        ListNode(4),
    ]
    list_a = [
        ListNode(0),
        ListNode(9),
        ListNode(1),
        *list_inter,
    ]
    list_b = [
        ListNode(3),
        *list_inter,
    ]
    for l in [list_a, list_b]:
        for i in range(1, len(l)):
            l[i - 1].next = l[i]

    assert get_intersection_node(list_a[0], list_b[0]) == list_inter[0]
