"""LeetCode 239: Sliding Window Maximum.

Problem: https://leetcode.com/problems/sliding-window-maximum/

Time complexity: O(n)
Auxiliary space complexity: O(k), excluding the output.
"""

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        result = []

        for i, value in enumerate(nums):
            # Remove indices outside the current window.
            while q and q[0] <= i-k:
                q.popleft()

            # Remove candidates dominated by the new value.
            while q and nums[q[-1]] <= value:
                q.pop()

            q.append(i)

            # The front contains the maximum of the complete window.
            if i >= k-1:
                result.append(nums[q[0]])

        return result
