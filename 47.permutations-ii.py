#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (44.34%)
# Likes:    1606
# Dislikes: 57
# Total Accepted:    316.5K
# Total Submissions: 712.4K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
#
# Example:
#
#
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
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

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        >>> sorted(Solution().permuteUnique([1, 2, 3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        >>> sorted(Solution().permuteUnique([1, 1, 2]))
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        """
        permutation_indexs = self.permute_index([], set(range(len(nums))))
        permutation_numbers = set()
        for indexs in permutation_indexs:
            permutation_numbers.add(tuple(nums[index] for index in indexs))
        return [list(i) for i in permutation_numbers]


# @lc code=end
if __name__ == "__main__":
    import doctest

    doctest.testmod()
