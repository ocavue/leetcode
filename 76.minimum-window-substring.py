"""
submits:
  - minutes: 55
    date: 2020-08-13
    cheating: false
labels:
  - "two-pointers"
"""
#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (33.43%)
# Likes:    4732
# Dislikes: 327
# Total Accepted:    412.6K
# Total Submissions: 1.2M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
#
# Example:
#
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
#
# Note:
#
#
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
#
#
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0:
            return ""
        if len(t) == 0:
            return ""

        # 遍历窗口为 s[i:j] 里的数字
        # 其中 0 <= i <= j <= len(s)
        i = 0
        j = 0

        # 当前窗口中各个数字有多少？
        received = {char: 0 for char in t}

        # 期待每个数字出现了多少次？注意 t 中可能有重复的数字
        expected = {}
        for char in t:
            expected[char] = expected.get(char, 0) + 1

        # 当前窗口中达到预期的数字
        matched = set()

        # 迄今为止最优的窗口长度
        best_i = 0
        best_j = len(s)

        # 用于检查当前 i j 是否是最优解
        # i 和 j 中任意一个值改变了之后都需要调用这个函数
        def check_best_window(i, j):
            nonlocal best_i, best_j
            if len(matched) == len(expected):
                if j - i < best_j - best_i:
                    best_i, best_j = i, j

        while True:

            # print(f"loop start  i:{i}, j:{j}, best_i:{best_i}, best_j:{best_j}",received)

            # assert 0 <= i <= j <= len(s)

            # 第一部分：优先将 i 向右边移动，从而减少窗口大小
            # 如果把 i 向右边移动后，依然符合 i<j，那么就尝试移动一下
            if i + 1 < j:

                # 如果 s[i] 是有关字符，那么只有当前的窗口中有多余的这个字符时才能向右边移动
                if s[i] in expected:
                    if received[s[i]] > expected[s[i]]:
                        received[s[i]] -= 1
                        i += 1
                        check_best_window(i, j)
                        continue
                # 如果 s[i] 是无关字符，那么可以自由地把 i 向右边移动
                else:
                    i += 1
                    check_best_window(i, j)
                    continue

            # 第二部分：如果 i 不能再向右边移动了，那么我们就尝试移动 j
            if j >= len(s):
                break

            c = s[j]
            if c in received:
                received[c] += 1
                if c not in matched and received[c] >= expected[c]:
                    matched.add(c)

            j += 1
            check_best_window(i, j)

            # assert 0 <= i <= j <= len(s)
            # print(f"loop result i:{i}, j:{j}, best_i:{best_i}, best_j:{best_j}",received)

        if len(matched) == len(expected):
            return s[best_i:best_j]
        else:
            return ""


# @lc code=end
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")
    f = Solution().minWindow
    # t.assertEqual(f("XADOBECODEBANC123", "ABC"), "BANC")
    # t.assertEqual(f("XADOBECODEBANC", "ABC"), "BANC")
    # t.assertEqual(f("ADOBECODEBANC", "ABC"), "BANC")
    # t.assertEqual(f("XXXXXXXXXXXAB", "ABC"), "")
    # t.assertEqual(f("a", "a"), "a")
    # t.assertEqual(f("ab", "a"), "a")
    t.assertEqual(f("aa", "aa"), "aa")
