"""LeetCode 295: Find Median from Data Stream.

Problem: https://leetcode.com/problems/find-median-from-data-stream/

Time complexity:
    - addNum: O(log n)
    - findMedian: O(1)
Space complexity: O(n)
"""

import heapq


class MedianFinder:
    # Maintain a max-heap for the lower half and a min-heap for the upper half.

    def __init__(self):
        self.lower = []  # Max-heap represented using negative values.
        self.upper = []  # Min-heap.

    def addNum(self, num: int) -> None:
        # Place num into the appropriate half.
        if not self.lower or num <= -self.lower[0]:
            # num belongs at or below the largest value in the lower half.
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)

        # Keep the heaps equally sized, allowing lower one extra element.
        if len(self.lower) > len(self.upper) + 1:
            largest_lower = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, largest_lower)
        elif len(self.upper) > len(self.lower):
            smallest_upper = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -smallest_upper)

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return float(-self.lower[0])

        largest_lower = -self.lower[0]
        smallest_upper = self.upper[0]

        return (largest_lower + smallest_upper) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
