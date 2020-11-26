"""
submits:
- date: 2020-11-26
  minutes: 45
  cheating: false
labels:
- bfs
"""
#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#
# https://leetcode.com/problems/open-the-lock/description/
#
# algorithms
# Medium (52.07%)
# Likes:    1276
# Dislikes: 48
# Total Accepted:    76K
# Total Submissions: 145.4K
# Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
#
# You have a lock in front of you with 4 circular wheels. Each wheel has 10
# slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can
# rotate freely and wrap around: for example we can turn '9' to be '0', or '0'
# to be '9'. Each move consists of turning one wheel one slot.
#
# The lock initially starts at '0000', a string representing the state of the 4
# wheels.
#
# You are given a list of deadends dead ends, meaning if the lock displays any
# of these codes, the wheels of the lock will stop turning and you will be
# unable to open it.
#
# Given a target representing the value of the wheels that will unlock the
# lock, return the minimum total number of turns required to open the lock, or
# -1 if it is impossible.
#
#
# Example 1:
#
#
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" ->
# "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202"
# would be invalid,
# because the wheels of the lock become stuck after the display becomes the
# dead end "0102".
#
#
# Example 2:
#
#
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation:
# We can turn the last wheel in reverse to move from "0000" -> "0009".
#
#
# Example 3:
#
#
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# Output: -1
# Explanation:
# We can't reach the target without getting stuck.
#
#
# Example 4:
#
#
# Input: deadends = ["0000"], target = "8888"
# Output: -1
#
#
#
# Constraints:
#
#
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target will not be in the list deadends.
# target and deadends[i] consist of digits only.
#
#
#

# @lc code=start

from queue import Queue

num_map = {
    "0": ("1", "9"),
    "1": ("2", "0"),
    "2": ("3", "1"),
    "3": ("4", "2"),
    "4": ("5", "3"),
    "5": ("6", "4"),
    "6": ("7", "5"),
    "7": ("8", "6"),
    "8": ("9", "7"),
    "9": ("0", "8"),
}


def get_next_keys(key):
    return [
        num_map[key[0]][0] + key[1] + key[2] + key[3],
        num_map[key[0]][1] + key[1] + key[2] + key[3],
        key[0] + num_map[key[1]][0] + key[2] + key[3],
        key[0] + num_map[key[1]][1] + key[2] + key[3],
        key[0] + key[1] + num_map[key[2]][0] + key[3],
        key[0] + key[1] + num_map[key[2]][1] + key[3],
        key[0] + key[1] + key[2] + num_map[key[3]][0],
        key[0] + key[1] + key[2] + num_map[key[3]][1],
    ]


class Solution:
    def openLock(self, deadends, target: str) -> int:
        if target in deadends:
            return -1

        passed = {deadend: -1 for deadend in deadends}
        q = Queue()
        q.put(("0000", 0))

        while not q.empty():
            key, steps = q.get()
            if key in passed:
                continue

            if key == target:
                return steps
            passed[key] = steps

            for next_key in get_next_keys(key):
                if next_key not in passed:
                    q.put((next_key, steps + 1))
        return -1


# @lc code=end
if __name__ == "__main__":
    from tool import t

    f = Solution().openLock
    t(f(["8888"], "0009"), 1)
    t(f(["8888"], "0008"), 2)
    t(f(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"), -1)

