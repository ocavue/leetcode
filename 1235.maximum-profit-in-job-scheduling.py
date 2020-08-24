"""
submits:
- date: 2020-08-24
  minutes: 120
  cheating: false
labels: [dp]
comment: |
  这道题我的思路是对的，不过一开始还不足够清晰，重写了一遍才达到能够接受的程度。
"""
# 13:15 14:00
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
#
# algorithms
# Hard (43.90%)
# Likes:    550
# Dislikes: 7
# Total Accepted:    14.3K
# Total Submissions: 32.4K
# Testcase Example:  '[1,2,3,3]\n[3,4,5,6]\n[50,10,40,70]'
#
# We have n jobs, where every job is scheduled to be done from startTime[i] to
# endTime[i], obtaining a profit of profit[i].
#
# You're given the startTime , endTime and profit arrays, you need to output
# the maximum profit you can take such that there are no 2 jobs in the subset
# with overlapping time range.
#
# If you choose a job that ends at time X you will be able to start another job
# that starts at time X.
#
#
# Example 1:
#
#
#
#
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job.
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
#
#
# Example 2:
#
# ⁠
#
#
#
# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job.
# Profit obtained 150 = 20 + 70 + 60.
#
#
# Example 3:
#
#
#
#
# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6
#
#
#
# Constraints:
#
#
# 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
# 1 <= startTime[i] < endTime[i] <= 10^9
# 1 <= profit[i] <= 10^4
#
#
#

# @lc code=start

from collections import namedtuple
from typing import List, Dict, Tuple

Job = namedtuple("Job", ["start_time", "end_time", "profit"])


def reverse_bisect_left(reversed: List[int], target: int) -> Tuple[bool, int]:
    if not reversed:
        return False, 0
    if target > reversed[0]:
        return False, 0
    if target < reversed[-1]:
        return False, len(reversed)
    if len(reversed) == 1 and reversed[0] == target:
        return True, 0

    lo, hi = 0, len(reversed) - 1
    assert lo < hi
    while lo < hi:
        mi = (lo + hi) // 2
        if reversed[mi] > target:
            lo = mi
        elif reversed[mi] < target:
            hi = mi
        else:
            return True, mi

        if hi - lo <= 1:
            if reversed[lo] == target:
                return True, lo
            if reversed[hi] == target:
                return True, hi
            return False, hi
    return False, lo


class DP:
    def __init__(self):
        # key 是 start_time, value 是以这个时间点（或者更晚的时间）开始能获得的最大收益。
        self.map: Dict[int, int] = {}

        # start_times 严格递减
        self.start_times: List[int] = []

        self.best_profit = 0

    def add(self, start_time: int, profit: int):
        if start_time in self.map:
            assert profit >= self.map[start_time]
            self.map[start_time] = profit
        else:
            self.map[start_time] = profit
            assert len(self.start_times) == 0 or self.start_times[-1] > start_time
            self.start_times.append(start_time)

        assert profit >= self.best_profit  # 给你的时间更充裕了，那肯定不能降低收益呀
        self.best_profit = profit


def find_best_profit(job: Job, dp: DP) -> int:
    # 情况一：不做这个 job
    profit1 = 0
    matched, next_index = reverse_bisect_left(dp.start_times, job.start_time)
    if matched:
        profit1 = dp.map[dp.start_times[next_index]]
    else:
        next_index = next_index - 1
        if 0 <= next_index < len(dp.start_times):
            profit1 = dp.map[dp.start_times[next_index]]

    # 情况二：做这个 job
    profit2 = job.profit
    matched, next_index = reverse_bisect_left(dp.start_times, job.end_time)

    if matched:
        profit2 += dp.map[dp.start_times[next_index]]
    else:
        next_index = next_index - 1
        if 0 <= next_index < len(dp.start_times):
            profit2 += dp.map[dp.start_times[next_index]]

    # print(job, profit1, profit2, max(profit1, profit2))

    return max(profit1, profit2)


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [Job(start_time=s, end_time=e, profit=p) for s, e, p in zip(startTime, endTime, profit)]
        jobs.sort()

        dp = DP()

        for i in range(len(jobs) - 1, -1, -1):
            job = jobs[i]
            best_profit = find_best_profit(job, dp)
            dp.add(job.start_time, best_profit)

        return dp.best_profit


# @lc code=end
if __name__ == "__main__":
    f = Solution().jobScheduling

    import unittest

    t = unittest.TestCase("__init__")
    t.assertEqual(f(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]), 120)
    t.assertEqual(f(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9], profit=[20, 20, 100, 70, 60]), 150)
    t.assertEqual(f(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]), 6)
