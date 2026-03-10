#
# Problem: 11. Container With Most Water
# Difficulty: Medium
# Link: https://leetcode.com/problems/container-with-most-water/submissions/1943926972/
# Language: python3
# Date: 2026-03-10


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # BRUTE FORCE
        # left = 0
        # right = 1
        # area = 0

        # while left < len(heights)-1:
        #     if right < len(heights):
        #         prod = min(heights[left],heights[right]) * (right - left)
        #         area = max(area, prod)
        #         right += 1
        #     else:
        #         left += 1
        #         right = left + 1
        # return area
        
        #LINEAR TIME
        left = 0
        right = len(heights) - 1
        area = 0

        while left < right:
            prod = min(heights[left],heights[right]) * (right - left)
            area = max(area, prod)
            if(heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
        return area
