"""
submits:
  - date: 2020-04-27
    cheating: false
"""

#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (52.23%)
# Likes:    1340
# Dislikes: 272
# Total Accepted:    210.2K
# Total Submissions: 399.3K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a singly linked list, group all odd nodes together followed by the even
# nodes. Please note here we are talking about the node number and not the
# value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
#
# Example 1:
#
#         0  1  2  3  4
# Input:  1->2->3->4->5->NULL
#         0  2  4  1  3
# Output: 1->3->5->2->4->NULL
#
#
# Example 2:
#
#         0  1  2  3  4  5  6
# Input:  2->1->3->5->6->4->7->NULL
#         0  2  4  6  1  3  5
# Output: 2->3->6->7->1->5->4->NULL
#
#
# Note:
#
#
# The relative order inside both the even and odd groups should remain as it
# was in the input.
# The first node is considered odd, the second node even and so on ...
#
#
#


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next:
            return f"<Node {self.val}\n{self.next}>"
        else:
            return f"<Node {self.val} >"


# @lc code=start


def main(head: ListNode) -> ListNode:
    if not head:
        return head
    if not head.next:
        return head
    if not head.next.next:
        return head

    # h for head; t for tail
    h0 = t0 = head
    h1 = t1 = head.next

    index, node = 2, h1.next
    while True:
        if index % 2 == 0:
            t0.next = node
            t0 = node
        else:
            t1.next = node
            t1 = node

        node = node.next
        index += 1

        if not node:
            break

    t0.next = h1
    t1.next = None
    return h0


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        return main(head)


# @lc code=end

if __name__ == "__main__":

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    print(n1)
    print(main(n1))
