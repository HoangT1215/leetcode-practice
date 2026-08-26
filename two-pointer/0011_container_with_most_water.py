"""LeetCode 11: Container With Most Water.

Problem: https://leetcode.com/problems/container-with-most-water/

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        best = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > best:
                best = area

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return best
