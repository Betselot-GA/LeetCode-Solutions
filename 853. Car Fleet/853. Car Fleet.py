#
# Problem: 853. Car Fleet
# Difficulty: Medium
# Link: https://leetcode.com/problems/car-fleet/submissions/1952222495/
# Language: python3
# Date: 2026-03-18


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack  = []

        for p, s in pair:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
