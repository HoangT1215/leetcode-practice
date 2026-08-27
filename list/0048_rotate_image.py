"""LeetCode 48: Rotate Image.

Problem: https://leetcode.com/problems/rotate-image/

Time complexity: O(n^2)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Do not return anything; modify matrix in-place instead."""
        n = len(matrix)

        # Composition of reflection over the main diagonal and horizontal flip.
        for i in range(n):
            for j in range(i + 1, n):
                # Main-diagonal reflection.
                matrix[i][j], matrix[j][i] = (
                    matrix[j][i],
                    matrix[i][j],
                )

        # Horizontal flip.
        for row in matrix:
            row.reverse()
