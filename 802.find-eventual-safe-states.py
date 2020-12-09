"""
submits:
- date: 2020-12-09
  minutes: 13
  cheating: false
labels:
- dp
"""
#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#
# https://leetcode.com/problems/find-eventual-safe-states/description/
#
# algorithms
# Medium (49.17%)
# Likes:    965
# Dislikes: 183
# Total Accepted:    45.9K
# Total Submissions: 92.8K
# Testcase Example:  '[[1,2],[2,3],[5],[0],[5],[],[]]'
#
# We start at some node in a directed graph, and every turn, we walk along a
# directed edge of the graph. If we reach a terminal node (that is, it has no
# outgoing directed edges), we stop.
#
# We define a starting node to be safe if we must eventually walk to a terminal
# node. More specifically, there is a natural number k, so that we must have
# stopped at a terminal node in less than k steps for any choice of where to
# walk.
#
# Return an array containing all the safe nodes of the graph. The answer should
# be sorted in ascending order.
#
# The directed graph has n nodes with labels from 0 to n - 1, where n is the
# length of graph. The graph is given in the following form: graph[i] is a list
# of labels j such that (i, j) is a directed edge of the graph, going from node
# i to node j.
#
#
# Example 1:
#
#
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above.
#
#
# Example 2:
#
#
# Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# Output: [4]
#
#
#
# Constraints:
#
#
# n == graph.length
# 1 <= n <= 10^4
# 0 <= graph[i].legnth <= n
# graph[i] is sorted in a strictly increasing order.
# The graph may contain self-loops.
# The number of edges in the graph will be in the range [1, 4 * 10^4].
#
#
#

from typing import List, Union

# @lc code=start
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_map: List[Union[bool, None]] = [None] * len(graph)

        def is_safe(index: int) -> bool:
            if safe_map[index] is None:
                if not graph[index]:
                    safe_map[index] = True
                else:
                    safe_map[index] = False
                    has_unsafe = False
                    for next_index in graph[index]:
                        if not is_safe(next_index):
                            has_unsafe = True
                            break
                    if not has_unsafe:
                        safe_map[index] = True
            return safe_map[index]

        result = []
        for i in range(len(graph)):
            if is_safe(i):
                result.append(i)
        return result


# @lc code=end
if __name__ == "__main__":
    from tool import t

    f = Solution().eventualSafeNodes
    t(f([[1, 2], [2, 3], [5], [0], [5], [], []]), [2, 4, 5, 6])
    t(f([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]), [4])

