"""
submits:
  - date: 2020-08-10
    minutes: 55
    cheating: false
  - date: 2020-09-10
    minutes: 75
    cheating: false

labels: [Trie, backtracking]
comment: |
  这道题有两个难点：
  1. 如何做到一个字母在一个单词中只用到一次。这一点实际上需要用到 backtracking 算法。
     简单来说 backtracking 就是使用 dfs 穷举所有可能，并尽快剪枝。
  2. 如果 words 中所有单词的前半部分都相同，那么这部分计算是可以以某种方式缓存下来的。所以要使用 Trie 的数据结构
  看别人的答案学到了一些性能优化技巧：
  1. 将 result 列表作为参数传到 dfs 里，这样不需要每次递归都重新构造新的列表
  2. trie node 作为答案被获取到了之后，可以把它的 is_word 设置为 false，这样就不会重复地将它添加到 result 中了
"""
# 00:50
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (32.14%)
# Likes:    2696
# Dislikes: 118
# Total Accepted:    222.5K
# Total Submissions: 638.8K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +  '["oath","pea","eat","rain"]'
#
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
#
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
#
#
#
# Example:
#
#
# Input:
# board = [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
#
# Output: ["eat","oath"]
#
#
#
#
# Note:
#
#
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.
#
#
#

# @lc code=start

from typing import List, Optional, Dict
from collections import defaultdict


def find_words_v1(board: List[List[str]], words: List[str]) -> List[str]:
    if not board:
        return []
    if not board[0]:
        return []

    max_i = len(board)
    max_j = len(board[0])
    char_map = defaultdict(list)
    for i in range(max_i):
        for j in range(max_j):
            char_map[board[i][j]].append((i, j))

    def dfs(i: int, j: int, word: str, used: List[List[int]]) -> bool:

        if not word:
            return True

        assert used[i][j] is False
        used[i][j] = True

        for x, y in [
            [i - 1, j],
            [i + 1, j],
            [i, j - 1],
            [i, j + 1],
        ]:
            if 0 <= x < max_i and 0 <= y < max_j and board[x][y] == word[0] and used[x][y] is False:
                if dfs(x, y, word[1:], used):
                    used[i][j] = False
                    return True

        used[i][j] = False
        return False

    found_words = []
    used: List[List[int]] = []
    for i in range(max_i):
        used.append([False] * max_j)
    for origin_word in words:

        # 优先选择第一步迭代数量比较小的那头。这个做法单纯是为了应付 leetcode 里 "aaaaaaaaaaaaaa??" 形式的测试用例。要是换成 "aaaaaaaaaaaaaa??aaaaaaaaaaaaaa" 这样的测试用例的话，这个做法没有任何卵用。
        if len(char_map[origin_word[0]]) <= len(char_map[origin_word[-1]]):
            word = origin_word
        else:
            word = "".join(reversed(origin_word))

        first_char = word[0]
        found = False
        for (i, j) in char_map[first_char]:
            found = dfs(i, j, word[1:], used)
            if found:
                break
            for row in used:
                for cell in row:
                    assert cell is False
        if found:
            found_words.append(origin_word)
    return found_words


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = defaultdict(TrieNode)
        # for i in range(26):
        #     self.children.append(None)
        self.is_word = False

    def add_char(self, child_char: str):
        return self.children[child_char]

        # child_index = ord(child_char) - ord("a")
        # assert 0 <= child_index < 26

        # if not self.children[child_index]:
        #     self.children[child_index] = TrieNode()
        # return self.children[child_index]

    def get_child_node(self, child_char: str) -> "TrieNode":
        result = self.children.get(child_char)
        assert result
        return result

    def get_chars(self) -> List[str]:
        # return [chr(index + ord("a")) for (index, child) in enumerate(self.children) if child]
        return self.children.keys()

    def __repr__(self):
        import json

        map = {
            "is_word": self.is_word,
            "children": {},
        }
        for char in self.get_chars():
            map["children"][char] = json.loads(repr(self.get_child_node(char)))

        return json.dumps(map, indent=4)


def build_trie_root(words: List[str]) -> TrieNode:
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            node = node.add_char(char)
        node.is_word = True
    return root


def find_words_v2(board: List[List[str]], words: List[str]) -> List[str]:
    if not board:
        return []
    if not board[0]:
        return []

    max_i = len(board)
    max_j = len(board[0])
    char_map = defaultdict(list)
    for i in range(max_i):
        for j in range(max_j):
            char_map[board[i][j]].append((i, j))

    def dfs(i: int, j: int, node: TrieNode, prefix: str, used: List[List[bool]], result: List[str]) -> None:
        # assert used[i][j] is False
        used[i][j] = True

        # assert prefix
        # assert prefix[-1] == board[i][j]

        if node.is_word:
            result.append(prefix)
            node.is_word = False  # 注意这里，这样可以减少重复的比较

        for char in node.get_chars():
            for x, y in [
                [i - 1, j],
                [i + 1, j],
                [i, j - 1],
                [i, j + 1],
            ]:
                if 0 <= x < max_i and 0 <= y < max_j and board[x][y] == char and used[x][y] is False:
                    dfs(x, y, node.get_child_node(char), prefix + char, used, result)

        used[i][j] = False

    root = build_trie_root(words)
    # print("root:\n", root)

    used: List[List[bool]] = []
    for i in range(max_i):
        used.append([False] * max_j)

    # words_set = set(words)
    result: List[str] = []
    for first_char in root.get_chars():
        # print("first_char:", first_char)
        for (i, j) in char_map[first_char]:
            dfs(i, j, root.get_child_node(first_char), first_char, used, result)
    return result


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        return find_words_v2(board, words)


# @lc code=end

if __name__ == "__main__":
    f = Solution().findWords
    for board, words, expected in [
        [
            [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
            ["oath", "pea", "eat", "rain"],
            set(["oath", "eat"]),
        ],
        [[["a"]], ["aaa"], set()],
        [
            [
                # fmt:off
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
                # fmt:on
            ],
            ["oath", "pea", "eat", "rain"],
            set(["eat", "oath"]),
        ],
        [
            [
                ["a", "a", "a", "a"],
                ["a", "a", "a", "a"],
                ["a", "a", "a", "a"],
                ["a", "a", "a", "a"],
                ["b", "c", "d", "e"],
                ["f", "g", "h", "i"],
                ["j", "k", "l", "m"],
                ["n", "o", "p", "q"],
                ["r", "s", "t", "u"],
                ["v", "w", "x", "y"],
                ["z", "z", "z", "z"],
            ],
            [
                "aaaaaaaaaaaaaaaa",
                "aaaaaaaaaaaaaaab",
                "aaaaaaaaaaaaaaac",
                "aaaaaaaaaaaaaaad",
                "aaaaaaaaaaaaaaae",
                "aaaaaaaaaaaaaaaf",
                "aaaaaaaaaaaaaaag",
                "aaaaaaaaaaaaaaah",
                "aaaaaaaaaaaaaaai",
                "aaaaaaaaaaaaaaaj",
                "aaaaaaaaaaaaaaak",
                "aaaaaaaaaaaaaaal",
                "aaaaaaaaaaaaaaam",
                "aaaaaaaaaaaaaaan",
                "aaaaaaaaaaaaaaao",
                "aaaaaaaaaaaaaaap",
                "aaaaaaaaaaaaaaaq",
                "aaaaaaaaaaaaaaar",
                "aaaaaaaaaaaaaaas",
                "aaaaaaaaaaaaaaat",
                "aaaaaaaaaaaaaaau",
                "aaaaaaaaaaaaaaav",
                "aaaaaaaaaaaaaaaw",
                "aaaaaaaaaaaaaaax",
                "aaaaaaaaaaaaaaay",
                "aaaaaaaaaaaaaaaz",
                "aaaaaaaaaaaaaaba",
                "aaaaaaaaaaaaaabb",
                "aaaaaaaaaaaaaabc",
                "aaaaaaaaaaaaaabd",
                "aaaaaaaaaaaaaabe",
                "aaaaaaaaaaaaaabf",
                "aaaaaaaaaaaaaabg",
                "aaaaaaaaaaaaaabh",
                "aaaaaaaaaaaaaabi",
                "aaaaaaaaaaaaaabj",
                "aaaaaaaaaaaaaabk",
                "aaaaaaaaaaaaaabl",
                "aaaaaaaaaaaaaabm",
                "aaaaaaaaaaaaaabn",
                "aaaaaaaaaaaaaabo",
                "aaaaaaaaaaaaaabp",
                "aaaaaaaaaaaaaabq",
                "aaaaaaaaaaaaaabr",
                "aaaaaaaaaaaaaabs",
                "aaaaaaaaaaaaaabt",
                "aaaaaaaaaaaaaabu",
                "aaaaaaaaaaaaaabv",
                "aaaaaaaaaaaaaabw",
                "aaaaaaaaaaaaaabx",
                "aaaaaaaaaaaaaaby",
                "aaaaaaaaaaaaaabz",
                "aaaaaaaaaaaaaaca",
                "aaaaaaaaaaaaaacb",
                "aaaaaaaaaaaaaacc",
                "aaaaaaaaaaaaaacd",
                "aaaaaaaaaaaaaace",
                "aaaaaaaaaaaaaacf",
                "aaaaaaaaaaaaaacg",
                "aaaaaaaaaaaaaach",
                "aaaaaaaaaaaaaaci",
                "aaaaaaaaaaaaaacj",
                "aaaaaaaaaaaaaack",
                "aaaaaaaaaaaaaacl",
                "aaaaaaaaaaaaaacm",
                "aaaaaaaaaaaaaacn",
                "aaaaaaaaaaaaaaco",
                "aaaaaaaaaaaaaacp",
                "aaaaaaaaaaaaaacq",
                "aaaaaaaaaaaaaacr",
                "aaaaaaaaaaaaaacs",
                "aaaaaaaaaaaaaact",
                "aaaaaaaaaaaaaacu",
                "aaaaaaaaaaaaaacv",
                "aaaaaaaaaaaaaacw",
                "aaaaaaaaaaaaaacx",
                "aaaaaaaaaaaaaacy",
                "aaaaaaaaaaaaaacz",
                "aaaaaaaaaaaaaada",
                "aaaaaaaaaaaaaadb",
                "aaaaaaaaaaaaaadc",
                "aaaaaaaaaaaaaadd",
                "aaaaaaaaaaaaaade",
                "aaaaaaaaaaaaaadf",
                "aaaaaaaaaaaaaadg",
                "aaaaaaaaaaaaaadh",
                "aaaaaaaaaaaaaadi",
                "aaaaaaaaaaaaaadj",
                "aaaaaaaaaaaaaadk",
                "aaaaaaaaaaaaaadl",
                "aaaaaaaaaaaaaadm",
                "aaaaaaaaaaaaaadn",
                "aaaaaaaaaaaaaado",
                "aaaaaaaaaaaaaadp",
                "aaaaaaaaaaaaaadq",
                "aaaaaaaaaaaaaadr",
                "aaaaaaaaaaaaaads",
                "aaaaaaaaaaaaaadt",
                "aaaaaaaaaaaaaadu",
                "aaaaaaaaaaaaaadv",
                "aaaaaaaaaaaaaadw",
                "aaaaaaaaaaaaaadx",
                "aaaaaaaaaaaaaady",
                "aaaaaaaaaaaaaadz",
                "aaaaaaaaaaaaaaea",
                "aaaaaaaaaaaaaaeb",
                "aaaaaaaaaaaaaaec",
                "aaaaaaaaaaaaaaed",
                "aaaaaaaaaaaaaaee",
                "aaaaaaaaaaaaaaef",
                "aaaaaaaaaaaaaaeg",
                "aaaaaaaaaaaaaaeh",
                "aaaaaaaaaaaaaaei",
                "aaaaaaaaaaaaaaej",
                "aaaaaaaaaaaaaaek",
                "aaaaaaaaaaaaaael",
                "aaaaaaaaaaaaaaem",
                "aaaaaaaaaaaaaaen",
                "aaaaaaaaaaaaaaeo",
                "aaaaaaaaaaaaaaep",
                "aaaaaaaaaaaaaaeq",
                "aaaaaaaaaaaaaaer",
                "aaaaaaaaaaaaaaes",
                "aaaaaaaaaaaaaaet",
                "aaaaaaaaaaaaaaeu",
                "aaaaaaaaaaaaaaev",
                "aaaaaaaaaaaaaaew",
                "aaaaaaaaaaaaaaex",
                "aaaaaaaaaaaaaaey",
                "aaaaaaaaaaaaaaez",
                "aaaaaaaaaaaaaafa",
                "aaaaaaaaaaaaaafb",
                "aaaaaaaaaaaaaafc",
                "aaaaaaaaaaaaaafd",
                "aaaaaaaaaaaaaafe",
                "aaaaaaaaaaaaaaff",
                "aaaaaaaaaaaaaafg",
                "aaaaaaaaaaaaaafh",
                "aaaaaaaaaaaaaafi",
                "aaaaaaaaaaaaaafj",
                "aaaaaaaaaaaaaafk",
                "aaaaaaaaaaaaaafl",
                "aaaaaaaaaaaaaafm",
                "aaaaaaaaaaaaaafn",
                "aaaaaaaaaaaaaafo",
                "aaaaaaaaaaaaaafp",
                "aaaaaaaaaaaaaafq",
                "aaaaaaaaaaaaaafr",
                "aaaaaaaaaaaaaafs",
                "aaaaaaaaaaaaaaft",
                "aaaaaaaaaaaaaafu",
                "aaaaaaaaaaaaaafv",
                "aaaaaaaaaaaaaafw",
                "aaaaaaaaaaaaaafx",
                "aaaaaaaaaaaaaafy",
                "aaaaaaaaaaaaaafz",
                "aaaaaaaaaaaaaaga",
                "aaaaaaaaaaaaaagb",
                "aaaaaaaaaaaaaagc",
                "aaaaaaaaaaaaaagd",
                "aaaaaaaaaaaaaage",
                "aaaaaaaaaaaaaagf",
                "aaaaaaaaaaaaaagg",
                "aaaaaaaaaaaaaagh",
                "aaaaaaaaaaaaaagi",
                "aaaaaaaaaaaaaagj",
                "aaaaaaaaaaaaaagk",
                "aaaaaaaaaaaaaagl",
                "aaaaaaaaaaaaaagm",
                "aaaaaaaaaaaaaagn",
                "aaaaaaaaaaaaaago",
                "aaaaaaaaaaaaaagp",
                "aaaaaaaaaaaaaagq",
                "aaaaaaaaaaaaaagr",
                "aaaaaaaaaaaaaags",
                "aaaaaaaaaaaaaagt",
                "aaaaaaaaaaaaaagu",
                "aaaaaaaaaaaaaagv",
                "aaaaaaaaaaaaaagw",
                "aaaaaaaaaaaaaagx",
                "aaaaaaaaaaaaaagy",
                "aaaaaaaaaaaaaagz",
                "aaaaaaaaaaaaaaha",
                "aaaaaaaaaaaaaahb",
                "aaaaaaaaaaaaaahc",
                "aaaaaaaaaaaaaahd",
                "aaaaaaaaaaaaaahe",
                "aaaaaaaaaaaaaahf",
                "aaaaaaaaaaaaaahg",
                "aaaaaaaaaaaaaahh",
                "aaaaaaaaaaaaaahi",
                "aaaaaaaaaaaaaahj",
                "aaaaaaaaaaaaaahk",
                "aaaaaaaaaaaaaahl",
                "aaaaaaaaaaaaaahm",
                "aaaaaaaaaaaaaahn",
                "aaaaaaaaaaaaaaho",
                "aaaaaaaaaaaaaahp",
                "aaaaaaaaaaaaaahq",
                "aaaaaaaaaaaaaahr",
                "aaaaaaaaaaaaaahs",
                "aaaaaaaaaaaaaaht",
                "aaaaaaaaaaaaaahu",
                "aaaaaaaaaaaaaahv",
                "aaaaaaaaaaaaaahw",
                "aaaaaaaaaaaaaahx",
                "aaaaaaaaaaaaaahy",
                "aaaaaaaaaaaaaahz",
                "aaaaaaaaaaaaaaia",
                "aaaaaaaaaaaaaaib",
                "aaaaaaaaaaaaaaic",
                "aaaaaaaaaaaaaaid",
                "aaaaaaaaaaaaaaie",
                "aaaaaaaaaaaaaaif",
                "aaaaaaaaaaaaaaig",
                "aaaaaaaaaaaaaaih",
                "aaaaaaaaaaaaaaii",
                "aaaaaaaaaaaaaaij",
                "aaaaaaaaaaaaaaik",
                "aaaaaaaaaaaaaail",
                "aaaaaaaaaaaaaaim",
                "aaaaaaaaaaaaaain",
                "aaaaaaaaaaaaaaio",
                "aaaaaaaaaaaaaaip",
                "aaaaaaaaaaaaaaiq",
                "aaaaaaaaaaaaaair",
                "aaaaaaaaaaaaaais",
                "aaaaaaaaaaaaaait",
                "aaaaaaaaaaaaaaiu",
                "aaaaaaaaaaaaaaiv",
                "aaaaaaaaaaaaaaiw",
                "aaaaaaaaaaaaaaix",
                "aaaaaaaaaaaaaaiy",
                "aaaaaaaaaaaaaaiz",
                "aaaaaaaaaaaaaaja",
                "aaaaaaaaaaaaaajb",
                "aaaaaaaaaaaaaajc",
                "aaaaaaaaaaaaaajd",
                "aaaaaaaaaaaaaaje",
                "aaaaaaaaaaaaaajf",
                "aaaaaaaaaaaaaajg",
                "aaaaaaaaaaaaaajh",
                "aaaaaaaaaaaaaaji",
                "aaaaaaaaaaaaaajj",
                "aaaaaaaaaaaaaajk",
                "aaaaaaaaaaaaaajl",
                "aaaaaaaaaaaaaajm",
                "aaaaaaaaaaaaaajn",
                "aaaaaaaaaaaaaajo",
                "aaaaaaaaaaaaaajp",
                "aaaaaaaaaaaaaajq",
                "aaaaaaaaaaaaaajr",
                "aaaaaaaaaaaaaajs",
                "aaaaaaaaaaaaaajt",
                "aaaaaaaaaaaaaaju",
                "aaaaaaaaaaaaaajv",
                "aaaaaaaaaaaaaajw",
                "aaaaaaaaaaaaaajx",
                "aaaaaaaaaaaaaajy",
                "aaaaaaaaaaaaaajz",
                "aaaaaaaaaaaaaaka",
                "aaaaaaaaaaaaaakb",
                "aaaaaaaaaaaaaakc",
                "aaaaaaaaaaaaaakd",
                "aaaaaaaaaaaaaake",
                "aaaaaaaaaaaaaakf",
                "aaaaaaaaaaaaaakg",
                "aaaaaaaaaaaaaakh",
                "aaaaaaaaaaaaaaki",
                "aaaaaaaaaaaaaakj",
                "aaaaaaaaaaaaaakk",
                "aaaaaaaaaaaaaakl",
                "aaaaaaaaaaaaaakm",
                "aaaaaaaaaaaaaakn",
                "aaaaaaaaaaaaaako",
                "aaaaaaaaaaaaaakp",
                "aaaaaaaaaaaaaakq",
                "aaaaaaaaaaaaaakr",
                "aaaaaaaaaaaaaaks",
                "aaaaaaaaaaaaaakt",
                "aaaaaaaaaaaaaaku",
                "aaaaaaaaaaaaaakv",
                "aaaaaaaaaaaaaakw",
                "aaaaaaaaaaaaaakx",
                "aaaaaaaaaaaaaaky",
                "aaaaaaaaaaaaaakz",
                "aaaaaaaaaaaaaala",
                "aaaaaaaaaaaaaalb",
                "aaaaaaaaaaaaaalc",
                "aaaaaaaaaaaaaald",
                "aaaaaaaaaaaaaale",
                "aaaaaaaaaaaaaalf",
                "aaaaaaaaaaaaaalg",
                "aaaaaaaaaaaaaalh",
                "aaaaaaaaaaaaaali",
                "aaaaaaaaaaaaaalj",
                "aaaaaaaaaaaaaalk",
                "aaaaaaaaaaaaaall",
                "aaaaaaaaaaaaaalm",
                "aaaaaaaaaaaaaaln",
                "aaaaaaaaaaaaaalo",
                "aaaaaaaaaaaaaalp",
                "aaaaaaaaaaaaaalq",
                "aaaaaaaaaaaaaalr",
                "aaaaaaaaaaaaaals",
                "aaaaaaaaaaaaaalt",
                "aaaaaaaaaaaaaalu",
                "aaaaaaaaaaaaaalv",
                "aaaaaaaaaaaaaalw",
                "aaaaaaaaaaaaaalx",
                "aaaaaaaaaaaaaaly",
                "aaaaaaaaaaaaaalz",
                "aaaaaaaaaaaaaama",
                "aaaaaaaaaaaaaamb",
                "aaaaaaaaaaaaaamc",
                "aaaaaaaaaaaaaamd",
                "aaaaaaaaaaaaaame",
                "aaaaaaaaaaaaaamf",
                "aaaaaaaaaaaaaamg",
                "aaaaaaaaaaaaaamh",
                "aaaaaaaaaaaaaami",
                "aaaaaaaaaaaaaamj",
                "aaaaaaaaaaaaaamk",
                "aaaaaaaaaaaaaaml",
                "aaaaaaaaaaaaaamm",
                "aaaaaaaaaaaaaamn",
                "aaaaaaaaaaaaaamo",
                "aaaaaaaaaaaaaamp",
                "aaaaaaaaaaaaaamq",
                "aaaaaaaaaaaaaamr",
                "aaaaaaaaaaaaaams",
                "aaaaaaaaaaaaaamt",
                "aaaaaaaaaaaaaamu",
                "aaaaaaaaaaaaaamv",
                "aaaaaaaaaaaaaamw",
                "aaaaaaaaaaaaaamx",
                "aaaaaaaaaaaaaamy",
                "aaaaaaaaaaaaaamz",
                "aaaaaaaaaaaaaana",
                "aaaaaaaaaaaaaanb",
                "aaaaaaaaaaaaaanc",
                "aaaaaaaaaaaaaand",
                "aaaaaaaaaaaaaane",
                "aaaaaaaaaaaaaanf",
                "aaaaaaaaaaaaaang",
                "aaaaaaaaaaaaaanh",
                "aaaaaaaaaaaaaani",
                "aaaaaaaaaaaaaanj",
                "aaaaaaaaaaaaaank",
                "aaaaaaaaaaaaaanl",
                "aaaaaaaaaaaaaanm",
                "aaaaaaaaaaaaaann",
                "aaaaaaaaaaaaaano",
                "aaaaaaaaaaaaaanp",
                "aaaaaaaaaaaaaanq",
                "aaaaaaaaaaaaaanr",
                "aaaaaaaaaaaaaans",
                "aaaaaaaaaaaaaant",
                "aaaaaaaaaaaaaanu",
                "aaaaaaaaaaaaaanv",
                "aaaaaaaaaaaaaanw",
                "aaaaaaaaaaaaaanx",
                "aaaaaaaaaaaaaany",
                "aaaaaaaaaaaaaanz",
                "aaaaaaaaaaaaaaoa",
                "aaaaaaaaaaaaaaob",
                "aaaaaaaaaaaaaaoc",
                "aaaaaaaaaaaaaaod",
                "aaaaaaaaaaaaaaoe",
                "aaaaaaaaaaaaaaof",
                "aaaaaaaaaaaaaaog",
                "aaaaaaaaaaaaaaoh",
                "aaaaaaaaaaaaaaoi",
                "aaaaaaaaaaaaaaoj",
                "aaaaaaaaaaaaaaok",
                "aaaaaaaaaaaaaaol",
                "aaaaaaaaaaaaaaom",
                "aaaaaaaaaaaaaaon",
                "aaaaaaaaaaaaaaoo",
                "aaaaaaaaaaaaaaop",
                "aaaaaaaaaaaaaaoq",
                "aaaaaaaaaaaaaaor",
                "aaaaaaaaaaaaaaos",
                "aaaaaaaaaaaaaaot",
                "aaaaaaaaaaaaaaou",
                "aaaaaaaaaaaaaaov",
                "aaaaaaaaaaaaaaow",
                "aaaaaaaaaaaaaaox",
                "aaaaaaaaaaaaaaoy",
                "aaaaaaaaaaaaaaoz",
                "aaaaaaaaaaaaaapa",
                "aaaaaaaaaaaaaapb",
                "aaaaaaaaaaaaaapc",
                "aaaaaaaaaaaaaapd",
                "aaaaaaaaaaaaaape",
                "aaaaaaaaaaaaaapf",
                "aaaaaaaaaaaaaapg",
                "aaaaaaaaaaaaaaph",
                "aaaaaaaaaaaaaapi",
                "aaaaaaaaaaaaaapj",
                "aaaaaaaaaaaaaapk",
                "aaaaaaaaaaaaaapl",
                "aaaaaaaaaaaaaapm",
                "aaaaaaaaaaaaaapn",
                "aaaaaaaaaaaaaapo",
                "aaaaaaaaaaaaaapp",
                "aaaaaaaaaaaaaapq",
                "aaaaaaaaaaaaaapr",
                "aaaaaaaaaaaaaaps",
                "aaaaaaaaaaaaaapt",
                "aaaaaaaaaaaaaapu",
                "aaaaaaaaaaaaaapv",
                "aaaaaaaaaaaaaapw",
                "aaaaaaaaaaaaaapx",
                "aaaaaaaaaaaaaapy",
                "aaaaaaaaaaaaaapz",
                "aaaaaaaaaaaaaaqa",
                "aaaaaaaaaaaaaaqb",
                "aaaaaaaaaaaaaaqc",
                "aaaaaaaaaaaaaaqd",
                "aaaaaaaaaaaaaaqe",
                "aaaaaaaaaaaaaaqf",
                "aaaaaaaaaaaaaaqg",
                "aaaaaaaaaaaaaaqh",
                "aaaaaaaaaaaaaaqi",
                "aaaaaaaaaaaaaaqj",
                "aaaaaaaaaaaaaaqk",
                "aaaaaaaaaaaaaaql",
                "aaaaaaaaaaaaaaqm",
                "aaaaaaaaaaaaaaqn",
                "aaaaaaaaaaaaaaqo",
                "aaaaaaaaaaaaaaqp",
                "aaaaaaaaaaaaaaqq",
                "aaaaaaaaaaaaaaqr",
                "aaaaaaaaaaaaaaqs",
                "aaaaaaaaaaaaaaqt",
                "aaaaaaaaaaaaaaqu",
                "aaaaaaaaaaaaaaqv",
                "aaaaaaaaaaaaaaqw",
                "aaaaaaaaaaaaaaqx",
                "aaaaaaaaaaaaaaqy",
                "aaaaaaaaaaaaaaqz",
                "aaaaaaaaaaaaaara",
                "aaaaaaaaaaaaaarb",
                "aaaaaaaaaaaaaarc",
                "aaaaaaaaaaaaaard",
                "aaaaaaaaaaaaaare",
                "aaaaaaaaaaaaaarf",
                "aaaaaaaaaaaaaarg",
                "aaaaaaaaaaaaaarh",
                "aaaaaaaaaaaaaari",
                "aaaaaaaaaaaaaarj",
                "aaaaaaaaaaaaaark",
                "aaaaaaaaaaaaaarl",
                "aaaaaaaaaaaaaarm",
                "aaaaaaaaaaaaaarn",
                "aaaaaaaaaaaaaaro",
                "aaaaaaaaaaaaaarp",
                "aaaaaaaaaaaaaarq",
                "aaaaaaaaaaaaaarr",
                "aaaaaaaaaaaaaars",
                "aaaaaaaaaaaaaart",
                "aaaaaaaaaaaaaaru",
                "aaaaaaaaaaaaaarv",
                "aaaaaaaaaaaaaarw",
                "aaaaaaaaaaaaaarx",
                "aaaaaaaaaaaaaary",
                "aaaaaaaaaaaaaarz",
                "aaaaaaaaaaaaaasa",
                "aaaaaaaaaaaaaasb",
                "aaaaaaaaaaaaaasc",
                "aaaaaaaaaaaaaasd",
                "aaaaaaaaaaaaaase",
                "aaaaaaaaaaaaaasf",
                "aaaaaaaaaaaaaasg",
                "aaaaaaaaaaaaaash",
                "aaaaaaaaaaaaaasi",
                "aaaaaaaaaaaaaasj",
                "aaaaaaaaaaaaaask",
                "aaaaaaaaaaaaaasl",
                "aaaaaaaaaaaaaasm",
                "aaaaaaaaaaaaaasn",
                "aaaaaaaaaaaaaaso",
                "aaaaaaaaaaaaaasp",
                "aaaaaaaaaaaaaasq",
                "aaaaaaaaaaaaaasr",
                "aaaaaaaaaaaaaass",
                "aaaaaaaaaaaaaast",
                "aaaaaaaaaaaaaasu",
                "aaaaaaaaaaaaaasv",
                "aaaaaaaaaaaaaasw",
                "aaaaaaaaaaaaaasx",
                "aaaaaaaaaaaaaasy",
                "aaaaaaaaaaaaaasz",
                "aaaaaaaaaaaaaata",
                "aaaaaaaaaaaaaatb",
                "aaaaaaaaaaaaaatc",
                "aaaaaaaaaaaaaatd",
                "aaaaaaaaaaaaaate",
                "aaaaaaaaaaaaaatf",
                "aaaaaaaaaaaaaatg",
                "aaaaaaaaaaaaaath",
                "aaaaaaaaaaaaaati",
                "aaaaaaaaaaaaaatj",
                "aaaaaaaaaaaaaatk",
                "aaaaaaaaaaaaaatl",
                "aaaaaaaaaaaaaatm",
                "aaaaaaaaaaaaaatn",
                "aaaaaaaaaaaaaato",
                "aaaaaaaaaaaaaatp",
                "aaaaaaaaaaaaaatq",
                "aaaaaaaaaaaaaatr",
                "aaaaaaaaaaaaaats",
                "aaaaaaaaaaaaaatt",
                "aaaaaaaaaaaaaatu",
                "aaaaaaaaaaaaaatv",
                "aaaaaaaaaaaaaatw",
                "aaaaaaaaaaaaaatx",
                "aaaaaaaaaaaaaaty",
                "aaaaaaaaaaaaaatz",
                "aaaaaaaaaaaaaaua",
                "aaaaaaaaaaaaaaub",
                "aaaaaaaaaaaaaauc",
                "aaaaaaaaaaaaaaud",
                "aaaaaaaaaaaaaaue",
                "aaaaaaaaaaaaaauf",
                "aaaaaaaaaaaaaaug",
                "aaaaaaaaaaaaaauh",
                "aaaaaaaaaaaaaaui",
                "aaaaaaaaaaaaaauj",
                "aaaaaaaaaaaaaauk",
                "aaaaaaaaaaaaaaul",
                "aaaaaaaaaaaaaaum",
                "aaaaaaaaaaaaaaun",
                "aaaaaaaaaaaaaauo",
                "aaaaaaaaaaaaaaup",
                "aaaaaaaaaaaaaauq",
                "aaaaaaaaaaaaaaur",
                "aaaaaaaaaaaaaaus",
                "aaaaaaaaaaaaaaut",
                "aaaaaaaaaaaaaauu",
                "aaaaaaaaaaaaaauv",
                "aaaaaaaaaaaaaauw",
                "aaaaaaaaaaaaaaux",
                "aaaaaaaaaaaaaauy",
                "aaaaaaaaaaaaaauz",
                "aaaaaaaaaaaaaava",
                "aaaaaaaaaaaaaavb",
                "aaaaaaaaaaaaaavc",
                "aaaaaaaaaaaaaavd",
                "aaaaaaaaaaaaaave",
                "aaaaaaaaaaaaaavf",
                "aaaaaaaaaaaaaavg",
                "aaaaaaaaaaaaaavh",
                "aaaaaaaaaaaaaavi",
                "aaaaaaaaaaaaaavj",
                "aaaaaaaaaaaaaavk",
                "aaaaaaaaaaaaaavl",
                "aaaaaaaaaaaaaavm",
                "aaaaaaaaaaaaaavn",
                "aaaaaaaaaaaaaavo",
                "aaaaaaaaaaaaaavp",
                "aaaaaaaaaaaaaavq",
                "aaaaaaaaaaaaaavr",
                "aaaaaaaaaaaaaavs",
                "aaaaaaaaaaaaaavt",
                "aaaaaaaaaaaaaavu",
                "aaaaaaaaaaaaaavv",
                "aaaaaaaaaaaaaavw",
                "aaaaaaaaaaaaaavx",
                "aaaaaaaaaaaaaavy",
                "aaaaaaaaaaaaaavz",
                "aaaaaaaaaaaaaawa",
                "aaaaaaaaaaaaaawb",
                "aaaaaaaaaaaaaawc",
                "aaaaaaaaaaaaaawd",
                "aaaaaaaaaaaaaawe",
                "aaaaaaaaaaaaaawf",
                "aaaaaaaaaaaaaawg",
                "aaaaaaaaaaaaaawh",
                "aaaaaaaaaaaaaawi",
                "aaaaaaaaaaaaaawj",
                "aaaaaaaaaaaaaawk",
                "aaaaaaaaaaaaaawl",
                "aaaaaaaaaaaaaawm",
                "aaaaaaaaaaaaaawn",
                "aaaaaaaaaaaaaawo",
                "aaaaaaaaaaaaaawp",
                "aaaaaaaaaaaaaawq",
                "aaaaaaaaaaaaaawr",
                "aaaaaaaaaaaaaaws",
                "aaaaaaaaaaaaaawt",
                "aaaaaaaaaaaaaawu",
                "aaaaaaaaaaaaaawv",
                "aaaaaaaaaaaaaaww",
                "aaaaaaaaaaaaaawx",
                "aaaaaaaaaaaaaawy",
                "aaaaaaaaaaaaaawz",
                "aaaaaaaaaaaaaaxa",
                "aaaaaaaaaaaaaaxb",
                "aaaaaaaaaaaaaaxc",
                "aaaaaaaaaaaaaaxd",
                "aaaaaaaaaaaaaaxe",
                "aaaaaaaaaaaaaaxf",
                "aaaaaaaaaaaaaaxg",
                "aaaaaaaaaaaaaaxh",
                "aaaaaaaaaaaaaaxi",
                "aaaaaaaaaaaaaaxj",
                "aaaaaaaaaaaaaaxk",
                "aaaaaaaaaaaaaaxl",
                "aaaaaaaaaaaaaaxm",
                "aaaaaaaaaaaaaaxn",
                "aaaaaaaaaaaaaaxo",
                "aaaaaaaaaaaaaaxp",
                "aaaaaaaaaaaaaaxq",
                "aaaaaaaaaaaaaaxr",
                "aaaaaaaaaaaaaaxs",
                "aaaaaaaaaaaaaaxt",
                "aaaaaaaaaaaaaaxu",
                "aaaaaaaaaaaaaaxv",
                "aaaaaaaaaaaaaaxw",
                "aaaaaaaaaaaaaaxx",
                "aaaaaaaaaaaaaaxy",
                "aaaaaaaaaaaaaaxz",
                "aaaaaaaaaaaaaaya",
                "aaaaaaaaaaaaaayb",
                "aaaaaaaaaaaaaayc",
                "aaaaaaaaaaaaaayd",
                "aaaaaaaaaaaaaaye",
                "aaaaaaaaaaaaaayf",
                "aaaaaaaaaaaaaayg",
                "aaaaaaaaaaaaaayh",
                "aaaaaaaaaaaaaayi",
                "aaaaaaaaaaaaaayj",
                "aaaaaaaaaaaaaayk",
                "aaaaaaaaaaaaaayl",
                "aaaaaaaaaaaaaaym",
                "aaaaaaaaaaaaaayn",
                "aaaaaaaaaaaaaayo",
                "aaaaaaaaaaaaaayp",
                "aaaaaaaaaaaaaayq",
                "aaaaaaaaaaaaaayr",
                "aaaaaaaaaaaaaays",
                "aaaaaaaaaaaaaayt",
                "aaaaaaaaaaaaaayu",
                "aaaaaaaaaaaaaayv",
                "aaaaaaaaaaaaaayw",
                "aaaaaaaaaaaaaayx",
                "aaaaaaaaaaaaaayy",
                "aaaaaaaaaaaaaayz",
                "aaaaaaaaaaaaaaza",
                "aaaaaaaaaaaaaazb",
                "aaaaaaaaaaaaaazc",
                "aaaaaaaaaaaaaazd",
                "aaaaaaaaaaaaaaze",
                "aaaaaaaaaaaaaazf",
                "aaaaaaaaaaaaaazg",
                "aaaaaaaaaaaaaazh",
                "aaaaaaaaaaaaaazi",
                "aaaaaaaaaaaaaazj",
                "aaaaaaaaaaaaaazk",
                "aaaaaaaaaaaaaazl",
                "aaaaaaaaaaaaaazm",
                "aaaaaaaaaaaaaazn",
                "aaaaaaaaaaaaaazo",
                "aaaaaaaaaaaaaazp",
                "aaaaaaaaaaaaaazq",
                "aaaaaaaaaaaaaazr",
                "aaaaaaaaaaaaaazs",
                "aaaaaaaaaaaaaazt",
                "aaaaaaaaaaaaaazu",
                "aaaaaaaaaaaaaazv",
                "aaaaaaaaaaaaaazw",
                "aaaaaaaaaaaaaazx",
                "aaaaaaaaaaaaaazy",
                "aaaaaaaaaaaaaazz",
            ],
            {
                "aaaaaaaaaaaaaaad",
                "aaaaaaaaaaaaaaei",
                "aaaaaaaaaaaaaaae",
                "aaaaaaaaaaaaaaed",
                "aaaaaaaaaaaaaabc",
                "aaaaaaaaaaaaaaaa",
                "aaaaaaaaaaaaaadh",
                "aaaaaaaaaaaaaacd",
                "aaaaaaaaaaaaaaac",
                "aaaaaaaaaaaaaabf",
                "aaaaaaaaaaaaaade",
                "aaaaaaaaaaaaaacg",
                "aaaaaaaaaaaaaadc",
                "aaaaaaaaaaaaaacb",
                "aaaaaaaaaaaaaaab",
            },
        ],
    ]:
        received = set(f(board, words))
        assert expected == received, f"{expected} != {received}"
