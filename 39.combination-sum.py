"""
submits:
  - date: 2020-03-09
    cheating: false
"""

#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (53.44%)
# Likes:    3076
# Dislikes: 97
# Total Accepted:    471.3K
# Total Submissions: 881.8K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of
# times.
#
# Note:
#
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#
#
#
from typing import List, Set, Tuple

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        min_candidate = candidates[0]
        max_candidate = candidates[-1]

        def find_combinations(candidates: List[int], target: int) -> List[List[int]]:
            """
            candidates is a sorted list
            """
            combinations = []

            if target < min_candidate:
                return combinations

            if min_candidate <= target <= max_candidate:
                if target in candidates:
                    combinations.append([target])

            for index, candidate in enumerate(candidates):
                sub_combinations: Set[Tuple] = find_combinations(
                    candidates=candidates[index:], target=target - candidate
                )
                for sub_combination in sub_combinations:
                    combinations.append([candidate, *sub_combination])

            return combinations

        return find_combinations(candidates, target)


# @lc code=end

if __name__ == "__main__":
    print(Solution().combinationSum([2, 3, 5], 8))
