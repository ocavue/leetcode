"""
submits:
  - date: 2020-04-30
    cheating: false
"""

#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (32.85%)
# Likes:    2716
# Dislikes: 604
# Total Accepted:    367.2K
# Total Submissions: 1.1M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
#
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random
# pointer points to, or null if it does not point to any node.
#
#
#
# Example 1:
#
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
# Example 2:
#
#
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
#
#
# Example 3:
#
#
#
#
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
#
#
# Example 4:
#
#
# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.
#
#
#
# Constraints:
#
#
# -10000 <= Node.val <= 10000
# Node.random is null or pointing to a node in the linked list.
# Number of Nodes will not exceed 1000.
#
#
#


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


# @lc code=start


def copy_random_list_v1(head):
    if not head:
        return None
    if not head.next:
        result = Node(head.val, None)
        if head.random == head:
            result.random = result
        return result

    old2new = {}
    old = head
    while old:
        old2new[old] = Node(old.val)
        old = old.next

    old = head
    while old:
        new = old2new[old]
        new.next = old2new[old.next] if old.next else None
        new.random = old2new[old.random] if old.random else None
        old = old.next

    return old2new[head]


def copy_random_list_v2(head_old):
    # https://www.youtube.com/watch?v=EHpS2TBfWQg
    if not head_old:
        return None

    head_new = Node(head_old.val)

    node_old, node_new, next_old = head_old, head_new, head_old.next
    while node_old.next:
        next_old = node_old.next
        next_new = Node(next_old.val)
        node_new.next = next_new
        node_old, node_new = next_old, next_new

    node_old, node_new = head_old, head_new
    while node_old:
        next_old = node_old.next
        next_new = node_new.next
        node_old.next = node_new
        node_new.random = node_old
        node_old, node_new = next_old, next_new

    node_new = head_new
    while node_new:
        node_new.random = node_new.random.random.next if node_new.random.random else None
        node_new = node_new.next

    return head_new


class Solution:
    def copyRandomList(self, head):
        return copy_random_list_v2(head)


# @lc code=end
