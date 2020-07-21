"""
submits:
  - date: 2020-04-12
    cheating: false
"""

#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
# https://leetcode.com/problems/gas-station/description/
#
# algorithms
# Medium (36.68%)
# Likes:    1345
# Dislikes: 356
# Total Accepted:    190.4K
# Total Submissions: 514K
# Testcase Example:  '[1,2,3,4,5]\n[3,4,5,1,2]'
#
# There are N gas stations along a circular route, where the amount of gas at
# station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from station i to its next station (i+1). You begin the journey with
# an empty tank at one of the gas stations.
#
# Return the starting gas station's index if you can travel around the circuit
# once in the clockwise direction, otherwise return -1.
#
# Note:
#
#
# If there exists a solution, it is guaranteed to be unique.
# Both input arrays are non-empty and have the same length.
# Each element in the input arrays is a non-negative integer.
#
#
# Example 1:
#
#
# Input:
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
#
# Output: 3
#
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 +
# 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to
# station 3.
# Therefore, return 3 as the starting index.
#
#
# Example 2:
#
#
# Input:
# gas  = [2,3,4]
# cost = [3,4,3]
#
# Output: -1
#
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to
# the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 =
# 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you
# only have 3.
# Therefore, you can't travel around the circuit once no matter where you
# start.
#
#
#

# @lc code=start
from typing import List


def main_v1(gas: List[int], cost: List[int]) -> int:
    """
    time: O(n*n)
    space: O(n)
    """
    l = len(gas)

    def has_route(start: int) -> bool:
        tank = 0
        for i in range(start, start + l + 1):
            tank += gas[i % l]

            # travel to next station
            tank -= cost[i % l]
            if tank < 0:
                return False

        return True

    scores = []
    for i in range(l):
        score = gas[i] - cost[i % l]
        scores.append((score, i))
    scores.sort()
    scores.reverse()
    for score, index in scores:
        if score < 0:
            break
        if has_route(index):
            return index
    return -1


def main_v2(gas: List[int], cost: List[int]) -> int:
    """
    time: O(n)
    space: O(n)
    """

    # the start index
    s = 0
    tank = 0
    # the gas left if we start at `0` and travel to `i`
    gas_needed = 0

    for i in range(0, len(gas)):
        tank += gas[i] - cost[i]

        if tank < 0:
            # if we start at `s`, we are not able to travel to `i+1`.
            #   |
            #   V
            # if we start at any index `j` where `s <= j <= i`, we are not able to travel to `i+1`.
            #   |
            #   V
            # if start at any index `j` where `0 <= j <= i`, we are not able to travel to `i+1`.
            #   |
            #   V
            # So the start point must be larger then `i`

            # if we want to travel from `s` to `i+1`, we need at least `-tank` gas in the tank when we are at `s`.
            # So we need `gas_needed = gas_needed + (-tank)` gas in the tank if we want to travel from 0 to `i+1`.
            gas_needed += -tank

            s = i + 1
            tank = 0

    # After the for loop above, `s` is the start index, `gas_needed` is the gas needed for traveling from 0 to `s`,
    # tank is the left gas from `s` to `len(gas)`.

    return s if tank >= gas_needed else -1


main = main_v2


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return main(gas, cost)


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")

    t.assertEqual(main([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
    t.assertEqual(main([2, 3, 4], [3, 4, 3]), -1)
