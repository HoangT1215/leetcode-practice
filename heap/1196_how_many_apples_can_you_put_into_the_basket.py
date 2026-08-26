"""LeetCode 1196: How Many Apples Can You Put into the Basket.

Problem: https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

Time complexity: O(n log n) in the worst case
Space complexity: O(n), because the input is copied before heapification
"""

import heapq
from typing import List


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        remaining = 5000
        counter = 0

        # heapify builds the heap in O(n). Copy first to preserve the input list.
        heap = weight.copy()
        heapq.heapify(heap)

        while heap:
            value = heapq.heappop(heap)

            if value > remaining:
                break

            remaining -= value
            counter += 1

        return counter
