#
# Problem: 42. Trapping Rain Water
# Difficulty: Hard
# Link: https://leetcode.com/problems/trapping-rain-water/submissions/1945472962/
# Language: python3
# Date: 2026-03-11


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height)-1
        lMax, rMax = height[l], height[r]
        res = 0

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                res += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]
        return res
        
