#
# Problem: 424. Longest Repeating Character Replacement
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/submissions/1963295653/
# Language: python3
# Date: 2026-03-29


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
