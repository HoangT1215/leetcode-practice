"""LeetCode 78: Subsets.

Problem: https://leetcode.com/problems/subsets/

Time complexity: O(n^2 * 2^n) for this repeated-recursion implementation.
Output space complexity: O(n * 2^n).
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return [[]]

        return self.subsets(nums[:-1]) + [
            subset + [nums[-1]] for subset in self.subsets(nums[:-1])
        ]
