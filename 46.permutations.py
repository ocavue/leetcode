#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (60.49%)
# Likes:    3165
# Dislikes: 94
# Total Accepted:    527.4K
# Total Submissions: 870.2K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#
#
# @lc code=start

from typing import List, Set


class Solution:
    def permute_index(
        self, chioced_indexs: List[int], possible_indexs: Set[int]
    ) -> List[List[int]]:
        """
        >>> sorted(Solution().permute_index([], {0, 1, 2}))
        [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
        """
        if not possible_indexs:
            return [chioced_indexs]
        else:
            result: List[List[int]] = []
            for index in possible_indexs:
                next_possible_indexs = possible_indexs - {index}
                next_chioced_indexs = [*chioced_indexs, index]
                result += self.permute_index(next_chioced_indexs, next_possible_indexs)
            return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        >>> sorted(Solution().permute([1, 2, 3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        """
        permutation_indexs = self.permute_index([], set(range(len(nums))))
        permutation_numbers = []
        for indexs in permutation_indexs:
            permutation_numbers.append([nums[index] for index in indexs])
        return permutation_numbers


# @lc code=end
if __name__ == "__main__":
    import doctest

    doctest.testmod()
