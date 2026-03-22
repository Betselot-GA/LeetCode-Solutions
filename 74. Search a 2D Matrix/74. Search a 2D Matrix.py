#
# Problem: 74. Search a 2D Matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-a-2d-matrix/submissions/1956136155/
# Language: python3
# Date: 2026-03-22


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # left, right = 0, len(matrix)-1
        

        # while left <= right:
        #     mid = (left + right ) // 2
        #     left_m, right_m = 0, len(matrix[0])-1
        #     if matrix[mid][0] <= target <= matrix[mid][-1]:
        #         while left_m <= right_m:
        #             mid_m = ( left_m + right_m ) // 2
        #             if matrix[mid][mid_m] > target:
        #                 right_m = mid_m - 1
        #             elif matrix[mid][mid_m] < target:
        #                 left_m = mid_m + 1
        #             else:
        #                 return True
        #         return False
        #     elif matrix[mid][-1] < target:
        #         left = mid + 1
            
        #     else:
        #         right = mid - 1

        

        # return False
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right ) // 2
            row = mid // cols
            col = mid % cols

            if target > matrix[row][col]:
                left = mid + 1
            elif target < matrix[row][col]:
                right = mid - 1
            else:
                return True
        return False

        
