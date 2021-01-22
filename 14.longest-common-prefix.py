"""
submits:
- date: 2021-01-22
  minutes: 6
  cheating: false
"""
#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (35.68%)
# Likes:    3574
# Dislikes: 2094
# Total Accepted:    923.9K
# Total Submissions: 2.6M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
#
# Example 1:
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#
# Constraints:
#
#
# 0 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
#
#
#

List = list
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min([len(s) for s in strs])
        i = 0
        for i in range(min_len):
            if len(set(s[i] for s in strs)) != 1:
                break
        return strs[0][:i]


# @lc code=end

if __name__ == "__main__":
    f = Solution().longestCommonPrefix
    print("1")
    print(f(["flower", "flow", "flight"]))
    print(f(["dog", "racecar", "car"]))
    print("1")
