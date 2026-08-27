"""LeetCode 56: Merge Intervals.

Problem: https://leetcode.com/problems/merge-intervals/

Time complexity: O(n log n)
Space complexity: O(n) for the output list
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        final_list = [intervals[0].copy()]

        # Extract each interval's endpoints directly.
        for start, end in intervals[1:]:
            previous_end = final_list[-1][1]

            if start <= previous_end:
                # Take the maximum so a nested interval cannot shrink the
                # endpoint of the interval already in final_list.
                final_list[-1][1] = max(previous_end, end)
            else:
                # No overlap: begin a new merged interval.
                final_list.append([start, end])

        return final_list
