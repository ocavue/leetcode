#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (51.58%)
# Likes:    1527
# Dislikes: 252
# Total Accepted:    164.2K
# Total Submissions: 314.5K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
#
#
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
#
#
# Write a function to compute the next state (after one update) of the board
# given its current state. The next state is created by applying the above
# rules simultaneously to every cell in the current state, where births and
# deaths occur simultaneously.
#
# Example:
#
#
# Input:
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
#
#
# Follow up:
#
#
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
#
#
#

from typing import List

# @lc code=start

DEAD_TO_DEAD = 0
DEAD_TO_LIVE = 2
LIVE_TO_LIVE = 1
LIVE_TO_DEAD = 3


class Solution:
    def gameOfLife(self, input_board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        这道题最有趣的地方在于，使用除了 0 1 之外的其他数字来表示它原来和现在属于什么类型
        """

        row_length = len(input_board)
        col_length = len(input_board[0])

        def get_live_neighbors(row, col):
            lives = 0
            for r in [row - 1, row, row + 1]:
                for c in [col - 1, col, col + 1]:
                    if (r, c) != (row, col):
                        if 0 <= r < row_length and 0 <= c < col_length:
                            cell = input_board[r][c]
                            if cell == LIVE_TO_DEAD or cell == LIVE_TO_LIVE:
                                lives += 1
            return lives

        for row in range(row_length):
            for col in range(col_length):
                cell = input_board[row][col]
                lives = get_live_neighbors(row, col)
                if cell == LIVE_TO_DEAD or cell == LIVE_TO_LIVE:
                    # Any live cell with fewer than two live neighbors dies, as if caused by under-population.
                    # Any live cell with two or three live neighbors lives on to the next generation.
                    # Any live cell with more than three live neighbors dies, as if by over-population.
                    if lives < 2 or lives > 3:
                        input_board[row][col] = LIVE_TO_DEAD
                else:
                    # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                    if lives == 3:
                        input_board[row][col] = DEAD_TO_LIVE

        for row in range(row_length):
            for col in range(col_length):
                if input_board[row][col] == DEAD_TO_LIVE:
                    input_board[row][col] = LIVE_TO_LIVE
                elif input_board[row][col] == LIVE_TO_DEAD:
                    input_board[row][col] = DEAD_TO_DEAD


# @lc code=end
if __name__ == "__main__":
    i = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Solution().gameOfLife(i)
    assert i == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
