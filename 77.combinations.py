#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (55.71%)
# Likes:    1810
# Dislikes: 74
# Total Accepted:    320.6K
# Total Submissions: 571.9K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
#
# You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#
# Example 2:
#
#
# Input: n = 1, k = 1
# Output: [[1]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
# 1 <= k <= n
#
#
#

from typing import List

# @lc code=start


def combine(lo: int, hi: int, k: int) -> List[List[int]]:
    assert lo <= hi

    if hi - lo + 1 == k:
        return [list(range(lo, hi + 1))]
    if hi - lo + 1 < k:
        return []
    if k == 0:
        return []
    if k == 1:
        return [[i] for i in range(lo, hi + 1)]

    result: List[List[int]] = []
    # 结果包含 hi
    for nums in combine(lo, hi - 1, k - 1):
        assert len(nums) == k - 1
        nums.append(hi)
        assert len(nums) == k
        result.append(nums)
    # 结果不包含 hi
    for nums in combine(lo, hi - 1, k):
        assert len(nums) == k
        result.append(nums)
    return result


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combine(1, n, k)


# @lc code=end
if __name__ == "__main__":
    from tool import test

    t = test()
    f = Solution().combine
    t.assertEqual(
        sorted(f(n=4, k=2)),
        sorted([[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
    )
