"""
submits:
- date: 2020-11-30
  minutes: 24
  cheating: false
"""
#
# @lc app=leetcode id=756 lang=python3
#
# [756] Pyramid Transition Matrix
#
# https://leetcode.com/problems/pyramid-transition-matrix/description/
#
# algorithms
# Medium (55.02%)
# Likes:    332
# Dislikes: 360
# Total Accepted:    22.4K
# Total Submissions: 40.4K
# Testcase Example:  '"BCD"\n["BCG","CDE","GEA","FFF"]'
#
# We are stacking blocks to form a pyramid. Each block has a color which is a
# one letter string.
#
# We are allowed to place any color block C on top of two adjacent blocks of
# colors A and B, if and only if ABC is an allowed triple.
#
# We start with a bottom row of bottom, represented as a single string. We also
# start with a list of allowed triples allowed. Each allowed triple is
# represented as a string of length 3.
#
# Return true if we can build the pyramid all the way to the top, otherwise
# false.
#
# Example 1:
#
#
# Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
# Output: true
# Explanation:
# We can stack the pyramid like this:
# ⁠   A
# ⁠  / \
# ⁠ G   E
# ⁠/ \ / \
# B   C   D
#
# We are allowed to place G on top of B and C because BCG is an allowed
# triple.  Similarly, we can place E on top of C and D, then A on top of G and
# E.
#
#
#
# Example 2:
#
#
# Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
# Output: false
# Explanation:
# We can't stack the pyramid to the top.
# Note that there could be allowed triples (A, B, C) and (A, B, D) with C !=
# D.
#
#
#
# Constraints:
#
#
# bottom will be a string with length in range [2, 8].
# allowed will have length in range [0, 200].
# Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E',
# 'F', 'G'}.
#
#
#

# @lc code=start

from typing import List, Dict
from collections import defaultdict

"""
>>> iter_product( [ [A,B], [C,D,E] ] )
A + C
A + D
A + E
B + C
B + D
B + E
"""


def iter_product(lists: List[List[str]]):
    if len(lists) == 0:
        yield from []
    elif len(lists) == 1:
        yield from lists[0]
    else:
        for i in lists[0]:
            for j in iter_product(lists[1:]):
                yield i + j


def pyramid_transition(bottom: str, allowed: Dict[str, List[str]]) -> bool:
    assert len(bottom) >= 2
    if len(bottom) == 2:
        return bottom in allowed and len(allowed[bottom]) >= 1
    else:
        next_candidates = []
        for i in range(len(bottom) - 1):
            bottom_pair = bottom[i] + bottom[i + 1]
            next_candidates.append(allowed[bottom_pair])
        # print(next_candidates)
        for next_bottom_candidate in iter_product(next_candidates):
            assert len(next_bottom_candidate) == len(bottom) - 1
            if pyramid_transition(next_bottom_candidate, allowed):
                return True
        return False


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_map: Dict[str, List[str]] = defaultdict(list)
        for a, b, c in allowed:
            allowed_map[a + b].append(c)
        return pyramid_transition(bottom, allowed_map)


# @lc code=end

if __name__ == "__main__":
    from tool import t

    t(list(iter_product([["A", "B"], ["C", "D", "E"]])), ["AC", "AD", "AE", "BC", "BD", "BE",])
    t(list(iter_product([["A", "B"], ["C", "D", "E"], []])), [])

    f = Solution().pyramidTransition
    t(f("BCD", allowed=["BCG", "CDE", "GEA", "FFF"]), True)
    t(f( "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]), False)
