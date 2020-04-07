#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.86%)
# Likes:    7220
# Dislikes: 1872
# Total Accepted:    1.2M
# Total Submissions: 3.8M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#
#


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start


def combine_two_nodes(l1: ListNode, l2: ListNode) -> ListNode:
    result = None
    latest = None
    while not (l1 is None and l2 is None):
        n1 = n2 = 0
        if l1 is not None:
            n1 = l1.val
            l1 = l1.next
        if l2 is not None:
            n2 = l2.val
            l2 = l2.next
        next = ListNode(n1 + n2)

        if result is None:
            latest = result = next
        else:
            latest.next = next
            latest = latest.next

        assert result is not None
        assert latest is not None
        assert latest.next is None
    return result


def normalize_node(node: ListNode) -> ListNode:
    extra = 0
    while node is not None:
        if extra:
            node.val += extra
            extra = 0
        if node.val >= 10:
            extra = node.val // 10
            node.val = node.val % 10

            if (node.next) is None:
                node.next = ListNode(0)
        node = node.next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    combined = combine_two_nodes(l1, l2)
    normalize_node(combined)
    return combined


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return add_two_numbers(l1, l2)


# @lc code=end
