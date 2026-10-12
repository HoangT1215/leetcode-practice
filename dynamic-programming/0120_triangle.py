"""LeetCode 120: Triangle.

Problem: https://leetcode.com/problems/triangle/

Time complexity: O(n^2), where n is the number of rows.
Space complexity: O(n)
"""

import numpy as np


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]

        dp = np.zeros(n)
        for k in range(n - 1, -1, -1):
            row = triangle[k]
            r = len(row)
            for j in range(r):
                if k == n - 1:
                    dp[j] = row[j]
                else:
                    dp[j] = row[j] + min(dp[j], dp[j + 1])

        return int(dp[0])
