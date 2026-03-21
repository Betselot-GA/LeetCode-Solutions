#
# Problem: 74. Search a 2D Matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-a-2d-matrix/submissions/1955168982/
# Language: python3
# Date: 2026-03-21


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1

        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False
