"""LeetCode 813: Largest Sum of Averages.

Problem: https://leetcode.com/problems/largest-sum-of-averages/

Time complexity: O(k * n^2)
Space complexity: O(n * k)
"""

import numpy as np


class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        n = len(nums)
        if n == 1:
            return nums[0]

        # Define dp[i, j] as best value of i + 1 numbers split into j + 1 groups.
        dp = np.zeros((n, k))
        # Suboptimal memory allocation, can reduce to O(n).
        avg = sum(nums) / n

        for j in range(k):
            left_avg = 0

            for i in range(n):
                left_avg = (left_avg * i + nums[i]) / (i + 1)

                if j == 0:
                    dp[i, j] = left_avg
                elif i >= j:
                    right_avg = 0

                    # Try cuts after t, growing the last group leftward.
                    for t in range(i - 1, j - 2, -1):
                        size = i - t
                        right_avg = (
                            right_avg * (size - 1) + nums[t + 1]
                        ) / size

                        dp[i, j] = max(dp[i, j], dp[t, j - 1] + right_avg)

        return dp[n - 1, k - 1]
