"""
submits:
  - date: 2020-03-11
    cheating: false
"""

#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (33.81%)
# Likes:    980
# Dislikes: 442
# Total Accepted:    172.1K
# Total Submissions: 508.8K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
#
# Example:
#
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
#
#
#

from typing import Union, List

# @lc code=start
class Solution:
    def is_vaild_ip_part(self, part: str) -> bool:
        if part == "0":
            return True
        if part.startswith("0"):
            return False

        if len(part) == 3:
            return part <= "255"
        elif 1 <= len(part) <= 2:
            return True
        return False

    def get_ip_parts_comb(self, s: str, num: str) -> List[List[str]]:

        if len(s) > 3 * num:
            return []
        if len(s) == 0:
            return []
        if num == 1:
            if self.is_vaild_ip_part(s):
                return [[s]]
            else:
                return []

        results = []

        # if the next part is a one-digig number
        part, reset_str = s[:1], s[1:]
        if self.is_vaild_ip_part(part):
            results += [
                [part] + reset_parts
                for reset_parts in self.get_ip_parts_comb(reset_str, num - 1)
            ]

        # if the next part is a two-digigs number
        part, reset_str = s[:2], s[2:]
        if self.is_vaild_ip_part(part):
            results += [
                [part] + reset_parts
                for reset_parts in self.get_ip_parts_comb(reset_str, num - 1)
            ]

        # if the next part is a three-digigs number
        part, reset_str = s[:3], s[3:]
        if self.is_vaild_ip_part(part):
            results += [
                [part] + reset_parts
                for reset_parts in self.get_ip_parts_comb(reset_str, num - 1)
            ]

        return results

    def restoreIpAddresses(self, s: str) -> List[str]:
        return [".".join(ip_parts) for ip_parts in self.get_ip_parts_comb(s, 4)]


# @lc code=end

if __name__ == "__main__":
    for ip_str in [
        "25525511135",
        "0000",
        "11111111",
        "255155255255",
        "25515525524",
        "010010",
    ]:
        print(Solution().restoreIpAddresses(ip_str))

