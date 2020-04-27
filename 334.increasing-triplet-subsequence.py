"""
tag: redo
"""
#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (39.83%)
# Likes:    1344
# Dislikes: 119
# Total Accepted:    129.9K
# Total Submissions: 325.9K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given an unsorted array return whether an increasing subsequence of length 3
# exists or not in the array.
#
# Formally the function should:
#
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return
# false.
#
# Note: Your algorithm should run in O(n) time complexity and O(1) space
# complexity.
#
#
# Example 1:
#
#
# Input: [1,2,3,4,5]
# Output: true
#
#
#
# Example 2:
#
#
# Input: [5,4,3,2,1]
# Output: false
#
#
#
#

from typing import List

# @lc code=start


def main(nums: List[int]) -> bool:
    n1 = n2 = float("inf")
    # n1 = so far best candidate of end element of a one-cell subsequence to form a triplet subsequence
    # n2 = so far best candidate of end element of a two-cell subsequence to form a triplet subsequence
    for n in nums:
        if n <= n1:
            n1 = n
        elif n <= n2:
            n2 = n
        else:
            return True
    return False


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        return main(nums)


# @lc code=end
if __name__ == "__main__":
    assert main([1, 2, 3, 4, 5]) is True
    assert main([5, 4, 3, 2, 1]) is False
    assert main([0, 4, 2, 1, 0, -1, -3]) is False

