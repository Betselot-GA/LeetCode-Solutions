#
# Problem: 153. Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/1956178589/
# Language: python3
# Date: 2026-03-22


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid element is greater than right, min is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # mid element <= right, min is at mid or left side
                right = mid

        return nums[left]
