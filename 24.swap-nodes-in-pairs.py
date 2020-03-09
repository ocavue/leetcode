#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (48.41%)
# Likes:    1796
# Dislikes: 154
# Total Accepted:    416K
# Total Submissions: 859.2K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
#
#
#
# Example:
#
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
#
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next:
            return "{} -> {}".format(self.val, self.next)
        else:
            return "{}".format(self.val)


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        assert head
        next = head.next
        if not next:
            return head
        else:
            head.next = self.swapPairs(next.next) if next.next else None
            next.next = head
            return next


# @lc code=end

if __name__ == "__main__":
    print("=" * 20)
    head = ListNode(1)
    print(head)
    print(Solution().swapPairs(head))

    print("=" * 20)
    head = ListNode(1)
    head.next = ListNode(2)
    print(head)
    print(Solution().swapPairs(head))

    print("=" * 20)
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    print(head)
    print(Solution().swapPairs(head))

    print("=" * 20)
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(head)
    print(Solution().swapPairs(head))
