"""LeetCode 1338: Reduce Array Size to The Half.

Problem: https://leetcode.com/problems/reduce-array-size-to-the-half/

Time complexity: O(n + k log k), where k is the number of distinct values
Space complexity: O(k)
"""

from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        freq = Counter(arr)

        # Remove the most frequent values first to minimize the set size.
        sorted_freq = dict(
            sorted(
                freq.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )

        total = 0
        counter = 0

        for item in sorted_freq:
            total += freq[item]
            counter += 1

            if n - total <= n // 2:
                return counter

        return counter
