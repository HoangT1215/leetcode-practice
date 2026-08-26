"""LeetCode 1243: Array Transformation.

Problem: https://leetcode.com/problems/array-transformation/

Time complexity: O(n * d), where d is the number of transformation days
Space complexity: O(n)
"""

from typing import List


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        next_array = arr.copy()
        n = len(arr)

        while True:
            current = next_array.copy()

            for i in range(1, n - 1):
                if current[i] < current[i - 1] and current[i] < current[i + 1]:
                    next_array[i] += 1
                elif current[i] > current[i - 1] and current[i] > current[i + 1]:
                    next_array[i] -= 1

            # Exact equality works directly for Python lists.
            if current == next_array:
                return current
