"""LeetCode 1911: Maximum Alternating Subsequence Sum.

Problem: https://leetcode.com/problems/maximum-alternating-subsequence-sum/

Solution 1 (commented): O(n) time and O(n) space
Solution 2 (active): O(n) time and O(1) space
"""

from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        #--- solution 1: prefix/suffix dp approach
        # n = len(nums)
        # if n <= 2:
        #     return max(nums)
        # left, right = [0] * n, [0] * n

        # left[0] = nums[0]
        # left[1] = max(nums[0], nums[1])

        # right[-1] = nums[-1]
        # right[-2] = max(nums[-1], nums[-2])

        # # Best "prefix - middle" available for a future + value.
        # max_left = left[0] - nums[1]

        # # Best "- middle + suffix" available for an earlier + value.
        # max_right = right[-1] - nums[-2]

        # for i in range(2, n):
        #     left[i] = max(
        #         left[i - 1],          # Skip nums[i].
        #         nums[i],              # Start a new subsequence.
        #         max_left + nums[i],   # Extend with "- middle + nums[i]".
        #     )

        #     # Allow nums[i] to become the minus term for future positions.
        #     max_left = max(max_left, left[i - 1] - nums[i])
        #     j = n - i - 1
        #     right[j] = max(
        #         right[j + 1],
        #         nums[j],
        #         nums[j] + max_right,
        #     )
        #     max_right = max(max_right, right[j + 1] - nums[j])

        # best = max(nums)

        # # Choose nums[i] as a minus term, with disjoint sides.
        # for i in range(1, n - 1):
        #     best = max(
        #         best,
        #         left[i - 1] - nums[i] + right[i + 1],
        #     )
        # return best

        #--- solution 2: two state dp (similar to the stock problem)
        add, subtract = float("-inf"), 0

        for value in nums:
            add, subtract = (
                max(add, subtract + value),
                max(subtract, add - value),
            )

        return add
