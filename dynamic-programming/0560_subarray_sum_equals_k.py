"""LeetCode 560: Subarray Sum Equals K.

Problem: https://leetcode.com/problems/subarray-sum-equals-k/

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = 0
        prefix = [0] * n

        # Naive solution below would be O(n^3), because sum(...) is O(n).
        # for i in range(n):
        #     for j in range(i, n):
        #         subarray_sum = sum(nums[i:j + 1])
        #         if subarray_sum == k:
        #             counter += 1

        # Prefix-sum solution: a subarray sum is the difference between
        # two prefix sums. Track how often each earlier prefix has appeared.
        frequency = {0: 1}
        total = 0

        for i in range(n):
            total += nums[i]
            prefix[i] = total
            counter += frequency.get(prefix[i] - k, 0)
            frequency[prefix[i]] = frequency.get(prefix[i], 0) + 1

        return counter
