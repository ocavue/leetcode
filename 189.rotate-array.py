#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (33.11%)
# Likes:    2212
# Dislikes: 752
# Total Accepted:    417.7K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
#
# Example 1:
#
#

# n = 7

# Input:  [1,2,3,4,5,6,7] and k = 1
# Output: [7,1,2,3,4,5,6]
# Input:  [1,2,3,4,5,6,7] and k = 2
# Output: [6,7,1,2,3,4,5]
# Input:  [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Input:  [1,2,3,4,5,6,7] and k = 4
# Output: [4,5,6,7,1,2,3]

# n = 8

# Input:  [1,2,3,4,5,6,7,8] and k = 1
# Output: [8,1,2,3,4,5,6,7]
# Input:  [1,2,3,4,5,6,7,8] and k = 2
# Output: [7,8,1,2,3,4,5,6]


# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?
#
#


# @lc code=start

from typing import List, TypeVar

DEBUG = False
T = TypeVar


def log(*args, **kw):
    if DEBUG:
        print(*args, **kw)


def get_next_position(origin_position: int, n: int, k: int) -> None:
    return (origin_position + k) % n


def jump_for_one_revolution(nums: List[T], n: int, k: int, start_index: int) -> int:
    curr = start_index
    steps = 0
    flying_val = nums[curr]
    while True:
        next = get_next_position(curr, n, k)
        log(f"{curr} -> {next}")

        # Switch the flying value and nums[next]
        flying_val, nums[next] = nums[next], flying_val

        curr = next
        steps += 1

        if curr == start_index:
            assert 0 < steps <= n, f"error. steps:{steps}; n:{n};"
            assert n % steps == 0, f"error. steps:{steps}; n:{n};"
            return steps


def rotate(nums: List[T], k: int) -> None:
    n = len(nums)
    k = k % n
    assert 0 <= k < n

    if k == 0:
        return None
    else:
        steps = jump_for_one_revolution(nums=nums, n=n, k=k, start_index=0)
        log("steps:", steps)
        rotate_times = n // steps
        for i in range(1, rotate_times):
            s = jump_for_one_revolution(nums=nums, n=n, k=k, start_index=i)
            log("steps:", s)
            assert steps == s
        log("done")


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotate(nums, k)


# @lc code=end
if __name__ == "__main__":
    DEBUG = True

    l = [1, 2, 3, 4, 5, 6, 7, 8]
    rotate(l, 2)
    assert l == [7, 8, 1, 2, 3, 4, 5, 6]

    l = [1, 2, 3, 4, 5, 6, 7]
    rotate(l, 3)
    assert l == [5, 6, 7, 1, 2, 3, 4]
