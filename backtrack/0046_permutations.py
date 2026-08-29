"""LeetCode 46: Permutations.

Problem: https://leetcode.com/problems/permutations/

Time complexity: O(n * n!)
Output space complexity: O(n * n!)
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        if n == 0:
            return []
        elif n == 1:
            # A one-element list has exactly one permutation.
            return [nums]
        else:
            output = []

            # Choose each number as the first element. Recursively generate
            # every permutation of the remaining numbers, then prepend the
            # chosen number to each result.
            for i in range(n):
                remaining = nums[:i] + nums[i + 1:]
                previous_output = self.permute(remaining)

                for element in previous_output:
                    output.append([nums[i]] + element)

            return output
