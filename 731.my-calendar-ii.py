"""
submits:
- date: 2020-10-24
  minutes: 33
  cheating: true
comment: |
  这道题使用了两个数组去记录单词和双次的 booking 记录，反直觉的是，这两个数组中，每个数字内部的多条记录可能是重合的。
"""
#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#
# https://leetcode.com/problems/my-calendar-ii/description/
#
# algorithms
# Medium (49.66%)
# Likes:    671
# Dislikes: 90
# Total Accepted:    45.8K
# Total Submissions: 92.1K
# Testcase Example:  '["MyCalendarTwo","book","book","book","book","book","book"]\n' +  '[[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]'
#
# Implement a MyCalendarTwo class to store your events. A new event can be
# added if adding the event will not cause a triple booking.
#
# Your class will have one method, book(int start, int end). Formally, this
# represents a booking on the half open interval [start, end), the range of
# real numbers x such that start <= x < end.
#
# A triple booking happens when three events have some non-empty intersection
# (ie., there is some time that is common to all 3 events.)
#
# For each call to the method MyCalendar.book, return true if the event can be
# added to the calendar successfully without causing a triple booking.
# Otherwise, return false and do not add the event to the calendar.
# Your class will be called like this: MyCalendar cal = new MyCalendar();
# MyCalendar.book(start, end)
#
# Example 1:
#
#
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(50, 60); // returns true
# MyCalendar.book(10, 40); // returns true
# MyCalendar.book(5, 15); // returns false
# MyCalendar.book(5, 10); // returns true
# MyCalendar.book(25, 55); // returns true
# Explanation:
# The first two events can be booked.  The third event can be double booked.
# The fourth event (5, 15) can't be booked, because it would result in a triple
# booking.
# The fifth event (5, 10) can be booked, as it does not use time 10 which is
# already double booked.
# The sixth event (25, 55) can be booked, as the time in [25, 40) will be
# double booked with the third event;
# the time [40, 50) will be single booked, and the time [50, 55) will be double
# booked with the second event.
#
#
#
#
# Note:
#
#
# The number of calls to MyCalendar.book per test case will be at most
# 1000.
# In calls to MyCalendar.book(start, end), start and end are integers in the
# range [0, 10^9].
#
#
#
#

# @lc code=start


class MyCalendarTwo:
    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def _has_iter(self, s1, e1, s2, e2):
        # [s1,e1) 和  [s2,e2] 没有冲突 等价于 e1 <= s2 or e2 <= s1
        # 所以 [s1,e1) 和  [s2,e2] 有冲突 等价于 e1 > s2 and e2 > s1
        return e1 > s2 and e2 > s1

    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlaps:
            if self._has_iter(i, j, start, end):
                return False
        for i, j in self.calendar:
            if self._has_iter(i, j, start, end):
                self.overlaps.append(
                    (
                        max(i, start),
                        min(j, end),
                    )
                )
        self.calendar.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end
