"""
submits:
  - date: 2020-04-16
    cheating: false

labels:
  - max/min elements in sliding window

"""

#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (40.87%)
# Likes:    2787
# Dislikes: 160
# Total Accepted:    236.8K
# Total Submissions: 573.3K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
#
# Follow up:
# Could you solve it in linear time?
#
# Example:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----

# 0  1   2   3  4  5  6  7
# [1 3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#


# @lc code=start
from typing import List, Tuple, TypeVar, Deque
from collections import deque

T = TypeVar("T")


def max_sliding_window(vals: List[T], k: int) -> List[T]:

    """

    maxs 是一个双向 queue，储存的是在当前窗口中可选的若干个最大值和他们的 index

    maxs 可以保证下面的条件：
    1. 长度永远小于等于 k
    2. 按照 值，maxs 严格单调递减，也就是说 maxs[0] 是 maxs 中最大的元素；
       按照 index，maxs 严格单调递增。
    3. 在整个算法的周期中，执行不多于 n 次插入操作，因此也执行不多于 n 次删除操作
    """
    maxs: Deque[Tuple[T, int]] = deque()

    for i in range(k):
        pair = (vals[i], i)
        # maxs.append()
        while maxs and maxs[-1] < pair:
            maxs.pop()
        maxs.append(pair)

    out: List[T] = []

    for j in range(k, len(vals) + 1):
        i = j - k
        assert 0 <= i < i + k == j <= len(vals)

        # 窗口是 [i, j)，窗口中的最后一项是 j-1

        pair = (vals[j - 1], j - 1)

        # 如果 maxs 中最大的值，目前已经不在当前窗口中了，那么移除这个最大值
        if maxs and i - 1 == maxs[0][1]:
            maxs.popleft()

        while maxs and maxs[-1] <= pair:
            maxs.pop()

        maxs.append(pair)

        out.append(maxs[0][0])

    return out


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return max_sliding_window(nums, k)


# @lc code=end
if __name__ == "__main__":
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], k=3) == [3, 3, 5, 5, 6, 7]
    assert max_sliding_window([1, -1], k=1) == [1, -1]
