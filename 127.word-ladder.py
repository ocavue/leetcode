"""
submits:
  - date: 2020-04-11
    cheating: false
labels: [bfs]
"""

#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (27.71%)
# Likes:    2618
# Dislikes: 1039
# Total Accepted:    379.8K
# Total Submissions: 1.4M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
#
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
# Note:
#
#
# Return 0 if there is no such transformation sequence.
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
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
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
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#
#
#
#
#
#

# @lc code=start
from collections import namedtuple, defaultdict
from typing import List, Dict, Union
from queue import Queue

Node = namedtuple("Node", ["word", "distance", "parent", "linked_nodes"])


class Graph:
    def __init__(self):
        self.words: List[str] = []
        self.edges: List[List[int, int]] = []
        self.wildcard_map: Dict[str, List[int]] = defaultdict(list)

    def add_word(self, new_word: str) -> int:
        new_index = len(self.words)
        self.edges.append([])
        self.words.append(new_word)
        assert len(self.edges) == len(self.words) == new_index + 1

        for index in range(len(new_word)):
            wildcard = "".join(
                [c if i != index else "*" for i, c in enumerate(new_word)]
            )
            for word_index in self.wildcard_map[wildcard]:
                self.add_edge(word_index, new_index)
            self.wildcard_map[wildcard].append(new_index)

        return new_index
        # for index, word in enumerate(self.words):
        #     if self.is_adjacent(word, new_word):
        #         self.add_edge(new_index, index)
        # return new_index

    def add_edge(self, v: int, w: int):
        self.edges[w].append(v)
        self.edges[v].append(w)

    @staticmethod
    def is_adjacent(word1, word2):
        diff = 0
        assert len(word1) == len(word2), "{} and {} have not-equal length".format(
            repr(word1), repr(word2)
        )
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
            if diff >= 2:
                break
        return diff == 1


class BreadthFirstPath:
    def __init__(self, g: Graph, start: int):
        self.marked = [False] * len(g.words)
        self.edge_to = [None] * len(g.words)
        self.start = start
        self.g = g
        self.__bfs()

    def __bfs(self):
        q = Queue()
        q.put(self.start)
        self.marked[self.start] = True
        while not q.empty():
            v = q.get()
            for w in self.g.edges[v]:
                if not self.marked[w]:
                    self.marked[w] = True
                    self.edge_to[w] = v
                    q.put(w)

    def path_to(self, v: int) -> Union[List[int], None]:
        if self.edge_to[v] is None:
            return None
        else:
            current = v
            path = []
            # print("self.edge_to:", self.edge_to)
            while current is not None:
                path.append(current)
                current = self.edge_to[current]
            return list(reversed(path))


def ladder_length(begin_word: str, end_word: str, words: List[str]) -> int:
    g = Graph()
    end_word_index = None
    g.add_word(begin_word)
    for word in words:
        if word == end_word:
            end_word_index = g.add_word(word)
        else:
            g.add_word(word)

    if not end_word_index:
        return 0

    bfp = BreadthFirstPath(g, 0)
    path = bfp.path_to(end_word_index)
    # print(path)
    if path is None:
        return 0
    else:
        return len(path)


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, words: List[str]) -> int:
        return ladder_length(begin_word, end_word, words)


# @lc code=ends
if __name__ == "__main__":
    import unittest

    t = unittest.TestCase("__init__")

    t.assertEqual(
        ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5
    )
    t.assertEqual(ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"],), 0)
