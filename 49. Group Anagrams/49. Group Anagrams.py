#
# Problem: 49. Group Anagrams
# Difficulty: Medium
# Link: https://leetcode.com/problems/group-anagrams/submissions/2201497525/
# Language: python3
# Date: 2026-11-22


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key in seen:
                seen[key].extend([strs[i]])
            else:
                seen[key] = [strs[i]]
        return list(seen.values())
        
