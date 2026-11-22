#
# Problem: 347. Top K Frequent Elements
# Difficulty: Medium
# Link: https://leetcode.com/problems/top-k-frequent-elements/submissions/2201506653/
# Language: python3
# Date: 2026-11-22


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nd= {}
        for i in range(len(nums)):
            if nums[i] in nd:
                nd[nums[i]] += 1
            else:
                nd[nums[i]] = 1
        sd = sorted(nd, key=nd.get, reverse=True)
        return sd[:k]
