#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (41.11%)
# Likes:    2878
# Dislikes: 284
# Total Accepted:    460.9K
# Total Submissions: 1.1M
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +  '[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
#
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
#
#
#
# Example:
#
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
#
#
#
#
#

# @lc code=start
import math


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals = []
        self.mins = []

    def push(self, x: int) -> None:
        self.vals.append(x)
        self.mins.append(min([self.getMin(), x]))

    def pop(self) -> None:
        del self.vals[-1]
        del self.mins[-1]

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        if self.mins:
            return self.mins[-1]
        else:
            return math.inf


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2
