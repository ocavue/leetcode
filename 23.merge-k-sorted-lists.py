"""
submits:
  - minutes: 33
    cheating: false
    date: 2020-08-07
comment: |
  这道题我使用的思路是类似 Merge Sort 的思路（如果每一个 list 都只有一个元素，那么这道题就是一道
  排序算法题目）。在一开始使用 Merge Sort 的思路时候，我翻了一个错误，就是先把前两个列表合并，然后
  把合并后的结果和第三个列表合并，然后再和第四个列表合并，以此类推。这样的做法在某些场景中会很慢，比
  如说：[[0],[1],[2],[3],[4],[5],[6],[7],[8] ...] 这种情况。正确的做法应该是先两两合并，然后
  再四四合并，然后再八八合并，从而尽可能地确保不会出现特别长的 list，因为合并两个 list 的算法复杂度
  是 O(两个列表长度的合)。
  下面评估这种做法的算法复杂度。假设有 N 个列表，每个列表的长度不超过 K，那么时间复杂度就需要
    (每次合并需要多少次比较操作) *  (多少次合并)
         L * N/2
    +  2*L * N/4
    +  4*L * N/8
    +  8*L * N/16
    + 16*L * N/32
    + ....
    = O( N * K * log(N) )
  但是使用 Priority-Queue（比如说 Heap）的话可以实现 O( K * log(N) ) 的时间复杂度。以后可以按照
  这种方式做一下。
labels:
  - Priority-Queue
  - Heap
"""

# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (38.33%)
# Likes:    4964
# Dislikes: 296
# Total Accepted:    669K
# Total Submissions: 1.7M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
#
# Example:
#
#
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
#
#
#

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1

    # assert l1
    # assert l2
    # assert l1.val is not None
    # assert l2.val is not None

    result_root = None
    if l1.val <= l2.val:
        result_root = ListNode(l1.val)
        l1 = l1.next
    else:
        result_root = ListNode(l2.val)
        l2 = l2.next

    curr = result_root
    while l1 and l2:
        # assert l1.val is not None
        # assert l2.val is not None

        if l1.val <= l2.val:
            curr.next = ListNode(l1.val)
            l1 = l1.next
        else:
            curr.next = ListNode(l2.val)
            l2 = l2.next

        curr = curr.next

    # assert curr.next is None
    curr.next = l1 or l2 or None
    return result_root


def merge_k_lists(lists: List[ListNode]) -> ListNode:
    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]
    m = len(lists) // 2
    l1 = merge_k_lists(lists[:m])
    l2 = merge_k_lists(lists[m:])
    return merge_two_lists(l1, l2)


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return merge_k_lists(lists)


# @lc code=end

