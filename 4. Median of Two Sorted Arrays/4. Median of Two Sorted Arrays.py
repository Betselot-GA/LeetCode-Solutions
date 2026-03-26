#
# Problem: 4. Median of Two Sorted Arrays
# Difficulty: Hard
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/1959927182/
# Language: python3
# Date: 2026-03-26


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1 + nums2
        res.sort()
        n = len(res)
        m = None

        if n % 2 == 0:
            m = ( res[n//2] + res[(n//2) - 1] ) / 2
        else:
            m =  res[ n // 2]
        return m
