"""
submits:
  - date: 2020-08-11
    minutes: 65
    cheating: false
labels: [dp]
comment: 这道题一开始没有想到用 dp 去做，后来看了题目中的 tags 之后知道可以用 dp 做，之后就很简单了
"""

#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#
# https://leetcode.com/problems/predict-the-winner/description/
#
# algorithms
# Medium (47.37%)
# Likes:    1518
# Dislikes: 89
# Total Accepted:    70.8K
# Total Submissions: 147.8K
# Testcase Example:  '[1,5,2]'
#
# Given an array of scores that are non-negative integers. Player 1 picks one
# of the numbers from either end of the array followed by the player 2 and then
# player 1 and so on. Each time a player picks a number, that number will not
# be available for the next player. This continues until all the scores have
# been chosen. The player with the maximum score wins.
#
# Given an array of scores, predict whether player 1 is the winner. You can
# assume each player plays to maximize his score.
#
# Example 1:
#
#
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2.
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If
# player 2 chooses 5, then player 1 will be left with 1 (or 2).
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
# Hence, player 1 will never be the winner and you need to return False.
#
#
#
#
# Example 2:
#
#
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5
# and 7. No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to
# return True representing player1 can win.
#
#
#
# Constraints:
#
#
# 1 <= length of the array <= 20.
# Any scores in the given array are non-negative integers and will not exceed
# 10,000,000.
# If the scores of both players are equal, then player 1 is still the winner.
#
#
#

from typing import List

# @lc code=start


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = []
        for i in range(len(nums)):
            dp.append([None] * len(nums))

        def get_best_score(i: int, j: int):
            # 如果当前只剩下 nums[i:j+1] 这些数字，那么 player1 最多可以获得多少分（分数可能为负数）
            if not (0 <= i <= j < len(nums)):
                return 0

            if i == j:
                return nums[i]

            assert dp[i][j] is not None
            return dp[i][j]

        for j in range(0, len(nums)):
            for i in range(j, -1, -1):
                next_player_is_1 = (j - i + 1) % 2 == len(nums) % 2
                # print("next_player_is_1:", next_player_is_1)

                if next_player_is_1:
                    # 接下来轮到 player 1 出手

                    # player1 选择 nums[i]
                    case1 = nums[i] + get_best_score(i + 1, j)
                    # player1 选择 nums[j]
                    case2 = nums[j] + get_best_score(i, j - 1)

                    # player1 会选择让自己分数最多的方式
                    best_case = max(case1, case2)

                else:
                    # 接下来轮到 player 2 出手

                    # player2 选择 nums[i]
                    case1 = get_best_score(i + 1, j)
                    # player2 选择 nums[j]
                    case2 = get_best_score(i, j - 1)

                    # player2 会选择让 player1 分数最少的方式
                    best_case = min(case1, case2)

                dp[i][j] = best_case

        best_score = dp[0][len(nums) - 1]
        return best_score + best_score >= sum(nums)


# @lc code=end
if __name__ == "__main__":
    f = Solution().PredictTheWinner

    assert f([1, 5, 2]) is False
    assert f([1, 5, 233, 7]) is True
