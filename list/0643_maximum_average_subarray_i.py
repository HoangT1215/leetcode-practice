"""LeetCode 643: Maximum Average Subarray I.

Problem: https://leetcode.com/problems/maximum-average-subarray-i/

Time complexity: O(n)
Auxiliary space complexity: O(k) for the initial slice.
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if k == 1: return max(nums)
        n = len(nums)
        best = sum(nums[:k])/k
        current = best
        for i in range(k,n):
            current += (nums[i]-nums[i-k])/k
            best = max(best,current)
        return best
