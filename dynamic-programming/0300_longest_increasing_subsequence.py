"""LeetCode 300: Longest Increasing Subsequence.

Problem: https://leetcode.com/problems/longest-increasing-subsequence/

Time complexity: O(n^2)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
