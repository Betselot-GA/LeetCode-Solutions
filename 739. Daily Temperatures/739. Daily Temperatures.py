#
# Problem: 739. Daily Temperatures
# Difficulty: Medium
# Link: https://leetcode.com/problems/daily-temperatures/
# Language: python3
# Date: 2026-03-17


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [temp, index]
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        
        return res
        
