#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (38.04%)
# Likes:    2617
# Dislikes: 332
# Total Accepted:    373K
# Total Submissions: 974.4K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
#
# Input: 1->2
# Output: false
#
# Example 2:
#
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
#


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start


def get_link_list_len(head: ListNode):
    length = 0
    while head:
        length += 1
        head = head.next
    return length


def is_palindrome(head: ListNode) -> bool:
    if not head:
        return True

    length = get_link_list_len(head)

    if length <= 1:
        return True

    prev = None
    for _ in range(length // 2):
        next = head.next
        head.next = prev

        prev, head = head, next

    mid_to_left_head = prev
    mid_to_right_head = head if length % 2 == 0 else head.next

    assert (
        length // 2
        == get_link_list_len(mid_to_left_head)
        == get_link_list_len(mid_to_right_head)
    )

    l, r = mid_to_left_head, mid_to_right_head
    assert l and r
    while l and r:
        if l.val != r.val:
            return False
        l, r = l.next, r.next
        assert (l and r) or (not l and not r)
    return True


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        return is_palindrome(head)


# @lc code=end
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    assert (is_palindrome(head)) is True

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    assert (is_palindrome(head)) is True

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(9)
    assert (is_palindrome(head)) is False
