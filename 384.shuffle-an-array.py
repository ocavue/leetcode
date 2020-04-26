#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#
# https://leetcode.com/problems/shuffle-an-array/description/
#
# algorithms
# Medium (51.90%)
# Likes:    436
# Dislikes: 914
# Total Accepted:    111.4K
# Total Submissions: 214.1K
# Testcase Example:  '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
#
# Shuffle a set of numbers without duplicates.
#
#
# Example:
#
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
#
# // Shuffle the array [1,2,3] and return its result. Any permutation of
# [1,2,3] must equally likely to be returned.
# solution.shuffle();
#
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
#
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();
#
#
#

from typing import List
from random import randint

# @lc code=start

"""
使用 Fisher–Yates shuffle (AKA Knuth-Shuffle） 算法
"""

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return [i for i in self.nums]

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = [n for n in self.nums]
        for i in range(len(nums) - 1, -1, -1):
            j = randint(0, i)
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
        return nums


# @lc code=end

if __name__ == "__main__":
    obj = Solution([1, 2, 3])
    print(obj.reset())
    print(obj.shuffle())
