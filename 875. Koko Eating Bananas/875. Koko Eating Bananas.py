#
# Problem: 875. Koko Eating Bananas
# Difficulty: Medium
# Link: https://leetcode.com/problems/koko-eating-bananas/submissions/1955169221/
# Language: python3
# Date: 2026-03-21


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
