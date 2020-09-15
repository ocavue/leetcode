"""
labels: [greedy]
comment: 好难。看答案 https://leetcode-cn.com/problems/task-scheduler/solution/ren-wu-diao-du-qi-by-leetcode/
submits:
- date: 2020-08-29
  cheating: true
  minutes: 80
"""
#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (47.60%)
# Likes:    3632
# Dislikes: 718
# Total Accepted:    199.7K
# Total Submissions: 397.2K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# Given a characters array tasks, representing the tasks a CPU needs to do,
# where each letter represents a different task. Tasks could be done in any
# order. Each task is done in one unit of time. For each unit of time, the CPU
# could complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the cooldown
# period between two same tasks (the same letter in the array), that is that
# there must be at least n units of time between any two same tasks.
#
# Return the least number of units of times that the CPU will take to finish
# all the given tasks.
#
#
# Example 1:
#
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.
#
#
# Example 2:
#
#
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.
#
#
# Example 3:
#
#
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation:
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle
# -> idle -> A
#
#
#
# Constraints:
#
#
# 1 <= task.length <= 10^4
# tasks[i] is upper-case English letter.
# The integer n is in the range [0, 100].
#
#
#

# @lc code=start

from typing import Dict, List, Tuple
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        if n == 0:
            return len(tasks)

        counter = Counter()
        for task in tasks:
            counter[task] += 1

        most_common = counter.most_common()

        time = 0
        max_count = -1
        slots = 0
        for task, count in most_common:
            if max_count == -1:
                max_count = count
                slots = (count - 1) * n
                time = count + slots
            elif count == max_count:
                slots -= count - 1
                time += 1
            elif count == max_count - 1:
                slots -= count
                time += 0
            elif count <= max_count - 2:
                slots -= count
                time += 0

        if slots < 0:
            return time + abs(slots)
        else:
            return time

        # q: Queue[Tuple[str, int, int]] = Queue()
        # for task, count in counter.most_common():
        #     q.put((task, count, 0))
        # del counter

        # loop = 0
        # while not q.empty():
        #     task, count, min_loop = q.get()

        #     if min_loop > loop:
        #         loop += min_loop - loop
        #         print(f'idie. cost {min_loop - loop}')
        #     assert min_loop <= loop

        #     print(f'doing {task}. cost 1')
        #     if count == 1:
        #         pass
        #     else:
        #         q.put((task, count - 1, loop + n + 1))

        #     loop += 1
        # return loop

        # pairs = [(0, -count, task) for task, count in counter.items()]
        # heapq.heapify(pairs)

        # passed_task_count, passed_idle_count = 0, 0

        # while pairs:
        #     min_idie = pairs[0][0]
        #     if min_idie == 0:
        #         idie, neg_count, task = pairs[0]

        #         print("do", task)

        #         if neg_count == -1:
        #             heapq.heappop(pairs)
        #         else:
        #             heapq.heapreplace(pairs, (n, neg_count + 1, task))

        #         for i, pair in enumerate(pairs):
        #             if pair[2] != task:
        #                 pairs[i] = (max(0, pair[0] - 1), pair[1], pair[2])
        #         passed_task_count += 1

        #         print(pairs)
        #     else:
        #         print("idie *", min_idie)
        #         for i, pair in enumerate(pairs):
        #             pairs[i] = (pair[0] - min_idie, pair[1], pair[2])
        #         passed_idle_count += min_idie
        #         print(pairs)
        #     print('loop ',passed_task_count + passed_idle_count)

        # return passed_task_count + passed_idle_count

        # task_counter = Counter(tasks)
        # idle_map: Dict[str, int] = {char: 0 for char in task_counter.keys()}

        # passed_task_count = 0
        # passed_idle_count = 0
        # while passed_task_count < len(tasks):
        #     most_common_tasks = task_counter.most_common()
        #     removed_task = ""
        #     for (task, task_count) in most_common_tasks:
        #         if idle_map[task] == 0:
        #             removed_task = task
        #             break
        #     if removed_task:
        #         passed_task_count += 1
        #         idle_map[removed_task] = n
        #         task_counter[removed_task] -= 1
        #         if task_counter[removed_task] == 0:
        #             del task_counter[removed_task]

        #         for task in idle_map.keys():
        #             if task != removed_task:
        #                 idle_map[task] = max(0, idle_map[task] - 1)
        #     else:
        #         passed_idle_count += 1
        #         for task in idle_map.keys():
        #             idle_map[task] = max(0, idle_map[task] - 1)

        # return passed_task_count + passed_idle_count


# @lc code=end

if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().leastInterval
    t.assertEqual(f(tasks=["A", "A", "A", "B", "B", "B"], n=2), 8)
    t.assertEqual(f(tasks=["A", "A", "A", "B", "B", "B"], n=0), 6)
    t.assertEqual(f(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2), 16)
