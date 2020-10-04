"""
submits:
- date: 2020-10-04
  minute: 35
  cheating: false
"""
#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (46.46%)
# Likes:    1977
# Dislikes: 88
# Total Accepted:    98.4K
# Total Submissions: 200.1K
# Testcase Example:  '"aab"'
#
# Given a string S, check if the letters can be rearranged so that two
# characters that are adjacent to each other are not the same.
#
# If possible, output any possible result.  If not possible, return the empty
# string.
#
# Example 1:
#
#
# Input: S = "aab"
# Output: "aba"
#
#
# Example 2:
#
#
# Input: S = "aaab"
# Output: ""
#
#
# Note:
#
#
# S will consist of lowercase letters and have length in range [1, 500].
#
#
#
#
#

from tool import test

# @lc code=start
import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_times = max(counter.values())
        row_count = max_times

        rows = []
        for _ in range(row_count):
            rows.append([])

        heap = []
        for char, times in counter.items():
            heapq.heappush(heap, (-times, char))

        row_index = 0
        while heap:
            times, char = heapq.heappop(heap)
            times = -1 * times
            for _ in range(times):
                rows[row_index].append(char)
                row_index = (row_index + 1) % row_count
                assert 0 <= row_index < row_count

        # print(rows)
        result = ""
        for row in rows:
            for char in row:
                if result and result[-1] == char :
                    return ""
                result = result + char
        return result

        # counter = Counter(s)
        # heap = []
        # for char, times in counter.items():
        #     heapq.heappush(heap, (-times, -1, char))

        # result = ""

        # index = 0
        # while heap:
        #     times, _, char = heapq.heappop(heap)
        #     prev_char = result[-1] if result else ""
        #     if prev_char == char:
        #         return ""
        #     else:
        #         result = result + char
        #         print(result)
        #         if times < -1:
        #             heapq.heappush(heap, (times + 1, index, char))

        #     index += 1
        # return result


# @lc code=end
if __name__ == "__main__":
    t = test()
    f = Solution().reorganizeString
    t.assertEqual(f("aab"), "aba")
    t.assertEqual(f("aaab"), "")
    t.assertEqual(f("vvl"), "vlv")
    t.assertEqual(f("vvlo"), "vlvo")
    t.assertEqual(f("vvlvo"), "vlvov")
