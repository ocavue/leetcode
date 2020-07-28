"""
submits:
  - date: 2020-07-28
    cheating: false
    minutes: 15
labels: []
comment: |
  这道题出的很差劲：
  1. "Letters also wrap around." 令人很难理解。
  2. 这道题明显使用二分法是算法复杂度最低的做法，但是我直接遍历一遍竟然也通过测试了。
  3. 完全不知道为什么题目中会带有 heap | depth-first-search | breadth-first-search | graph 的标签。
  学到的经验就是做题前要看 Likes 和 Dislikes 的数据。Dislikes 比例太高的题目（比如这一道）就不应该去做。
  额外的收获：在最后看答案的时候，发现 python 自带了一个叫做 bisect 的库，可以方便地进行二分法操作。
"""

#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
#
# algorithms
# Easy (44.88%)
# Likes:    411
# Dislikes: 519
# Total Accepted:    75.7K
# Total Submissions: 166.9K
# Testcase Example:  '["c","f","j"]\n"a"'
#
#
# Given a list of sorted characters letters containing only lowercase letters,
# and given a target letter target, find the smallest element in the list that
# is larger than the given target.
#
# Letters also wrap around.  For example, if the target is target = 'z' and
# letters = ['a', 'b'], the answer is 'a'.
#
#
# Examples:
#
# ),dict(
# letters = ["c", "f", "j"]
# target = "a"
# output = "c"
#
# ),dict(
# letters = ["c", "f", "j"]
# target = "c"
# output = "f"
#
# ),dict(
# letters = ["c", "f", "j"]
# target = "d"
# output = "f"
#
# ),dict(
# letters = ["c", "f", "j"]
# target = "g"
# output = "j"
#
# ),dict(
# letters = ["c", "f", "j"]
# target = "j"
# output = "c"
#
# ),dict(
# letters = ["c", "f", "j"]
# target = "k"
# output = "c"
#
#
#
# Note:
#
# letters has a length in range [2, 10000].
# letters consists of lowercase letters, and contains at least 2 unique
# letters.
# target is a lowercase letter.
#
#
#

from typing import List

# @lc code=start


class Solution:
    def nextGreatestLetter(self, ls: List[str], target: str) -> str:
        # assert sorted(ls) == ls
        # assert len(target) == 1
        # assert len(ls) >= 2

        if target >= ls[-1]:
            return self.nextGreatestLetter(ls, chr(ord("a") - 1))
        if target < ls[0]:
            return ls[0]

        for c in ls:
            if c > target:
                return c


# @lc code=end


if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().nextGreatestLetter

    for d in [
        dict(letters=["c", "f", "j"], target="a", output="c",),
        dict(letters=["c", "f", "j"], target="c", output="f",),
        dict(letters=["c", "f", "j"], target="d", output="f",),
        dict(letters=["c", "f", "j"], target="g", output="j",),
        dict(letters=["c", "f", "j"], target="j", output="c",),
        dict(letters=["c", "f", "j"], target="k", output="c",),
    ]:
        t.assertEqual(f(d["letters"], d["target"]), d["output"])

