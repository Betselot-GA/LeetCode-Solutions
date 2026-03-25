#
# Problem: 33. Search in Rotated Sorted Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1958950709/
# Language: python3
# Date: 2026-03-25


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        dict_nums = {}

        for i in range(len(nums)):
            dict_nums[nums[i]] = i

        nums.sort()
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return dict_nums[nums[mid]]
        return -1


        
