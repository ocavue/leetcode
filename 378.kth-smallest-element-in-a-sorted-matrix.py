#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (52.35%)
# Likes:    1925
# Dislikes: 113
# Total Accepted:    163.5K
# Total Submissions: 310.3K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
#
#
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
#
#
# Example:
#
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
#
# return 13.
#
#
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n^2.
#

# @lc code=start
from typing import TypeVar, List, Optional
import heapq
from collections import namedtuple

T = TypeVar("T")

# val is the first element so the heap will sort cells by its values
Cell = namedtuple("Cell", ["val", "row_idx", "col_idx"])


class Solution:
    def kthSmallest(self, matrix: List[List[T]], k: int) -> T:
        n = len(matrix)

        removed_smallest_cells = 0
        heap: List[Cell] = []

        for row_idx in range(n):
            heapq.heappush(heap, Cell(row_idx=row_idx, col_idx=0, val=matrix[row_idx][0]))

        while removed_smallest_cells < k - 1:
            smallest_cell = heapq.heappop(heap)
            removed_smallest_cells += 1

            if smallest_cell.col_idx < n - 1:
                heapq.heappush(
                    heap,
                    Cell(
                        row_idx=smallest_cell.row_idx,
                        col_idx=smallest_cell.col_idx + 1,
                        val=matrix[smallest_cell.row_idx][smallest_cell.col_idx + 1],
                    ),
                )

        smallest_cell = heap[0]
        return smallest_cell.val


# @lc code=end
if __name__ == "__main__":
    f = Solution().kthSmallest
    assert (f([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)) == 13
    assert (f([[-5]], 1)) == -5
