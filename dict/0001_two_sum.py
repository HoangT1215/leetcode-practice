"""LeetCode 1: Two Sum.

Problem: https://leetcode.com/problems/two-sum/

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        tracker = {}

        for i in range(n):
            tracker[target - nums[i]] = i

        for i in range(n):
            # The indices must differ when target == 2 * nums[i].
            if nums[i] in tracker and tracker[nums[i]] != i:
                return [i, tracker[nums[i]]]
