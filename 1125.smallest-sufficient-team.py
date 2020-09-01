
#
# @lc app=leetcode id=1125 lang=python3
#
# [1125] Smallest Sufficient Team
#
# https://leetcode.com/problems/smallest-sufficient-team/description/
#
# algorithms
# Hard (45.34%)
# Likes:    363
# Dislikes: 8
# Total Accepted:    8.8K
# Total Submissions: 18.9K
# Testcase Example:  '["java","nodejs","reactjs"]\n[["java"],["nodejs"],["nodejs","reactjs"]]'
#
# In a project, you have a list of required skills req_skills, and a list of
# people.  The i-th person people[i] contains a list of skills that person
# has.
#
# Consider a sufficient team: a set of people such that for every required
# skill in req_skills, there is at least one person in the team who has that
# skill.  We can represent these teams by the index of each person: for
# example, team = [0, 1, 3] represents the people with skills people[0],
# people[1], and people[3].
#
# Return any sufficient team of the smallest possible size, represented by the
# index of each person.
#
# You may return the answer in any order.  It is guaranteed an answer
# exists.
#
#
# Example 1:
# Input: req_skills = ["java","nodejs","reactjs"], people =
# [["java"],["nodejs"],["nodejs","reactjs"]]
# Output: [0,2]
#
# Example 2:
# Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"],
# people =
# [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# Output: [1,2]
#
#
# Constraints:
#
#
# 1 <= req_skills.length <= 16
# 1 <= people.length <= 60
# 1 <= people[i].length, req_skills[i].length, people[i][j].length <= 16
# Elements of req_skills and people[i] are (respectively) distinct.
# req_skills[i][j], people[i][j][k] are lowercase English letters.
# Every skill in people[i] is a skill in req_skills.
# It is guaranteed a sufficient team exists.
#
#
#

# @lc code=start

from typing import List, Set, Iterable, Tuple


def is_sufficient(
    skill_bitmaps: List[int], chosen_bitmap: int, max_bit: int,
):
    team_skill = 0
    for i, skill in enumerate(skill_bitmaps):
        if (2 ** i) | chosen_bitmap == chosen_bitmap:
            team_skill |= skill
    return team_skill == max_bit


def search_min_team_size(skill_bitmaps: List[int], chosen_bitmap: int, max_bit: int, index: int, size: int) -> Tuple[int, int]:

    # assert get_ones_from_bitmap(chosen_bitmap) == size, f"chosen_bitmap: {bin(chosen_bitmap)}; size: {size}"
    # assert is_sufficient(skill_bitmaps, chosen_bitmap, max_bit)

    if index == len(skill_bitmaps):
        return chosen_bitmap, size

    if chosen_bitmap | (2 ** index) != chosen_bitmap:
        # 第 index 个人已经被解雇了
        return search_min_team_size(skill_bitmaps, chosen_bitmap, max_bit, index + 1, size)

    # 对于第 index 个人，有两种选择：解雇或者不解雇

    # 不解雇
    next_chosen_bitmap_1, next_size_1 = search_min_team_size(skill_bitmaps, chosen_bitmap, max_bit, index + 1, size)

    # 解雇
    new_chosen_bitmap = chosen_bitmap - (2 ** index)
    # assert get_ones_from_bitmap(chosen_bitmap) - get_ones_from_bitmap(new_chosen_bitmap) == 1

    if is_sufficient(skill_bitmaps, new_chosen_bitmap, max_bit):
        next_chosen_bitmap_2, next_size_2 = search_min_team_size(skill_bitmaps, new_chosen_bitmap, max_bit, index + 1, size - 1)

        if next_size_1 < next_size_2:
            return next_chosen_bitmap_1, next_size_1
        else:
            return next_chosen_bitmap_2, next_size_2
    else:
        return next_chosen_bitmap_1, next_size_1


def get_indexs_from_bitmap(bitmap: int) -> List[int]:
    indexs: List[int] = []

    for i in range(bitmap.bit_length()):
        if (2 ** i) | bitmap == bitmap:
            indexs.append(i)
    return indexs


def get_ones_from_bitmap(bitmap: int) -> int:
    ones = 0
    for i in range(bitmap.bit_length()):
        if (2 ** i) | bitmap == bitmap:
            ones += 1
    return ones


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        max_bit = 2 ** len(req_skills) - 1

        # 初始化
        skill_bitmaps: List[int] = []
        for person in people:
            bitmap = 0
            for skill in person:
                skill_index = req_skills.index(skill)
                bitmap += 2 ** skill_index
            skill_bitmaps.append(bitmap)
            assert 0 <= bitmap <= max_bit

        chosen_bitmap = 2 ** len(people) - 1
        chosen_size = len(people)

        # 删除可以被简单替代的人
        to_remove = []
        for i, x in enumerate(skill_bitmaps):
            for j in range(i + 1, len(skill_bitmaps)):
                y = skill_bitmaps[j]
                if x | y == y:
                    # x 能完全被 y 替代
                    to_remove.append(i)
                    break
        # assert get_ones_from_bitmap(chosen_bitmap) == chosen_size
        for index in to_remove:
            # assert get_ones_from_bitmap(chosen_bitmap) == chosen_size
            chosen_bitmap -= 2 ** index
            chosen_size -= 1

        best_chose_bitmap, best_team_size = search_min_team_size(skill_bitmaps, chosen_bitmap, max_bit, 0, chosen_size)

        return get_indexs_from_bitmap(best_chose_bitmap)


# @lc code=end
if __name__ == "__main__":
    f = Solution().smallestSufficientTeam
    import unittest

    t = unittest.TestCase("__init__")
    t.assertEqual(
        f(["java", "nodejs", "reactjs"], [["java"], ["nodejs"], ["nodejs", "reactjs"]]), [0, 2],
    )
    t.assertEqual(
        f(
            ["algorithms", "math", "java", "reactjs", "csharp", "aws"],
            [
                ["algorithms", "math", "java"],
                ["algorithms", "math", "reactjs"],
                ["java", "csharp", "aws"],
                ["reactjs", "csharp"],
                ["csharp", "math"],
                ["aws", "java"],
            ],
        ),
        [1, 2],
    )
    t.assertEqual(
        f(["mmcmnwacnhhdd", "vza", "mrxyc"], [["mmcmnwacnhhdd"], [], [], ["vza", "mrxyc"]]), [0, 3],
    )
    t.assertEqual(
        f(
            ["wieaul", "cxota", "frq", "knngtpip", "junne", "ctniuowumlcrhh"],
            [
                ["wieaul"],
                ["wieaul", "frq", "junne", "ctniuowumlcrhh"],
                ["wieaul"],
                [],
                ["knngtpip"],
                [],
                ["frq", "knngtpip"],
                ["cxota"],
                ["ctniuowumlcrhh"],
                [],
            ],
        ),
        [1, 6, 7],
    )

