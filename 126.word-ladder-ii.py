"""
submits:
  - date: 2020-07-29
    cheating: false
    minutes: 68
labels: [bfs]
comment: |
  这道题使用 Breadth-first search（广度优先搜索）找到最短路径。有意思的地方是 willcard 的设计。
"""

#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (20.57%)
# Likes:    1793
# Dislikes: 248
# Total Accepted:    186.5K
# Total Submissions: 846.7K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
#
#
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
# Note:
#
#
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: []
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#
#
#


# @lc code=start

from typing import List, Dict
from collections import defaultdict
from queue import Queue


def build_wildcards(word: str) -> List[str]:
    """
    >>> build_wildcards("foo")
    ['*oo', 'f*o', 'fo*']
    >>> build_wildcards('f')
    ['*']
    >>> build_wildcards('')
    []
    """
    results = []
    for i in range(len(word)):
        results.append(word[:i] + "*" + word[i + 1 :])
    return results


class Graph:
    def __init__(self):
        self.edges: List[List[int]] = []
        self.words: List[str] = []
        self.edges: List[List[int]] = []  # index 是起始点的 word_index，value 是终点的 word_index 列表
        self.wildcards: Dict[str, List[int]] = defaultdict(list)

    def add_word(self, word: str):
        new_word_index = len(self.words)
        self.words.append(word)
        self.edges.append([])

        assert len(self.words) == len(self.edges) == new_word_index + 1

        for wildcard in build_wildcards(word):

            for other_word_index in self.wildcards[wildcard]:
                self.edges[other_word_index].append(new_word_index)
                self.edges[new_word_index].append(other_word_index)

            self.wildcards[wildcard].append(new_word_index)

    def path_to(self, index: int) -> List[int]:
        assert 0 <= index < len(self.words)
        return self.edges[index]


class BFS:
    def __init__(self, words: List[str]):

        self.g = Graph()
        self.len = len(words)
        for word in words:
            self.g.add_word(word)

        self.g.wildcards = None  # 手动 GC

    def get_paths_to(self, a: int, b: int) -> List[List[int]]:
        g = self.g
        q = Queue()

        # 到达某一个点的最短路径。 # key 是 to_index, value 是 from_index 列表。
        paths: List[List[int]] = []
        for i in range(self.len):
            paths.append([])

        # 到达某一个点所需要的最短距离。key 是 word_index, value 是距离
        distances: List[int] = [-1] * self.len

        q.put(a)
        distances[a] = 0

        while not q.empty():
            from_index = q.get()
            assert distances[from_index] != -1

            for to_index in g.path_to(from_index):
                new_distance = distances[from_index] + 1
                existed_distance = distances[to_index]
                if existed_distance == -1:
                    q.put(to_index)
                    distances[to_index] = new_distance
                    paths[to_index].append(from_index)
                elif existed_distance == new_distance:
                    paths[to_index].append(from_index)
                elif existed_distance < new_distance:
                    pass
                elif existed_distance > new_distance:
                    raise Exception("NO WAY!")

        if distances[b] == -1:
            return []

        def _get_paths_to(end_index: int) -> List[List[int]]:
            assert distances[end_index] != -1

            if end_index == a:
                return [[a]]

            result: List[List[int]] = []
            for prev_index in paths[end_index]:
                prev_paths: List[List[int]] = _get_paths_to(prev_index)
                for prev_path in prev_paths:
                    assert len(prev_path) == distances[end_index]

                    prev_path.append(end_index)
                    curr_path = prev_path
                    assert len(prev_path) == distances[end_index] + 1
                    result.append(curr_path)
            return result

        return _get_paths_to(b)


class Solution:
    def findLadders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        if end_word not in word_list:
            return []

        word_list = [begin_word, *word_list]

        begin_index = 0
        end_index = word_list.index(end_word)

        bfs = BFS(word_list)
        index_paths = bfs.get_paths_to(begin_index, end_index)
        word_paths: List[List[str]] = []

        for index_path in index_paths:
            word_path = []
            for index in index_path:
                word_path.append(word_list[index])
            word_paths.append(word_path)

        return word_paths


# @lc code=end
if __name__ == "__main__":
    import doctest
    import unittest

    doctest.testmod()

    f = Solution().findLadders

    t = unittest.TestCase("__init__")

    # fmt: off
    t.assertEqual(
        f(
            "hit",
            "hot",
            ["hot"],
        ),
        [
            ["hit", "hot"],
        ],
    )

    t.assertEqual(
        f(
            "hit",
            "dot",
            ["hot", "dot"],
        ),
        [
            ["hit", "hot", "dot"],
        ],
    )

    t.assertEqual(
        f(
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log", "cog"],
        ),
        [
            ["hit", "hot", "dot", "dog", "cog"],
            ["hit", "hot", "lot", "log", "cog"],
        ],
    )

    t.assertEqual(
        f(
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log"],
        ),
        [],
    )
