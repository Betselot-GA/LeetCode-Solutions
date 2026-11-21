#
# Problem: 217. Contains Duplicate
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate/submissions/2200264109/
# Language: python3
# Date: 2026-11-21


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nd = set(nums)
        return len(nd) != len(nums)
