"""
submits:
- date: 2020-08-31
  minute: 60
  cheating: true
labels:
- pq
"""
#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#
# https://leetcode.com/problems/course-schedule-iii/description/
#
# algorithms
# Hard (32.81%)
# Likes:    793
# Dislikes: 33
# Total Accepted:    22.5K
# Total Submissions: 67K
# Testcase Example:  '[[100,200],[200,1300],[1000,1250],[2000,3200]]'
#
# There are n different online courses numbered from 1 to n. Each course has
# some duration(course length) t and closed on dth day. A course should be
# taken continuously for t days and must be finished before or on the dth day.
# You will start at the 1st day.
#
# Given n online courses represented by pairs (t,d), your task is to find the
# maximal number of courses that can be taken.
#
# Example:
#
#
# Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# Output: 3
# Explanation:
# There're totally 4 courses, but you can take 3 courses at most:
# First, take the 1st course, it costs 100 days so you will finish it on the
# 100th day, and ready to take the next course on the 101st day.
# Second, take the 3rd course, it costs 1000 days so you will finish it on the
# 1100th day, and ready to take the next course on the 1101st day.
# Third, take the 2nd course, it costs 200 days so you will finish it on the
# 1300th day.
# The 4th course cannot be taken now, since you will finish it on the 3300th
# day, which exceeds the closed date.
#
#
#
#
# Note:
#
#
# The integer 1 <= d, t, n <= 10,000.
# You can't take two courses simultaneously.
#
#
#
#
#

from typing import List, Tuple, Dict
from collections import defaultdict
import heapq

# @lc code=start


# 使用递归(time limit exceeded)
def schedule_v1(courses: List[List[int]]):
    courses.sort(key=lambda c: c[1])

    def get_most_courses(index: int, now: int) -> int:
        if index == len(courses):
            return 0

        # 选择一：不上这门课
        case1 = get_most_courses(index + 1, now)

        # 选择二：上这门课
        cost, deadline = courses[index]
        if now + cost > deadline:
            return case1
        else:
            case2 = 1 + get_most_courses(index + 1, now + cost)
            return max(case1, case2)

    return get_most_courses(0, 0)


# 使用动态规划(time limit exceeded)
def schedule_v2(courses: List[List[int]]):
    courses.sort(key=lambda c: c[1])

    # dp[(index, start)] 表示从 start 开始学习第 index 门课程，最多可以学多少门课
    dp: Dict[Tuple[int, int], int] = defaultdict(lambda: -1)

    to_calcute: List[Tuple[int, int]] = [(0, 0)]

    while to_calcute:
        index, start = to_calcute[-1]

        if index == len(courses):
            to_calcute.pop()
            dp[(index, start)] = 0
            continue

        # 选择一：不上这门课
        if dp[(index + 1, start)] == -1:
            to_calcute.append((index + 1, start))
            continue
        case1 = dp[(index + 1, start)]

        # 选择二：上这门课
        case2 = 0
        cost, deadline = courses[index]
        if start + cost > deadline:
            pass
        else:
            if dp[(index + 1, start + cost)] == -1:
                to_calcute.append((index + 1, start + cost))
                continue
            case2 = 1 + dp[(index + 1, start + cost)]

        dp[(index, start)] = max(case1, case2)
        assert (index, start) == to_calcute.pop()
        assert dp[(index, start)] >= 0

    return dp[(index, start)]


# 使用优先队列
def schedule_v3(courses: List[List[int]]):
    courses.sort(key=lambda c: c[1])

    heap: List[Tuple[int, int]] = []
    used_days = 0

    for cost, deadline in courses:
        if used_days + cost <= deadline:
            heapq.heappush(heap, (-cost, deadline))
            used_days += cost
        elif heap:
            max_cost = -heap[0][0]
            if max_cost > cost:
                heapq.heapreplace(heap, (-cost, deadline))
                used_days -= max_cost
                used_days += cost
    return len(heap)


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        return schedule_v3(courses)


# @lc code=end

if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().scheduleCourse

    t.assertEqual(f([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]), 3)
    t.assertEqual(f([[100, 2], [32, 50]]), 1)

