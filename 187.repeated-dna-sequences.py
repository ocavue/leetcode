"""
submits:
- date: 2020-11-12
  minutes: 12
  cheating: false

"""
#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (39.22%)
# Likes:    1008
# Dislikes: 317
# Total Accepted:    193.4K
# Total Submissions: 473K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G',
# and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful
# to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
#
#
# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
#
#
# Constraints:
#
#
# 0 <= s.length <= 10^5
# s[i] is 'A', 'C', 'G', or 'T'.
#
#
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        counter = defaultdict(int)
        for i in range(0, len(s)):
            j = i + 10
            sub = s[i:j]
            if len(sub) < 10:
                break
            counter[sub]+=1
        result = []
        for sub, times in counter.items():
            if times>1:
                result.append(sub)
        return result


# @lc code=end

