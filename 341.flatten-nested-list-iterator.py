"""
submits:
  - date: 2020-04-30
    cheating: false
"""

#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#
# https://leetcode.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (51.30%)
# Likes:    1463
# Dislikes: 599
# Total Accepted:    155.7K
# Total Submissions: 301.6K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# Given a nested list of integers, implement an iterator to flatten it.
#
# Each element is either an integer, or a list -- whose elements may also be
# integers or other lists.
#
# Example 1:
#
#
#
# Input: [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns
# false,
# the order of elements returned by next should be: [1,1,2,1,1].
#
#
# Example 2:
#
#
# Input: [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns
# false,
# the order of elements returned by next should be: [1,4,6].
#
#
#
#
#

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import List


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> List["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


# @lc code=start


class NestedIterator:
    def __init__(self, nested_list: List[NestedInteger]):
        def gen(integers: List[NestedInteger]):
            for i in integers:
                if i.isInteger():
                    yield i.getInteger()
                else:
                    sub_integers = i.getList()
                    yield from gen(sub_integers)

        self.gen = gen(nested_list)
        self._next: int = False

    def next(self) -> int:
        if self._next is False:
            self.hasNext()

        result = self._next
        self._next = False
        return result

    def hasNext(self) -> bool:
        if self._next is False:
            try:
                self._next = next(self.gen)
                return True
            except StopIteration:
                return False
        else:
            return True


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end
